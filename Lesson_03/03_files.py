from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt", encoding="utf-8")
lines: list[str] = file.readlines()
print(len(lines))

file = open(ROOT_DIR / "rockyou.txt", encoding="utf-8")
chars: str = file.read()
print(len(chars))

file = open(ROOT_DIR / "rockyou.txt", encoding="utf-8")
chars: str = file.read()
counter = 0
while True:
    try:
        word = file.readline()
        counter += 1
        print(counter)
    except Exception:
        break
    
file.close()

print(counter)

# with open("rockyou.txt", "r", encoding='utf-8') as file:
#     lines = file.readlines()
#     print(len(lines))