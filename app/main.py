def main():
    file_name = input("Enter file name: ")
    strings = []
    string = ""
    while not string == "stop" or string == "STOP":
        strings.append(string)
        string = input("Enter new string: ")
        if not string == "stop" or string == "":
            strings += "\n"
    strings = strings[2:]
    print(strings)
    result = "".join(strings)
    with open(f"{file_name}.txt", "w") as f:
        f.write(result)


if __name__ == "__main__":
    main()
