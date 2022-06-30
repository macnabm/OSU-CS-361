import time
from PIL import Image
import os


# string PRNG_FILENAME = 'prng-service.txt';
PRNG_FILENAME = 'prng-service.txt'
IMAGE_FILENAME = 'image-service.txt'
IMG_DIR = os.path.join(os.getcwd(), 'img')


# void triggerPrngService(void) {
def trigger_prng_service():

    # FILE f = fopen(PRNG_FILENAME, 'w');
    # f << "run";
    # f.close();

    with open(PRNG_FILENAME, 'w') as f:
        f.write("run")
# }


def trigger_image_service():
    with open(PRNG_FILENAME, 'r') as f:
        num = int(f.readlines()[0])

    with open(IMAGE_FILENAME, 'w') as f:
        f.write(str(num))


def get_image_path():
    with open(IMAGE_FILENAME, 'r') as f:
        return f.readlines()[0]


def print_menu():
    print("1 - Generate Pseudorandom Image")
    print("2 - Exit")


def get_choice():
    # string choice;
    # cout << "Enter command: ";
    # cin >> choice;
    # return choice;
    command = input("Enter number for command (1 or 2): ")
    return command


def show_image(img_file):
    print(img_file)
    image = Image.open(os.path.join(IMG_DIR, img_file))
    image.show()


# int main() {
def main():
    while True:
        print_menu()
        command = get_choice()
        if command == '1':
            trigger_prng_service()
            time.sleep(1)
            trigger_image_service()
            time.sleep(1)
            show_image(get_image_path())
        elif command == '2':
            break
        else:
            print("Invalid command entered, please try again.\n")
#   return 0;
# }


if __name__ == "__main__":
    main()
