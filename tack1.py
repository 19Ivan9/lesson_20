from datetime import datetime

class File:
    COUNTER = 0
    def __init__(self,filename,method):
        self.__file = open(filename,method)
        self.__logger = open('logger.txt','a')

    def __enter__(self):
        self.__logger.write(f'Enter: {datetime.now().time()}. File info: {self.__file}\n')
        File.COUNTER += 1
        return self.__file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__logger.write(f'Exit: {datetime.now().time()}. File info: {self.__file}\n\n')
        self.__logger.close()
        self.__file.close()
        return print(f'Counter: {File.COUNTER}')

if __name__ == '__main__':

    with File('myfile.txt','w') as file:
        file.write('hello')
