def generate_range(start, finish):
    return list(range(int(start), int(finish)+1))


def is_overlap(list1, list2):

    # Element-wise compare
    ls1 = [e for e in list1 if e in list2]
    ls2 = [e for e in list2 if e in list1]

    # Check for overlap
    return len(ls1) > 0 or len(ls2) > 0

def solve_puzzle():

    total_overlapping = 0

    # read file
    with open("day-04-input.txt", "r") as f:
        line = f.readline().strip("\n")
        while line != '':

            elf_1, elf_2 = line.split(",")
            elf_1_range = generate_range(*elf_1.split("-"))
            elf_2_range = generate_range(*elf_2.split("-"))
            print(elf_1_range, elf_2_range)

            if is_overlap(elf_1_range, elf_2_range):
                total_overlapping += 1

            line = f.readline()

    print(f"Total Overlapping: {total_overlapping}")

if __name__ == "__main__":
    solve_puzzle()