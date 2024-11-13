from pathlib import Path
import base64
import re

path = list(Path.cwd().rglob("\ufeff"))[0]

with open(path) as f:
    data = f.read()
    raw = base64.b64decode(data.encode()).decode()
    count = len(raw)
    random_value = re.search(r"ENIGMA\{(.+)\}", raw).group(1)
    print(f"ENIGMA{{{random_value}_{count}}}")
