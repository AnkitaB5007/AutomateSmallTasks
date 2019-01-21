import os

path = 'C:\Desktop\Desk Songs'
os.chdir(path)
for dirname, dirnames, filename in os.walk('.'):
    for subdirname in dirnames:
        old_path = os.path.join(dirname, subdirname)
        print(os.path.join(dirname, subdirname))
        if '_TS_' in old_path:

            os.rename(old_path, old_path.replace('_TS_', '_TC_'))
        if '_TC_' in old_path:

            os.rename(old_path, old_path.replace('_TC_', '_TS_'))
