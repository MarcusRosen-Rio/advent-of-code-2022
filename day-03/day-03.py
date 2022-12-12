def get_compartments(line):
    # Break line in the middle and return compartments
    line_length = len(line)
    return line[0:line_length//2], line[line_length//2:]


def get_priority_for_char(c):

    # turn character into a priority using ascii
    # conversion with an offset depending on upper or lower case
    if str.islower(c):
        return ord(c) - 96
    else:
        return ord(c) - 38


def solve_puzzle():

    total_score = 0

    # read file
    with open("day-03-input.txt", "r") as f:
        line = f.readline()
        while line != '':

            # Split into Compartments
            print(f"Line is: {line}")
            compartment1, compartment2 = get_compartments(line)
            #print(f"Compartments are: {compartment1}, {compartment2}")

            # Get unique characters in first compartment
            compartment_unique = "".join(set(compartment1))

            # get priority for each character the exists in both compartments and the max value
            score = max([get_priority_for_char(c) for c in compartment_unique if c in compartment2])
            total_score += score

            line = f.readline()

    print(f"Total score is: {total_score}")


if __name__ == "__main__":
    solve_puzzle()