def modify_content(content):
    """Modify content by converting it to uppercase"""
    return content.upper()


def main():
    print("Welcome to the file modification program!")
    filename = input("Please enter the filename to modify: ")
    print(f"Attempting to read the file: {filename}")

    try:
        with open(filename, "r") as file:
            content = file.read()
        print(f"Original content of {filename}:")
        print(content)
        modified_content = modify_content(content)

        new_filename = "modified_" + filename
        with open(new_filename, "w") as file:
            file.write(modified_content)

        print(f"Modified content written to {new_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied. Cannot read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
