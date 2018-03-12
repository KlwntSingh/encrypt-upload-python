import sys
import os
import Utils
from decrypter import decrypt_file as df
from encrypter import encrypt_file as ef

class App():

    def __init__(self, base_path):
        self.BASE_PATH = base_path
        self.INIT_FOLDER = self.BASE_PATH + ".eu" if self.BASE_PATH[-1] == '/' else self.BASE_PATH + "/" + ".eu"
        self.ENCRYPTED_PATH = self.INIT_FOLDER + "/data"

        # ONLY FOR TESTING PURPOSES
        self.OUTPUT_FOLDER = "data"

        self.init = self.initializer
        self.encrypt = lambda a: self.encrypt_files(a)
        self.decrypt = lambda a: self.decrypt_files(a)

    def initializer(self):
        os.makedirs(self.INIT_FOLDER)

    def check_if_eu_dir(self):
        return os.path.exists(self.INIT_FOLDER)

    def get_encup_key(self):
        self.key = raw_input("Enter the key: ")

    def encrypt_files(self, files_and_folders):
        self.get_encup_key()
        files_and_folders = Utils.parse_all_files_folder_from_user(files_and_folders)
        all_files = Utils.get_all_files_in_paths(files_and_folders)
        all_folders = Utils.all_folder_upto_file_depth(all_files)
        Utils.make_nested_directories(self.ENCRYPTED_PATH, all_folders)
        ef(self.key, all_files)

    def remove_init_folder_from_file_path(self, path):
        return "/".join(path.split("/")[self.ENCRYPTED_PATH.split("/"):])

    def decrypt_files(self, others):
        self.get_encup_key()

        if not os.path.exists(self.INIT_FOLDER):
            os.makedirs(self.INIT_FOLDER)

        all_files = Utils.get_all_files_in_paths([self.ENCRYPTED_PATH])
        all_folders = Utils.all_folder_upto_file_depth(all_files)
        Utils.make_nested_directories(self.OUTPUT_FOLDER, map( self.remove_init_folder_from_file_path, all_folders))
        df(self.key, all_files)

    def clean_files(self):
        encrypted_files = Utils.get_all_files_in_paths([self.ENCRYPTED_PATH])
        unencrypted_files = map(self.remove_init_folder_from_file_path, encrypted_files)

        def recur_delete_directory(path):
            directory_path = "/".join(path.split("/")[:-1])
            if len(directory_path) > 0:
                files = os.listdir(directory_path)
                if len(files) == 0:
                    os.removedirs(directory_path)
                    recur_delete_directory(directory_path)

        for file in unencrypted_files:
            if os.path.exists(file):
                os.remove(file)
                recur_delete_directory(file)