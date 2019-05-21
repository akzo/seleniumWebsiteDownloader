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

driver = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
driver.get(website)

# Getting the webpage name from the url
url = driver.current_url
match = re.search(r"\w*\.aspx", url)
page = match.group(0)
page = page.replace("aspx", "html")
print(page)

# Using hot keys to download the website

ahk.start()
ahk.ready()
ahk.execute("Send,^s")
ahk.execute("WinWaitActive, Save As,,2")
ahk.execute("WinActivate, Save As")
save_as = "Send, C:\\Transition\\" + page
save_as = save_as.encode('utf8')
print(type(save_as))


sent = "Send, C:\\Transition\\" + "Home.html"
print(type(sent))
ahk.execute(save_as)
ahk.execute("Send, {Enter}")



#\w*\.aspx
