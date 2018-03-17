import zipfile

def compress_folder(list_of_source_path, destination_path, list_of_arc_name = []):
    if len(list_of_arc_name) == 0:
        list_of_arc_name = list_of_source_path
    with zipfile.ZipFile(destination_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file_obj:
        for index, file in enumerate(list_of_source_path):
            zip_file_obj.write(file, list_of_arc_name[index])


def decompress_folder(source_zip_file, destination_path):
    with zipfile.ZipFile(source_zip_file, 'r') as zip_file_obj:
        zip_file_obj.extractall(destination_path)

def extract_file(source_zip_file, file_name, destination_path):
    with zipfile.ZipFile(source_zip_file, 'r') as zip_file_obj:
        return (zip_file_obj.extract(file_name, destination_path))