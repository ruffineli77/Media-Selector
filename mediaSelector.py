
import random
import os
import time


def gather_files():
    returned_dict = {}
    returned_list = []
    app_folder = os.getcwd()
    # print(app_folder)
    walk_objects = [a for a in os.walk(app_folder)]

    # print(walk_objects)


    if not walk_objects[0][2] and not walk_objects[0][1]:  # indexing here doesnt work if the top dir is empty. Need to check if empty before this point
        print("test 1")
        print(f"No mp4 files found at {app_folder}")
        
        return 

    elif walk_objects[0][1]:
        print("Returning a dict")
        for tup in walk_objects:
            if tup[2]:
                returned_dict[tup[0]] = []  # this part is important for excluding empty dirs. Where should it go?
                # print(tup[2])

                for file in tup[2]:
                    filepath = os.path.join(tup[0], file)
                    if filepath.endswith(".mp4"):
                        # returned_dict[tup[0]] = []   # how can we use this line without resetting the list to be empty each loop.
                        returned_dict[tup[0]].append(filepath)
                    else:
                        # print("{file} not an mp4 file.")
                        pass
            else:
                pass

        return returned_dict

    elif walk_objects[0][2]:
        print("Returning a list")
        for file in walk_objects[0][2]:
            file_path = os.path.join(walk_objects[0][0], file)
            # print(file)
            if file.endswith(".mp4"):
                # print("mp4 file found")
                returned_list.append(file_path)
            else:
                pass

        return returned_list
                        

# aa = gather_files()
# print(aa)
# print(type(aa))
# print(aa[""])


def display_files(gath_files):
    folder_message = "Enter {} to select {}"
    for key_index, folder in enumerate(gath_files.keys()):
        folder_name = os.path.split(folder)[1]
        if key_index != 0:
            print(folder_message.format(key_index, folder_name))
        else:
            pass


# display_files(aa)


def choose_files():
    app_data = gather_files()
    # print(type(app_data))
    
    

    if isinstance(app_data, list):
        random_file = random.choice(app_data)
        print(random_file)
        print(f"Playing: {random_file}")
        os.startfile(random_file)

    elif isinstance(app_data, dict):
        display_files(app_data)
        folders = [f for f in app_data]
        pass
        # for folder in app_data.keys():
        #     print(folder)


        while True:
            try:
                folder_selection = int(input("\nYour Selection: "))

                
                if folder_selection == 0:
                    print(f"{folder_selection}\nEnter a valid folder number.")
                    pass

                # if 



                else:
                    selected_files = app_data[folders[folder_selection]]  # a list of filepaths loctaed in the selected folder
                    print(f"selected files: {selected_files}")
                    os.startfile(random.choice(selected_files))
                    break


            except IndexError as ie:  # folder could be enpty
                print(f"{ie}\nEnter a valid folder number.")

            except ValueError as ve:
                print(f"{ve}\nEnter a number.") 

    else:
        print("")

    # return folder_name


# choose_files()
