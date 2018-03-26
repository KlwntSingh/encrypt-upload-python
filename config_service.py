import os
import Utils

def get_file_path(path):
    file_name = "CONFIG"
    path = Utils.remove_ending_slash(path)
    full_path = path + "/" + file_name
    return full_path

def get_config_file(path):
    full_path = get_file_path(path)
    if os.path.exists(full_path):
        with open(full_path, 'r') as file_obj:
            return file_obj.readlines()
    else:
        return []

def extract_name_from_file(lines):
    map = dict()
    for line in lines:
        words = line.split("=")
        map[words[0]] = words[1]
    return map.setdefault('name', '')

def get_repo_name(path):
    lines = get_config_file(path)
    return extract_name_from_file(lines)

def write_name(path, str):
    full_path = get_file_path(path)
    with open(full_path, 'w') as file_obj:
        file_obj.write("name=" + str.strip())