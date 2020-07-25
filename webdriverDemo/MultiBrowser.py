import os
from datetime import time

from selenium import webdriver

CHROMEPATH = os.getcwd()+"/../DriverBinaries/chromedriver"
FFPATH = os.getcwd()+"/../DriverBinaries/geckodriver"

driver = webdriver.Chrome(executable_path=CHROMEPATH)
#driver = webdriver.Firefox(executable_path=FFPATH)

path = driver.get_screenshot_as_png();



driver.get("https://www.google.com")


driver.quit()
