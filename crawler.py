###############################################
#     Made by a Web Analyst Anar Kazimov      #
#                   May 2019                  #
###############################################

from selenium import webdriver
import ahk
import time
import re


# URLs
website = "https://employmentprogram.gov.bc.ca/Transition/SitePages/Home.aspx"
destination = "C:\\Transition\\"

# Getting the webpage name from the url to create a corresponding folder
def extract_page_name(driver):
    url = driver.current_url
    match = re.search(r"\w*\/\w*\/\w*.aspx", url.decode('utf-8'), re.I | re.U)
    try:
        page = match.group(0)
    except AttributeError:
        return
    page = page.replace("aspx", "html")
    page = page.replace("/","-")
    return page

# Using hot keys to download the website
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

#Returns the list of links on the webpage
def list_of_links(driver):
    links = driver.find_elements_by_xpath("//a[@href]")
    links = list(dict.fromkeys(links))
    return links

def main():
    global website, destination
    driver = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
    driver.get(website)
    # Downloading the main webpage
    page = extract_page_name(driver)
    site_download(page, destination)
    
    
    # Find each link on the main webpage and download them as well
    visited_links = []
    links = list_of_links(driver)
    driver2 = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
    for link in links:
        if "javascript" in link.get_attribute("href"):
            continue
        if "#" in link.get_attribute("href"):
            continue
        if link not in visited_links:
            print link.get_attribute("href")
            visited_links.append(link)
            driver2.get(link.get_attribute("href"))
            page = extract_page_name(driver2)
            if page is None:
                continue
            site_download(page, destination)
        

   

    

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
