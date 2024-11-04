class Logger:
    def __init__(self, file_name):
        self.file_name = file_name

    def log(self, message):
        try:
            with open(self.file_name, 'a') as f:
                f.write(message + '\n')
                return 'Message written successfully'
        except IOError:
            return 'File not found'

file_2 = Logger('log.txt')
count = 5
with count !=0:
    print(file_2.log(str(input('Напишите что то? '))))