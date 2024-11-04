class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self):
        try:
            with open(self.file_name, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return 'File Not Found'

    def append_file(self, text):
        try:
            with open(self.file_name, 'a') as file:
                file.write(text)
                return "Data Appended Successfully"
        except FileNotFoundError:
            return "File Not Found"


    def write_file(self, text):
        try:
            with open(self.file_name, 'w') as file:
                file.write(text)
                return "Data Appended Successfully"
        except FileNotFoundError:
            return "File Not Found"


file_1 = FileManager('hello world.txt')
print(file_1.read_file())
#print(file_1.append_file(f'\n{str(input('Напишите какой нибудь текст! '))}'))
print(file_1.write_file(f'{str(input('Напишите какой нибудь текст! '))}'))