import os

folders = input("Please provide the list of folders with spaces in between : ").split()

for folder in folders:
    
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("Please provide a valid folder name : " + folder)
        continue
    except PermissionError:
        print("No access to this folder : " + folder)
        continue
        #break (break can used to stop the execution here)
    
    print("======= listing the files for the folder : " + folder)

    for file in files:
        print(file)