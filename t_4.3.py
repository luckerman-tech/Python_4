def file_processing(text: str, filename: str):
    with (open(filename, "a", encoding="utf-8") as file1,
          open(filename, "r", encoding="utf-8") as file2):
        file1.write(text) if file2.read() == '' else file1.write(f"\n{text}")

    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()
        for n in range(len(lines)):
            lines[n] = lines[n].strip("\n")

    print("Содержимое всех чётных строк файла:")
    for index, value in enumerate(lines, 1):
        if index % 2 == 0:
            print(value)


usertext = input("Введите текст, добавляемый в конец файла с новой строки: ")
while True:
    try:
        userfile = input("Введите имя файла: ")
        file_processing(usertext, userfile)
    except:
        print("Недопустимое имя файла!")
    else:
        break