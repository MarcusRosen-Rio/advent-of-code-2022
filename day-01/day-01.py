
def solve_puzzle():
    # Read file, summaries each section, keep track of the largest grouping its number

    # Keep track of Elfs
    elf_counter = 1
    elf_calories = 0

    elf_with_most_carried_calories = 0
    most_calories_carried_by_elf = 0

    # read file
    with open("day-01-input.txt", "r") as f:
        line = f.readline()
        while line != '':

            # Keep Adding to current Elf
            if line != '\n':
                elf_calories += int(line)
                print(f"Elf: {elf_counter} - Calories: {elf_calories}")

            # "\n" only means new Elf
            else:

                print("New Elf discovered")

                # Check if Largest
                if elf_calories > most_calories_carried_by_elf:
                    most_calories_carried_by_elf = elf_calories
                    elf_with_most_carried_calories = elf_counter
                    print(f"Elf with most: {elf_with_most_carried_calories} - Calories: {most_calories_carried_by_elf}\n")

                # Reset Counters
                elf_calories = 0
                elf_counter = elf_counter+1

            line = f.readline()

    print(f"Largest Elf is {elf_with_most_carried_calories} Carrying {most_calories_carried_by_elf} Calories")

if __name__ == "__main__":
    solve_puzzle()