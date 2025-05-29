import os 

link ="resources\cards better/"
cislo = 2

# Specify the folder path
folder_path = "./resources/cards better"  # <-- Change this to your actual folder path

# Get list of all file names in the folder
file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

# Print or save the list
print("Files in folder:")
print(file_list)

# Optionally, save to a text file
with open("file_list.txt", "w") as f:
    for i in range(4):
        for file_name in file_list:
            f.write(file_name + "," + str(cislo) + ",")
            cislo += 1
