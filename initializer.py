import sys
import os
import shutil
import Utils
from decrypter import decrypt_file as df
from encrypter import encrypt_file as ef

class App():

    def __init__(self, base_path):
        self.BASE_PATH = base_path
        self.EU_FOLDER_NAME = ".eu"
        self.ENCRYPTED_DATA_FOLDER_NAME = "/data"

        self.REPO_FOLDER = self.BASE_PATH + self.EU_FOLDER_NAME if self.BASE_PATH[-1] == '/' else self.BASE_PATH + "/" + self.EU_FOLDER_NAME
        self.ENCRYPTED_DATA_PATH = self.REPO_FOLDER + self.ENCRYPTED_DATA_FOLDER_NAME
        self.ENCRYPTED_FILE_EXTENSION_POST_FIX = ".enc"

        # ONLY FOR TESTING PURPOSES
        self.OUTPUT_FOLDER = self.BASE_PATH + "/data"

        self.init = self.initializer
        self.encrypt = lambda a: self.encrypt_files(a)
        self.decrypt = lambda a: self.decrypt_files(a)
        self.clean = self.clean_files

    def exit_from_app(self, msg):
        print(msg)
        sys.exit(1)

    def initializer(self):
        os.makedirs(self.REPO_FOLDER)

    def remove_base_path_from_path(self, path):
        """
        :param path: path is with base_path
        :return: path without surrounding slashes
        """
        path = "/" + Utils.remove_surrounding_slashes(path)

        base_path = Utils.remove_ending_slash(self.BASE_PATH)

        without_base_path = Utils.remove_surrounding_slashes(path.split(base_path)[1])
        return without_base_path

    def get_encrypted_file_or_folder_path(self, path):
        """

        :param path: path is with base_path
        :return: path has starting slash
        """
        path = Utils.remove_surrounding_slashes(path)
        base_path = Utils.remove_ending_slash(self.BASE_PATH)
        encrypted_data_path = Utils.remove_ending_slash(self.ENCRYPTED_DATA_PATH)

        path_without_base_path = self.remove_base_path_from_path(path)

        return encrypted_data_path + "/" + path_without_base_path


    def get_data_file_path(self, encrypted_path):
        """

        :param encrypted_path: path is with base_path
        :return: data_file_path with starting slash
        """
        encrypted_path = Utils.remove_surrounding_slashes(encrypted_path)

        repo_data_folder_name = Utils.remove_surrounding_slashes(
            self.EU_FOLDER_NAME) + "/" + Utils.remove_surrounding_slashes(self.ENCRYPTED_DATA_FOLDER_NAME)

        without_base_path = self.remove_base_path_from_path(encrypted_path)

        path_without_repo_data = Utils.remove_surrounding_slashes(without_base_path.split(repo_data_folder_name)[1])

        return Utils.remove_ending_slash(self.BASE_PATH) + "/" + path_without_repo_data

    def check_if_eu_dir(self):
        return os.path.exists(self.REPO_FOLDER)

    def get_encup_key(self):
        self.key = raw_input("Enter the key: ")

    def check_user_input_validity(self, path_for_files_and_folders):
        length = len(path_for_files_and_folders)
        for indexi in range(length):
            arg = path_for_files_and_folders[indexi]
            arg = Utils.get_absolute_path(arg)
            path_for_files_and_folders[indexi] = arg
            if not Utils.check_for_existence(arg):
                self.exit_from_app(arg + " does not exists ")
        return path_for_files_and_folders

    def encrypt_files(self, path_for_files_and_folders):
        self.get_encup_key()

        abs_path_for_files_and_folders = self.check_user_input_validity(path_for_files_and_folders)
        all_files = Utils.get_all_files_in_paths(abs_path_for_files_and_folders)
        all_folders = Utils.all_folder_upto_file_depth(all_files)

        encrypted_path_for_all_folders = map(self.get_encrypted_file_or_folder_path, all_folders)

        Utils.make_nested_directories(encrypted_path_for_all_folders)
        for file in all_files:
            out_file_path = self.add_encryption_extension(self.get_encrypted_file_or_folder_path(file))
            ef(self.key, file, out_file_path)

    def remove_init_folder_from_file_path(self, path):
        print(path.split(self.EU_FOLDER_NAME + self.ENCRYPTED_DATA_FOLDER_NAME + "/"))
        rTurn = "".join(path.split(self.EU_FOLDER_NAME + self.ENCRYPTED_DATA_FOLDER_NAME + "/"))

        return rTurn

    def remove_encrypted_extension(self, file_path):
        return file_path[:-len(self.ENCRYPTED_FILE_EXTENSION_POST_FIX)]

    def add_encryption_extension(self, file_path):
        return file_path + self.ENCRYPTED_FILE_EXTENSION_POST_FIX

    def decrypt_files(self, others):
        self.get_encup_key()

        all_encrypted_file_paths = Utils.get_all_files_in_paths([Utils.remove_ending_slash(self.ENCRYPTED_DATA_PATH)])
        all_encrypted_folder_paths = Utils.all_folder_upto_file_depth(all_encrypted_file_paths)

        all_data_folder_paths = map(self.get_data_file_path, all_encrypted_folder_paths)
        Utils.make_nested_directories(all_data_folder_paths)
        # print(map(lambda x: self.remove_init_folder_from_file_path(x), all_files))
        for file in all_encrypted_file_paths:
            out_file_path = self.get_data_file_path(self.remove_encrypted_extension(file))
            df(self.key, file, out_file_path)

    def clean_files(self, others):
        all_files_folders_inside_encrypted_data_folder = map(os.path.abspath,os.listdir(self.ENCRYPTED_DATA_PATH))

        for file in all_files_folders_inside_encrypted_data_folder:
            print(file)
            shutil.rmtree(file)