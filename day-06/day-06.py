from itertools import islice
UNIQUE_WINDOW_SIZE=4

def is_window_unique(window):
    return len(window) == len(set(window))

def split_into_sliding_windows(line):
    return [line[i:i+UNIQUE_WINDOW_SIZE] for i in range(len(line)-2)]

def process_line(line):

    window = []
    for index, value in enumerate(line):
        window.append(value)

        if len(window) == UNIQUE_WINDOW_SIZE:
            print(is_window_unique(window))


def solve_puzzle():

    # read file
    with open("day-06-input.txt", "r") as f:
        line = None
        while line != '':
            line = f.readline().strip("\n")
            windows = split_into_sliding_windows(line)
            #print(windows)

            counter = 4
            for w in windows:
                if not is_window_unique(w):
                    counter += 1
                else:
                    print(f" {line}: First marker after character {counter}")
                    break


if __name__ == "__main__":
    solve_puzzle()