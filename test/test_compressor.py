import os
import compressor as c
import unittest
import Utils
BASE_PATH = os.getcwd()

folder_to_zip = ".eu/"
destination_path = BASE_PATH + "/kulwant.zip"

class Internal_Methods(unittest.TestCase):

    # def testing_compression_of_files_in_folder(self):
    #     files = Utils.get_all_files_in_paths([folder_to_zip])
    #     print(files)
    #     c.compress_folder(files, destination_path)
    #     self.assertTrue(os.path.isfile(destination_path))

    # def testing_decompression_of_encup_repo(self):
    #     c.decompress_folder(destination_path, BASE_PATH)
    #     self.assertTrue(os.path.isdir(folder_to_zip))

    def testing_decompression_of_file_from_zip(self):
        c.extract_file(destination_path, ".eu/CONFIG", BASE_PATH + "/test")
        self.assertTrue(os.path.exists(BASE_PATH + "/test/.eu/CONFIG"))

if __name__ == '__main__':
    unittest.main()