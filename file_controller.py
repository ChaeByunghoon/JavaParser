import os


class FileController:

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def get_path_file_list(self):
        self.file_list = os.listdir(self.input_path)
        temp_list = list()
        for file_name in self.file_list:
            if os.path.isfile(self.input_path + file_name):
                temp_list.append(self.input_path + file_name)
        return temp_list

    def get_output_path_list(self):
        temp_list = list()
        for file_name in self.file_list:
            if os.path.isfile(self.input_path + file_name):
                temp_list.append(self.output_path + file_name)
        return temp_list

    def read_files(self, path_list):
        code_list = list()
        for path in path_list:
            if os.path.isfile(path):
                f = open(path, "r", encoding="ascii", errors="surrogateescape")
                code = f.read()
                code_list.append(code)
                f.close()
        return code_list

    def file_out(self, output_path_list, node_list):
        print(len(output_path_list))
        print(len(node_list))
        for i in range(0, len(output_path_list)):
            f = open(output_path_list[i], "w")
            for j in range(0, len(node_list[i])):
                print(node_list[i][j], file=f)
            f.close()


