from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


loginURL = 'https://swing.langara.bc.ca/prod/twbkwbis.P_WWWLogin'
browser = webdriver.Safari()
browser.get(loginURL)
studentID = browser.find_element_by_id('UserID')
studentID.send_keys(#ID#)
time.sleep(0.3)
password = browser.find_element_by_name('PIN')
password.send_keys(#password#)
time.sleep(0.3)
password.send_keys(Keys.ENTER)
time.sleep(1.3)
transcriptURL = 'https://swing.langara.bc.ca/prod/bwskotrn.P_ViewTran'
browser.get(transcriptURL)






