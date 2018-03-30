import os
import shutil

def make_nested_directories(directories_to_make):
    for directory in directories_to_make:
        final_path = directory

        if not check_for_existence(final_path):
            make_deep_directory_path(final_path)

def remove_ending_slash(path):
    return path if path[-1:] != "/" else path[:-1]

def remove_starting_slash(path):
    return path if path[0:1] != "/" else path[1:]

def remove_surrounding_slashes(path):
    return remove_ending_slash(remove_starting_slash(path))

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
        if os.path.isfile(path):
            final_list_of_finals.append(path)
        else:
            list_of_directory_path = os.listdir(path)
            for index, file in enumerate(list_of_directory_path):
                file_path = path + "/" + file
                list_of_directory_path[index] = file_path
            final_list_of_finals += get_all_files_in_paths(list_of_directory_path)

    return final_list_of_finals

def all_folder_upto_file_depth(paths):
    rTurn = []
    for path in paths:
        if(check_if_file(path)):
            rTurn.append("/".join(path.split("/")[:-1]))
        else:
            rTurn.append(path)

    return rTurn

def filteredPath(path):
    return removeEndingSlashes(path)

def make_deep_directory_path(path):
    return os.makedirs(path)

def check_if_file(path):
    return os.path.isfile(path)

def check_if_directory(path):
    return os.path.isdir(path)

def get_absolute_path(path):
    return os.path.abspath(path)

def check_for_existence(path):
    return os.path.exists(path)

def delete_file(file):
    os.remove(file)

def remove_dir(fold):
    shutil.rmtree(fold)

# makeAllNestedDirectories(".eu", getAllNestedDirectories("kulwant"))
# print(filteredPath("///"))