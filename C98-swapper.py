
def file_swap():
    print("Welcome to File  Swapper!")

    file1name = input("Enter name of first file: ")
    file2name = input("Enter name of second file: ")

    file1 = open(file1name).read()
    file2 = open(file2name).read()

    open(file1name, "w").write(file2)
    open(file2name, "w").write(file1)

    print("Files swapped successfully.")


file_swap()
