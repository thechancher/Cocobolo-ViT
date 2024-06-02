import os
import shutil

# the path of the complete database
dataset = r"C:\Users\yosua\Downloads\dataset-full"
# sorted database output
path = r"C:\Users\yosua\Downloads\BDBR"
train_path = os.path.join(dataset, "train")
test_path = os.path.join(dataset, "test")
validate_path = os.path.join(dataset, "validate")

for_train = 0.6 # % of data for train
for_test = 0.3 # % of data for test
# for_validate = "...the rest for validate"

def create_folder(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except OSError as e:
        print(f"Error creating '{path}': {e}")

def copy_file(src, dst):
    try:
        shutil.copy(src, dst)
    except FileNotFoundError:
        print("Couldn't find file in src.")
    except PermissionError:
        print("Denied permission to move file.")
    except Exception as e:
        print(f"Error moving: {e}")
        
def count_files(path):
    folders = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    
    for folder in folders:
        folder_path = os.path.join(path, folder)
        files = [name for name in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, name))]
        files_count = len(files)
        print(f"{files_count} files in folder {folder}")
        
        for_train = files_count*for_train
        for_test = for_train + files_count*for_test
        counter = 0
        for file in files:
            file_name = folder_path + "\\" + file
            folder_dst = folder_path.split("\\")
            folder_dst = folder_dst[-1]
            
            if counter < for_train:
                folder_dst = train_path + "\\" + folder_dst
            elif for_train <= counter < for_test:
                folder_dst = test_path + "\\" + folder_dst
            else:
                folder_dst = validate_path + "\\" + folder_dst
                
            create_folder(folder_dst)
            folder_dst = folder_dst + "\\" + file
            copy_file(file_name, folder_dst)
            
            counter += 1

create_folder(train_path)
create_folder(test_path)
create_folder(validate_path)

count_files(path)

