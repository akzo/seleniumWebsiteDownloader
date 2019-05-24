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

# Getting the webpage name from the url
def extract_page_name(driver):
    url = driver.current_url
    match = re.search(r"\w*\.aspx", url)
    page = match.group(0)
    page = page.replace("aspx", "html")
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


def main():
    global website, destination
    driver = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
    driver.get(website)
    
    page = extract_page_name(driver)
    site_download(page, destination)

if __name__ == "__main__":
    # execute only if run as a script
    main()
    
