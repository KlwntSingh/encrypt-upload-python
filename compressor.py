import zipfile

def compress_folder(list_of_source_path, destination_path):
    with zipfile.ZipFile(destination_path, mode='w', compression=zipfile.ZIP_DEFLATED) as zip_file_obj:
        for file in list_of_source_path:
            zip_file_obj.write(file)


def decompress_folder(source_zip_file, destination_path):
    with zipfile.ZipFile(source_zip_file, 'r') as zip_file_obj:
        zip_file_obj.extractall(destination_path)