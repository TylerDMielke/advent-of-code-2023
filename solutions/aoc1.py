from pathlib import Path


def main() -> None:
    input_path: Path = Path(__file__).parent.parent / 'input/aoc-input1.txt'

    number_list: list[int] = []
    with open(str(input_path), 'r') as fh:
        for line in fh.readlines():
            first_number: str = get_first_number(line)
            last_number: str = get_last_number(line)
            if first_number == last_number:
                last_number = get_word_number(line)
            number_list.append(int(f"{first_number}{last_number}"))

        the_sum: int = 0
        for number in number_list:
            the_sum += number

        print(the_sum)


def get_first_number(line: str) -> str:
    for iter in range(len(line)):
        if line[iter].isdigit():
            return line[iter]


def get_last_number(line: str) -> str:
    return get_first_number(line[::-1])


def get_word_number(line: str) -> str:
    words: list[str] = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for iter in range(len(words)):
        if words[iter] in line:
            print(f"Found Word: {words[iter]} {iter}")
            return str(iter + 1)


if __name__ == "__main__":
    main()