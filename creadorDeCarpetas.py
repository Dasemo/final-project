import os

folder_name = input("Enter folder name: ")
num_files = int(input("Enter number of files to create: "))

os.mkdir(folder_name)

for i in range(1, num_files+1):
    file_name = f"exercise{i}.py"
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w') as f:
        f.write("print()")

print(f"{num_files} files created in {folder_name} folder")