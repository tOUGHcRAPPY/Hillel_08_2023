from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent.parent

file = open(ROOT_DIR / "rockyou.txt", encoding="utf-8")
lines: str = file.readlines()

word = "user"

def add_all_findings(file, word):
    result_list = []
    for line in lines:
        if word in line:
            result_list.append(line)
        else:
            continue
    return len(result_list)


def file_word_checker(file, word):
    result = []
    for line in lines:
        if word in line:
            while True:
                users_input = input(
                    f"Found line: '{line}'. \
                Add to result? (y/n) or type 'break' to close the program: "
                )
                if users_input == "y":
                    result.append(line)
                    print(f"{line=} has been added to {len(result)=}.")
                    break
                elif users_input == "n":
                    break
                elif users_input == "break":
                    break
                else:
                    print("Invalid input")
                    users_input = input(
                        f"Found line: '{line}'. \
                Add to result? (y/n) or type 'break' to close the program: "
                    )
            if users_input == "break":
                break
    return len(result)


add_all_result = add_all_findings(file, word)
print(add_all_result)


word_checker_result = file_word_checker(file, word)
print(word_checker_result)
