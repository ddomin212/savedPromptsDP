def replace_string_in_file(file_path, old_str, new_str):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
            modified_content = file_content.replace(old_str, new_str)

        with open(file_path, 'w') as file:
            file.write(modified_content)

        print(f'Successfully replaced "{old_str}" with "{new_str}" in {file_path}.')
    except FileNotFoundError:
        print(f'File "{file_path}" not found.')

# Specify the file path
file_path = '/home/dan/Documents/savedPromptsDP/claude/analyza.md'

# Specify the string to be replaced and the new string
old_str = 'USER'
new_str = 'Daniel Dominko: \n---\n'

# Call the function to replace the string in the file
replace_string_in_file(file_path, old_str, new_str)

# Specify the string to be replaced and the new string
old_str = 'Poe'
new_str = 'Claude: \n---\n'

# Call the function to replace the string in the file
replace_string_in_file(file_path, old_str, new_str)

