from pathlib import Path

ROOT_DIR: Path = Path(__file__).absolute().parent.parent

# file = open(ROOT_DIR / "rockyou.txt", encoding="utf-8")
# lines: list[str] = file.readlines()
result: list[str] = []


def get_file_lines(filename: Path):
    file = open(filename)
    while True:
        line = file.readline()
        if not line:
            break

        yield line


for line in get_file_lines(ROOT_DIR / "rockyou.txt", encoding="utf-8"):
    user_input = input("Do you want to add the line: {line}?")
    if user_input == "yes":
        result.append(line)
    else:
        continue
