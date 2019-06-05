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

# VARIABLES
destination = "C:\\Transition\\"
website = "https://employmentprogram.gov.bc.ca/"

#This is the main func in the script.
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
    #non_html_files(files)
    
# Returns the external url for each local html file
def reverse_eng_url(origin_url, destination):
    return origin_url.replace(destination, "").replace("-","/").replace("\\","/").replace("html", "aspx")

# Replaces all of the external pointing links with their internal equivalents
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
                    print("local is: " + local)
                    print(a['href'])
                    print(internal)
                    a['href'] = internal #a[href] is found, internal also exists as a value, but for some reason internal doesn't get assigned to a[href]
                for a in soup.find_all("a", href=re.compile(ext+"#")):
                    a['href'] = internal
        f = open(local, "w")           
        #f.seek(0,2)
        f.write(str(soup))

# Replace non html external pointing files with internal ones
def non_html_files(files):
    # regex to find all non html files https:\/\/employmentprogram\.gov\.bc\.ca\/.+\.pdf|mp4
    for local in files:
        with open(local, "r+") as f:
            contents = f.read()
            soup = BeautifulSoup(contents, "lxml")
            
        print local
    

if __name__ == "__main__":
    replace_links(destination)
    
