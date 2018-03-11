import os

def getAllNestedDirectories(path):

    list_of_all_nested_directory = []

    if os.path.isfile(path):
        arr_path = path.split("/")
        if len(arr_path) > 1:
            final_path = "/".join(arr_path[:len(arr_path)- 1])
            list_of_all_nested_directory.append(final_path)

        return list_of_all_nested_directory


    list_directory_output = os.listdir(path)

    has_only_files = True
    for file in list_directory_output:
        file_path = path + "/" + file
        is_dir = os.path.isdir(file_path)
        # print(file_path)
        if(is_dir):
            list_of_all_nested_directory += getAllNestedDirectories(file_path)
            has_only_files = False

    if has_only_files:
        list_of_all_nested_directory.append(path)

    return list_of_all_nested_directory


def make_nested_directories(path, directories_to_make):
    for directory in directories_to_make:
        final_path = path + "/" + directory
        
        if not os.path.exists(final_path):
            os.makedirs(final_path)

def removeEndingSlashes(path):
    direc_array = path.split("/")
    if len(direc_array) > 2:
        direc_array = list(filter(lambda x: len(x) > 0, direc_array))

    output = "/".join(direc_array)
    # output = "/" + output
    return (output)

def get_all_files_in_paths(paths):
    final_list_of_finals = []
    
    for path in paths:
        list_of_directory_path = os.listdir(path)
        for file in list_of_directory_path:
            file_path = path + "/" + file
            if(os.path.isfile(file_path)):
                final_list_of_finals.append(file_path)
            else:
                final_list_of_finals += get_all_files_in_paths([file_path])

    return final_list_of_finals

def all_folder_upto_file_depth(paths):
    rTurn = []
    for path in paths:
        if(os.path.isfile(path)):
            rTurn.append("/".join(path.split("/")[:-1]))
        else:
            rTurn.append(path)

    return rTurn

def filteredPath(path):
    return removeEndingSlashes(path)

def checkIfDir(path):
    return os.path.isdir(path)

def parse_all_files_folder_from_user(arr):
    index = 1
    args = len(arr)
    for indexi in range(args):
        arg = arr[indexi]
        if checkIfDir(arg):
            arr[indexi] = filteredPath(arg)
    return arr

# makeAllNestedDirectories(".eu", getAllNestedDirectories("kulwant"))
# print(filteredPath("///"))