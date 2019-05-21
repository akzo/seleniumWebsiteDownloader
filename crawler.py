###############################################
#     Made by a Web Analyst Anar Kazimov      #
#                   May 2019                  #
###############################################

from selenium import webdriver
import ahk

driver = webdriver.Chrome('chromedriver.exe') #driver for chrome 74 is attached
driver.get("https://employmentprogram.gov.bc.ca/Transition/SitePages/Home.aspx")

ahk.start()
ahk.ready()
ahk.execute("Send,^s")
ahk.execute("WinWaitActive, Save As,,2")
ahk.execute("WinActivate, Save As")
ahk.execute("Send, Transition\\file.htm")
ahk.execute("Send, {Enter}")

