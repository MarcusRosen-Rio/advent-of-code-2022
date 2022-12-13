from collections import deque
stacks = []


def get_stack_for_position(position):
    return stacks[position]


def determine_stack_based_on_char_position(index):

    if index == 2:
        return 0
    else:
        return int((index - 2) / 4)


def parse_stack_line(line):

    # Find all unique Characters in line
    chars = list(set([c for c in line if str.isalnum(c)]))

    for c in chars:

        # find indexes in line
        indexes = [(index, value) for index, value in enumerate(line, start=1) if value == c]
        print(indexes)

        for char_index, char_value in indexes:

            # Map Index to a stack position
            stack_position = determine_stack_based_on_char_position(char_index)
            get_stack_for_position(stack_position).append(char_value)


def populate_stacks(queue_lines):

    # Build stacks
    global stacks
    number_of_stacks = max(int(l) for l in queue_lines[0] if str.isnumeric(l))
    stacks = [deque() for i in range(number_of_stacks)]

    for line in queue_lines[1:]:
        parse_stack_line(line)


def execute_9001_move_instructions(number_to_move, source_stack, destination_stack):

    move_counter = 0
    items_to_move = []
    while move_counter != number_to_move:

        # remove from source stack
        print(f"Source Stack is {source_stack}")
        items_to_move.append(get_stack_for_position(source_stack).pop())
        move_counter += 1

    # Add back in same order (reverse removal)
    items_to_move.reverse()
    for s in items_to_move:

        # add to destination stack
        get_stack_for_position(destination_stack).append(s)




def execute_move_instruction(number_to_move, source_stack, destination_stack):

    move_counter = 0
    while move_counter != number_to_move:

        # remove from source stack
        print(f"Source Stack is {source_stack}")
        item = get_stack_for_position(source_stack).pop()

        # add to destination stack
        get_stack_for_position(destination_stack).append(item)

        move_counter += 1


def solve_puzzle():

    # read file
    with open("day-05-input.txt", "r") as f:

        # Read all lines
        lines = f.readlines()

        # Use line break to find queue/ instructions separation
        queue_lines = []
        for line in lines:
            if line != "\n":
                queue_lines.append(line.strip("\n"))
            else:
                break

        queue_lines = (list(reversed(queue_lines)))
        populate_stacks(queue_lines)

        instruction_lines = [l for l in lines if l.startswith("move")]

        for line in instruction_lines:
            _, number_to_move, _, source_stack, _, destination_stack = line.split()
            execute_9001_move_instructions(int(number_to_move), int(source_stack)-1, int(destination_stack)-1)

        # print the result (last item of each stack)
        print("".join([s[-1] for s in stacks]))


if __name__ == "__main__":
    solve_puzzle()