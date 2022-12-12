def get_compartments(line):
    # Break line in the middle and return compartments
    line_length = len(line)
    return line[0:line_length//2], line[line_length//2:]


def get_priority_for_char(c):

    print(c)
    # turn character into a priority using ascii
    # conversion with an offset depending on upper or lower case
    if str.islower(c):
        return ord(c) - 96
    else:
        return ord(c) - 38


def get_elf_groupings():
    # Create line groups of 3

    with open("day-03-input.txt", "r") as f:
        lines = f.readlines()

        group_size = 3
        grouped = [lines[i:i+group_size] for i in range(0, len(lines), group_size)]

        return grouped



def solve_puzzle():

    total_score = 0
    groups = get_elf_groupings()

    for g in groups:
       score = max([get_priority_for_char(c) for c in g[0] if c in g[1] and c in g[2]])
       print(f"Score is: {score}")
       total_score += score

    print(f"Total score is: {total_score}")


if __name__ == "__main__":
    solve_puzzle()