import sys
import os
import Utils
from decrypter import decrypt_file as df
from encrypter import encrypt_file as ef

class App():

    def __init__(self):
        self.INIT_FOLDER = ".eu"
        self.ENCRYPTED_PATH = self.INIT_FOLDER + "/data"
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

    def decrypt_files(self, others):
        self.get_encup_key()
        if not os.path.exists(self.INIT_FOLDER):
            os.makedirs(self.INIT_FOLDER)

        all_files = Utils.get_all_files_in_paths([self.ENCRYPTED_PATH])
        all_folders = Utils.all_folder_upto_file_depth(all_files)
        Utils.make_nested_directories(self.OUTPUT_FOLDER, map(lambda x: "/".join(x.split("/")[2:]), all_folders))
        df(self.key, all_files)