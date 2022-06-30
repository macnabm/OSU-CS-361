import os
import random
from filewatcher import FileModified

FILENAME = 'prng-service.txt'
FULL_PATH = os.path.join(os.getcwd(), FILENAME)



def get_rand_positive_integer():
    return random.randint(0, 2**10)



def on_modify():
    print("File modified!")

    # bool go = false;
    go = False

    # arbitrary but we control what we write to the file, so we don't need extra logic
    with open(FULL_PATH, 'r') as f:
        if f.readlines()[0] == 'run':
            go = True

    # write the pseudo-random integer to the file
    # if (go) {
    if go:
        with open(FULL_PATH, 'w') as f:
            f.write(str(get_rand_positive_integer()))
    # }


def main():
    # FileModifiedHandler fmh(FULL_PATH, on_modify);
    file_modified_handler = FileModified(FULL_PATH, on_modify)
    # fmh.start();
    file_modified_handler.start()


if __name__ == "__main__":
    main()

