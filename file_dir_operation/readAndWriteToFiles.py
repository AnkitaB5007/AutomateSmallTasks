import os


def copy_fileToMultipleFolder():

    # gives the complete path name of the file including the directory name like C:\
    file_to_be_copied_path = os.path.realpath('D:\DEXXConfigurationFile.txt')
    print('*****'+file_to_be_copied_path)

    head, tail = os.path.split(file_to_be_copied_path)
    print('head :'+head)
    print('org_file: '+tail)

    list_to_be_modified = []
    print('Please enter the path : ')
    #path = 'D:\REPOSITORIES\Ford_Automation_Gen3\NorthAmerica\VR'

    # walks through the list of directories and files
    path = 'D:\REPOSITORIES\Ford_Automation_Gen3_8Inch_MY18\Ford_Automation_Gen3_8Inch_MY18\Common\Climate'
    os.chdir(path)
    for dirname, dirnames, filename in os.walk('.'):
        for filenames in filename:
            a = os.path.join(dirname, filenames)
            if 'DEXXConfigurationFile_NA.txt' in a:
                print(a)
                list_to_be_modified.append(a)
    # Read from the original file and write contents to destination file present in multiple folders
    # in a directory
    for x in list_to_be_modified:
        with open('D:\\PythonTestPurpose\\test\DEXXConfigurationFile.txt', 'r') as f:
            with open (path+x, 'w') as fw:
                for lines in f:
                    fw.write(lines)



copy_fileToMultipleFolder()
