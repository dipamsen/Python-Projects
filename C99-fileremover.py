import os
import shutil
import time


def delete_files():
    thirtydays = 30*24*60*60
    print(thirtydays)
    current_time = time.time() - thirtydays

    print(current_time)
    deletedcount = 0
    folder_path = input("Enter folder path to delete files from: ")
    if(os.path.exists(folder_path)):
        all_files = os.walk(folder_path)
        # print(all_files)
        for (root_folder, folders, files) in all_files:
            for filename in files:
                # print(filename)
                filepath = os.path.join(folder_path, filename)
                created_time = os.stat(filepath).st_ctime
                print(filename)
                if(current_time < created_time):
                    print("Deleting " + filename)
                    deletedcount += 1
                    os.remove(filepath)
    else:
        print("Not found")


delete_files()
