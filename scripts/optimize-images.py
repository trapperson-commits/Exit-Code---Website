"""Generate small grayscale WebP copies; never modify source photographs."""
from pathlib import Path
from io import BytesIO
import json
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'images' / 'optimalizalt'
OUT.mkdir(parents=True, exist_ok=True)
ASSETS = {
    'Képek/Ádám/exit-code-adam-besorolatlan-002.jpg': 'adam-nyito.webp',
    'Képek/Ádám/exit-code-adam-besorolatlan-004.jpg': 'adam-galeria.webp',
    'images/adam-wall-logo-v2.png': 'adam-fali-logo.webp',
    'images/joel-hero-logo-clean.png': 'joel-nyito.webp',
    'images/joel-gallery-logo-clean.png': 'joel-galeria.webp',
    'Név_Logo_Weboldalhoz/Jók/exit-code-LOGO_arculat-jo-001.jpg': 'ec-korlogo.webp',
    'Név_Logo_Weboldalhoz/Jók/exit-code-arculat-jo-003.jpg': 'exit-code-szologo.webp',
}
LIMIT = 66 * 1024
report = []
for source, name in ASSETS.items():
    original = ImageOps.exif_transpose(Image.open(ROOT / source))
    gray = ImageOps.grayscale(original)
    is_logo = 'logo' in name and not name.startswith('adam-')
    widths = [gray.width] if is_logo else [1400, 1280, 1152, 1024, 960]
    chosen = None
    for width in widths:
        image = gray.copy()
        image.thumbnail((width, width), Image.Resampling.LANCZOS)
        for quality in ([95, 90, 85, 80] if is_logo else [86, 82, 78, 74, 70, 66, 62, 58]):
            buffer = BytesIO()
            image.save(buffer, format='WEBP', quality=quality, method=6)
            if buffer.tell() <= LIMIT:
                chosen = (buffer.getvalue(), image.size, quality)
                break
        if chosen:
            break
    if chosen is None:
        raise RuntimeError(f'Could not meet size target: {source}')
    data, size, quality = chosen
    (OUT / name).write_bytes(data)
    report.append(dict(source=source, optimized='images/optimalizalt/' + name,
                       source_bytes=(ROOT / source).stat().st_size,
                       bytes=len(data), width=size[0], height=size[1], quality=quality))
    print(f'{name}: {size[0]}x{size[1]}, {len(data)/1024:.1f} KB, quality {quality}')
(OUT / 'meretjegyzek.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(f'Total: {sum(r["source_bytes"] for r in report)/1024/1024:.2f} MB -> {sum(r["bytes"] for r in report)/1024:.1f} KB')
