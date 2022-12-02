def main():
    elves = []

    file = open('input', 'r')
    str_lines = file.readlines()

    # part 1

    sum = 0
    for line in str_lines:
        if line == "\n":
            elves.append(sum)
            sum = 0
        else:
            sum += int(line)

    print(f"max: {max(elves)}")

    # Part two

    best_three = 0
    i = 0
    while i < 3:
        best_three += (max(elves))
        elves.remove(max(elves))
        i += 1

    print(f"best three: {best_three}")

main()