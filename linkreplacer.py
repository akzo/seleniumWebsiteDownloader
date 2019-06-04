###############################################
#     Made by a Web Analyst Anar Kazimov      #
#                   May 2019                  #
###############################################

# This script creates a list of all of the .html files in the folder
# Reverse engineers what the web url was
# Opense each file one by one, finds urls that are external linking and
# replaces them with local ones

import re
import os
from bs4 import BeautifulSoup

def replace_links(destination):
    files = []
    external_links = [] 
    #r = root, d = directories, f = files
    for r, d, f in os.walk(destination):
        for file in f:
            if '.html' in file:
                files.append(os.path.join(r, file))
                
    for f in files:
        external_links.append(reverse_eng_url(f, destination))

    html(files, external_links)

def reverse_eng_url(origin_url, destination):
    return origin_url.replace(destination, "").replace("-","/").replace("\\","/").replace("html", "aspx")

def html(files, external_links):
    for local in files:
        #open and read content of each file
        with open(local, "r+") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, "lxml")
            # find links in each file that contain external links and replace them with internal
            for internal, ext in zip(files, external_links):
                #print ext
                for a in soup.find_all("a", href=re.compile(ext)):
                    #print a
                    print(a['href']) 
                    print(internal)
                    a['href'] = internal #a[href] is found, internal also exists as a value, but for some reason internal doesn't get assigned to a[href]
                    print("new: " + a['href'])
            f.seek(0,2)
            f.write(str(soup))

def non_html_files(files):
    pass

if __name__ == "__main__":
    replace_links("C:\\Transition\\")
    
