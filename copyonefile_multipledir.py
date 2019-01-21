import os
import shutil

# create a file in a directory


def make_file():
    path = os.getcwd()
    print(path)
    # os.getcwd()  is current working directory
    os.chdir(path)
    file = open('new.txt', mode='w')
    file.write('hello world')
    file.close()

# copy a file to multiple folders that are in a directory


def copy_fileToMultipleFolder():

    # gives the complete path name of the file including the directory name like C:\
    file_to_be_copied_path = os.path.realpath('new.txt')
    print('*****'+file_to_be_copied_path)

    head, tail = os.path.split(file_to_be_copied_path)
    print('head :'+head)
    print('org_file: '+tail)

    print('Please enter the path : ')
    path = 'C:\Desktop\Desk Songs'
    os.chdir(path)
    for dirname, dirnames, filename in os.walk('.'):
        for subdirname in dirnames:
            dest_path = os.path.join(dirname, subdirname)
            print(os.path.join(dirname, subdirname))
            # copies only the contents of a file
            shutil.copy(file_to_be_copied_path, dest_path)


make_file()
copy_fileToMultipleFolder()
