import os
from filewatcher import FileModified
from os import walk

FILENAME = 'image-service.txt'

# make sure you have a img folder
IMG_DIR = 'img'
FULL_PATH = os.path.join(os.getcwd(), FILENAME)
IMG_DIR_FULL_PATH = os.path.join(os.getcwd(), IMG_DIR)


def get_files(mypath):
    f = []
    for (_, _, filenames) in walk(mypath):
        f.extend(filenames)
        break
    return f


def on_modify():
    # get the pseudorandom number meant as an index into our list of files
    with open(FULL_PATH, 'r') as f:
        # prevent trying to read our own modification to the file
        contents = f.readlines()[0]
        if '.' in contents:
            return

        val = int(contents)

    # write the pseudorandom indexed filename back to the file
    with open(FULL_PATH, 'w') as f:
        files = get_files(IMG_DIR_FULL_PATH)
        f.write(files[val % len(files)])


def main():
    file_modified_handler = FileModified(FULL_PATH, on_modify)
    file_modified_handler.start()


if __name__ == "__main__":
    main()
