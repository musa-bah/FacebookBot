# SELENIUM WILL HELP IN CONNECTING PYTHON TO THE WEB BROWSER.
# DOWNLOAD THE CHROME DRIVER IN THE PYTHON.EXT PATH.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Facebook:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.page = webdriver.Chrome()

    def login(self):
        # Get the user name and password fields by inspecting the page.
        page = self.page
        page.get('https://www.facebook.com/')
        time.sleep(2)
        username = page.find_element_by_id('email')
        password = page.find_element_by_name('pass')

        # Clear the fields to make sure they are empty.
        username.clear()
        password.clear()

        # Pass your user name and password to login to facebook
        username.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.ENTER)

        time.sleep(60)


facebook = Facebook('username', '[password]')
facebook.login()
# Testing my git repo.
# Second change.
# Another one

