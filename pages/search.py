"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckDuckGoSearchPage:
    
    # URL
    URL = "https://duckduckgo.com/"

    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')
    CLICK = (By.ID, 'search_button_homepage')

    # Initializer
    def __init__(self, browser):
        self.browser = browser
    
    # Interaction Methods
    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)

    def search_by_click(self, phrase):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase)
        click_icon = self.browser.find_element(*self.CLICK)
        click_icon.click()


        # search_input.send_keys(phrase + Keys.RETURN)
    