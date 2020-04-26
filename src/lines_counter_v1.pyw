#os for file system
import os

from sys import platform as _platform

import fnmatch
import inspect

files = 0
lines = 0          

extension  = '.cpp'
extension2 = '.h'	

filename = inspect.getframeinfo(inspect.currentframe()).filename
startPath = os.path.dirname(os.path.abspath(filename))

with open("files_with_extensions.txt", "w", encoding="utf-8") as filewrite:
    for r, d, f in os.walk(startPath):
        for file in f:
            if file.endswith(extension) | file.endswith(extension2):

                if _platform == "linux" | _platform == "linux2":
                    ss = '/'
                elif _platform == "win32" | _platform == "win64":
                    ss = '\\'

                filePathAndName = r + ss + file

                files += 1

                filewrite.write(f"{filePathAndName}")
                
                fi = open(filePathAndName, 'r')
                pos = fi.tell()

                fileLines = 0
                while (True):
                    li = fi.readline()

                    # check for any hidden symbols
                    if li.isspace():
                        continue
                    
                    newpos = fi.tell()
                    fileLines += 1
                    if newpos == pos:  # stream position hasn't changed -> EOF
                        break
                    else:
                        pos = newpos

                lines += fileLines

                filewrite.write(f"{fileLines}\n")
                print(file + "  " + str(fileLines))

                fi.close()
  

    print(files)
    print(lines)

    filewrite.write(f"{files}\n")
    filewrite.write(f"{lines}\n")
