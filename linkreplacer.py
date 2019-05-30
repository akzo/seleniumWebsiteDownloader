###############################################
#     Made by a Web Analyst Anar Kazimov      #
#                   May 2019                  #
###############################################

# This script opens the 

import os

def replace_links(destination):
    files = []
    #r = root, d = directories, f = files
    for r, d, f in os.walk(destination):
        for file in f:
            if '.html' in file:
                files.append(os.path.join(r, file))
                
    for f in files:
        print(f)

if __name__ == "__main__":
    replace_links("C:\\Transition\\")
    print("suka")
