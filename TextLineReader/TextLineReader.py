import os

#************Specify the folder path where your text files are located**************
folder_path = input("Enter the folder path : ")


txt_files = []

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
        txt_files.append(filename)
print("*****************************Text File to be printed********************************************")
print("Text files which is being counted :\n", txt_files)
print("\n*****************************Here is Your Result************************************************\n")



total_lines = 0

for filename in os.listdir(folder_path):
    if filename.endswith('.txt'):
#*************Build the full path to the file************
        file_path = os.path.join(folder_path, filename)

#*************Open the file and count the lines**********
        with open(file_path, 'r') as file:
            lines = file.readlines()
            total_lines += len(lines)

print(f'Total Annonatations done with in the folder : {total_lines}')
print("\n************************************************************************************************")