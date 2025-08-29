def read_and_modify_file():
    try:
        # Step 1: Ask user for the filename to read
        filename = input("Enter the filename to read: ")

        # Step 2: Open and read the file
        with open(filename, "r") as file:
            content = file.read()

        # Step 3: Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 4: Write the modified content to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"Modified content written to '{new_filename}' successfully!")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Could not read/write the file. Please check file permissions.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
read_and_modify_file()
