import os
from initializer import App
import unittest

BASE_PATH = os.getcwd()

app = App(BASE_PATH)

test_path = BASE_PATH + "/School"
encrypted_path = BASE_PATH + "/.eu/data/School"
test_path_without_base_path = "/School"

class Internal_Methods(unittest.TestCase):

    def testing_conversion_of_path_without_base_path(self):
        # print(app.remove_base_path_from_path(test_path))
        self.assertTrue(app.remove_base_path_from_path(test_path) == 'School' or app.remove_base_path_from_path(test_path) == '/School')

    def testing_conversion_of_path_without_base_path_to_without_base_path(self):
        # print(app.remove_base_path_from_path(test_path))
        self.assertTrue(app.remove_base_path_from_path(test_path_without_base_path) == 'School' or app.remove_base_path_from_path(test_path_without_base_path) == '/School')

    def testing_conversion_of_file_path_in_ecnrypted_form(self):
        # print(app.get_encrypted_file_path(test_path))
        self.assertTrue(app.get_encrypted_file_or_folder_path(test_path) == encrypted_path or app.get_encrypted_file_or_folder_path(test_path) == encrypted_path + "/")

    def testing_conversion_of_ecnrypted_form_in_file_path(self):
        # print(app.get_encrypted_file_path(test_path))
        self.assertTrue(app.get_data_file_path(encrypted_path) == test_path or app.get_data_file_path(encrypted_path) == test_path + "/")


if __name__ == '__main__':
    unittest.main()