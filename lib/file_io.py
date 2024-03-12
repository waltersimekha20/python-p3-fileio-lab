from pathlib import Path

def write_file(file_name, file_content):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, "a") as file:
        file.write("\n" + append_content)

def read_file(file_name):
    file_name_with_extension = str(file_name) + ".txt"
    with open(file_name_with_extension, "r") as file:
        content = file.read()
    return content
