import os


class FileController:

    def __init__(self, input_path):
        self.input_path = input_path

    def get_file_list(self):
        file_list = os.listdir(self.input_path)
        return file_list