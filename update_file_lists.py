import os


def add_full_path(file_path, full_path_prefix):
    """
    Adds a specified full path prefix to each line's .wav file reference in the given file.

    Args:
        file_path (str): Path to the file to modify.
        full_path_prefix (str): Full path to prepend to each .wav file reference.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Modify each line by adding the full path prefix to the .wav filename
    modified_lines = []
    for line in lines:
        parts = line.strip().split('|')  # Split the line by "|"
        parts[0] = os.path.join(full_path_prefix, parts[0] + '.wav')  # Add full path to the .wav file name
        modified_lines.append('|'.join(parts) + '\n')

    # Save the modified lines back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

    print(f"Updated file paths in {file_path}")


# Define the path prefix to add and file paths to update
full_path_prefix = "" # path to wav files
file_paths = ['filelists/ljs_audio_text_test_filelist.txt', 'filelists/ljs_audio_text_train_filelist.txt', 'filelists/ljs_audio_text_val_filelist.txt']

# Update each file
for file_path in file_paths:
    add_full_path(file_path, full_path_prefix)
