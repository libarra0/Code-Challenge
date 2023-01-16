import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Browser:
    browser, service = None, None

    # Initialise the webdriver with the path to chromedriver.exe
    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)
        print(browser.browser.title)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_session(self, username: str, password: str):
        self.add_input(by=By.ID, value='username', text=username)
        print(username)
        self.add_input(by=By.ID, value='password', text=password)
        print(password)
        self.click_button(by=By.XPATH, value='//*[@id="edit-actions"]/input')


if __name__ == '__main__':
    browser = Browser('YOUR_DRIVER_PATH')

    browser.open_page('https://clarity.dexcom.com')
    browser.click_button(by=By.XPATH, value="/html/body/div[1]/div[1]/div/div[3]/div/nav/ul/li[1]/div/a")
    time.sleep(1)

    browser.login_session(username='nilepatest001', password='Password@1')
    time.sleep(5)

    browser.close_browser()
