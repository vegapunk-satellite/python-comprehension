# Write a program that reads a text file with multiple lines and searches keywords the user enters via prompt.
# You can hard-code the file location in your code, you do not need to take it as a parameter.
# After reading the text file, it should ask the user what to search for: “Please enter a keyword: “.
# The user will enter a keyword (a single word). If the keyword exists in the text,
# it should print the entire line that contains the keyword. Otherwise, it should say “No result for <keyword>”.
# The program should keep asking for a new keyword and only terminate if the user enters “exit”. For example:
# “Please enter a keyword: football”
# “Found football: [We played football every weekend]”
# “Please enter a keyword: basketball”
# “No result for basketball”
# “Please enter a keyword: exit”
# “Exiting…” (and the program ends)

def read_lines_from_file(file_path):
    lines = []
    with open(source_file, 'r') as file:
        lines = [line.replace("\n", "") for line in file.readlines()]
    return lines

# print(source_lines)

def write_lines_to_file(lines):
    with open(source_file, 'w') as file:
        lines = [line + "\n" for line in lines]
        file.writelines(lines)

def is_keyword_in_line(keyword, line):
    words = line.split(" ")
    words = [word.lower() for word in words]
    return keyword.lower() in words

def find_first_line_with_keyword(keyword, lines) -> str:
    """ Returns the first line that contains keyword.
    If not such line is found, returns None"""
    for line in lines:
        if is_keyword_in_line(keyword, line):
            return line
    return None


source_file = "C:/Users/Asus/PycharmProjects/newproject/source.txt"
source_lines = read_lines_from_file(source_file)

while True:
    keyword = input("Please enter a keyword: ")
    if keyword == "exit":
        break
    for i in range(len(source_lines)):
        current_line = source_lines[i]
        if is_keyword_in_line(keyword, current_line):
            print(f"Found {keyword}: [{current_line}].")
            command = input("What would you like to do now? ")
            if command.lower().strip() == "continue":
                continue
            elif command.lower().strip() == "delete":
                print("Deleting...")
                del source_lines[i]
                write_lines_to_file(source_lines)
                break
            elif command.lower().strip().startswith("replace "):
                new_keyword = command.strip()[8:]
                print(f"Replacing {keyword} with {new_keyword}")
                source_lines[i] = current_line.replace(keyword, new_keyword)
                write_lines_to_file(source_lines)
                break
            elif command.lower().strip() == "edit":
                new_line = input("Please enter the new line: ")
                source_lines[i] = new_line
                write_lines_to_file(source_lines)
                break
    else:
        print(f"No more result for {keyword}.")
