import os


def main():
    path = input("Enter a directory or a file: ").strip()

    try:
        print(get_size(path), "bytes")
    except:
        print("Directory or file does not exist")


def get_size(path):
    size = 0

    if not os.path.isfile(path):
        lst = os.listdir(path)      # all files and subfolders
        for subdir in lst:
            size += get_size(path + "\\" + subdir)
    else:
        size += os.path.getsize(path)

    return size

if __name__ == "__main__":
    main()
