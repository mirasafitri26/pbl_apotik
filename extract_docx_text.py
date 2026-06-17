from pathlib import Path
import zipfile
import re
p = Path(r"c:\Users\LENOVO\Downloads\Dokumentasi_API_Apotek (1).docx")
if not p.exists():
    raise FileNotFoundError(p)
with zipfile.ZipFile(p, 'r') as z:
    xml = z.read('word/document.xml').decode('utf-8')
    texts = re.findall(r'<w:t[^>]*>(.*?)</w:t>', xml)
    text = ''.join(texts)
print(text[:12000])
