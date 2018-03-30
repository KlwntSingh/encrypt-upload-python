import sys
import os
import shutil
import getpass
from random import randint
import Utils
from decrypter import decrypt_file as df
from encrypter import encrypt_file as ef
import config_service as config
import compressor
class App():

    def __init__(self, base_path):
        self.command_without_eu_dir = ['init', 'unzip']
        self.BASE_PATH = Utils.remove_ending_slash(base_path)
        self.EU_FOLDER_NAME = ".eu"
        self.ENCRYPTED_DATA_FOLDER_NAME = "/data"

        self.REPO_FOLDER = self.BASE_PATH + "/" + self.EU_FOLDER_NAME
        self.ENCRYPTED_DATA_PATH = self.REPO_FOLDER + self.ENCRYPTED_DATA_FOLDER_NAME
        self.ENCRYPTED_FILE_EXTENSION_POST_FIX = ".enc"

        self.CONFIG_FILE = "CONFIG"

        # ONLY FOR TESTING PURPOSES
        self.OUTPUT_FOLDER = self.BASE_PATH + "/data"

        self.init = self.initializer
        self.encrypt = lambda a: self.encrypt_files(a)
        self.decrypt = lambda a: self.decrypt_files(a)
        self.zip = self.zip_repo
        self.unzip = lambda x: self.unzip_repo(x[0])
        self.clean = self.clean_files

    def exit_from_app(self, msg):
        sys.exit(1)

    def initializer(self, other):
        if not os.path.exists(self.REPO_FOLDER):
            os.makedirs(self.REPO_FOLDER)
        else:
            print("encup repo already initialized")
        name = config.get_repo_name(self.REPO_FOLDER)
        name = name if name else "Default"
        new_name = raw_input("Please Enter the name of repo[{n}]: ".format(n=name))
        new_name = new_name if new_name else name
        config.write_name(self.REPO_FOLDER, new_name)

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

    def get_password(self, st):
        return getpass.getpass(st)

    def get_encup_key(self):
        self.key = self.get_password("Enter the Key: ")

    def confirm_password(self, key):
        if key == self.get_password("Confirm the Key: "):
            return True
        else:
            return False

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
        while not self.confirm_password(self.key):
            print("Does not match. Please enter the Key again!")
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
        all_encrypted_files_folders_in_encrypted_data_folder = map(lambda x: Utils.remove_ending_slash(self.ENCRYPTED_DATA_PATH) + "/" + x, os.listdir(self.ENCRYPTED_DATA_PATH))
        for index, file in enumerate(all_files_folders_inside_encrypted_data_folder):
            if Utils.check_if_file(all_encrypted_files_folders_in_encrypted_data_folder[index]):
                if Utils.check_if_file(self.remove_encrypted_extension(file)):
                    Utils.delete_file(self.remove_encrypted_extension(file))
            else:
                shutil.rmtree(file)


    def zip_repo(self, others):
        name = config.get_repo_name(self.REPO_FOLDER)

        all_files = Utils.get_all_files_in_paths([self.REPO_FOLDER])
        all_files_without_base_path = list(map(self.remove_base_path_from_path, all_files))
        destination_path = Utils.remove_ending_slash(self.BASE_PATH) + "/" + name +".zip"
        compressor.compress_folder(all_files, destination_path, all_files_without_base_path)

    def unzip_repo(self, path):
        config_file_path = self.EU_FOLDER_NAME + "/" + self.CONFIG_FILE
        destination_file_name = self.BASE_PATH +"/"+ str(randint(0,1000))
        compressor.extract_file(path, config_file_path, destination_file_name)
        name = config.get_repo_name(destination_file_name + "/" + self.EU_FOLDER_NAME)
        full_path_for_repo = self.BASE_PATH + "/" + name
        Utils.make_nested_directories([full_path_for_repo])
        compressor.decompress_folder(path, full_path_for_repo)

        Utils.remove_dir(destination_file_name)