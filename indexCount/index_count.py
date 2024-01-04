# Line Count Script by Index Number across the files in folder
'''
This Python script reads text files in a specified folder,
 extracts the index number from the beginning of each line,
 and provides the total occurrences of each unique index across all files.
'''

import os


def count_line_indices(folder_path):
    line_count = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, "r") as file:
                for line_number, line in enumerate(file):
                    try:
                        # Extract the index number from the beginning of each line
                        index = int(line.split()[0])
                        key = (index, line_number)
                        line_count[key] = line_count.get(key, 0) + 1
                    except ValueError:
                        # Ignore lines that don't start with a valid integer
                        pass

    return line_count


def total_occurrences(line_count):
    total_count = {}

    for (index, line_number), count in line_count.items():
        total_count[index] = total_count.get(index, 0) + count

    return total_count


folder_path = input("Enter the folder path: ")
result = count_line_indices(folder_path)
total_result = total_occurrences(result)

for index, total_count in total_result.items():
    print(f"Index {index}: {total_count} total occurrences across all files")
