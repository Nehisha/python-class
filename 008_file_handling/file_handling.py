file_pointer = open("hello.csv")  # file pointer
content = file_pointer.read()
file_pointer.seek(0)  # seek vaneko jati choti read garna ni milcha
print(content)
arko_content = file_pointer.read()
print("Arko content: ", arko_content)


with open("introduction.txt", "w+") as file_pointer:
    file_pointer.write("Mero nam Nehisha Hirachan ho. \n")
    file_pointer.write("Ma srijana chowk tira baschu. \n")
    file_pointer.seek(0)

    lines = file_pointer.readlines()

    for line in lines:
        print(line, end="")
