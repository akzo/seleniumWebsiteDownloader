###############################################
#     Made by a Web Analyst Anar Kazimov      #
#                   May 2019                  #
###############################################

#Visit the website and downloads all of the .aspx pages

from selenium import webdriver
import ahk
import time
import re
from linkreplacer import *


# CONSTANTS TO BE CHANGED FROM PROJECT TO PROJECT
website = "https://employmentprogram.gov.bc.ca/Transition/SitePages/Home.aspx"
destination = "C:\\Transition\\"
avoid_urls_with_these_words = ["javascript", "#", "Lists"] #program would not download pages containing this word in the url
base = "https://employmentprogram.gov.bc.ca/Transition" #the base sublink that should be in each link. This will prevent downloading outside websites

#--------------------------------------------------------------------------------------------------------------------#
# Getting the webpage name from the url to create a corresponding file. This was adjusted for the Transition subsite
# that's why we extract it as word/word/word.aspx
#--------------------------------------------------------------------------------------------------------------------#
def extract_page_name(driver):
    url = driver.current_url
    match = re.search(r"\w*\/\w*\/\w*.aspx", url)
    try:
        page = match.group(0)
    except AttributeError:
        return
        
    page = page.replace("aspx", "html")
    page = page.replace("/","-")
    return page
    
#---------------------------------------------------------------------------------------------------------------------------#
# Using hot keys to download the website. We are replicating what the user does when downloading the website from the browser
#---------------------------------------------------------------------------------------------------------------------------#
def site_download(page, destination):
    ahk.start()
    ahk.ready()
    ahk.execute("Send,^s")
    ahk.execute("WinWaitActive, Save As,,2")
    ahk.execute("WinActivate, Save As")
    
    save_as = "Send, " + destination + page
    save_as = save_as.encode('utf8')
    ahk.execute(save_as)
    ahk.execute("Send, {Enter}")
    ahk.execute("Send, {Enter}") 
#--------------------------------------------#
#Returns the list of links on the webpage
#--------------------------------------------#
def list_of_links(driver):
    links = driver.find_elements_by_xpath("//a[@href]")
    links = list(dict.fromkeys(links))
    return links

#Downloads the homepage then goes to every link reachable from home
def main(site,depth, processed_links):
    global avoid_urls_with_these_words
    global base
    if depth >= 3:
        return
    
    global website, destination
    driver = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
    driver.get(site)
    # Downloading the main webpage
    page = extract_page_name(driver)
    site_download(page, destination)
    
    
    # Find each link on the main webpage and download them as well 
    visited_links = []
    links = list_of_links(driver)
    driver2 = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
    for link in links:
        url = link.get_attribute("href").split('?')[0]
        
        if any(word in url for word in avoid_urls_with_these_words):
            continue
        if base not in url:
            continue
        if url not in processed_links:
            print url + str(depth)
            #visited_links.append(link)
            processed_links.append(url)
            driver2.get(url)
            page = extract_page_name(driver2)
            if page is None:
                continue
                                
            site_download(page, destination)
            
            main(url, depth+1, processed_links)

   

   

    

if __name__ == "__main__":
    processed_links = []
    main(website, 0, processed_links)
    #replace_links(destination)
    print processed_links
