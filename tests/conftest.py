"""
This module contains shared fixtures which will work as a 
setup and tear down for the test cases.
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def browser():

    # Intialize a webdriver
    b = webdriver.Chrome(ChromeDriverManager().install())

    # Implicity wait for 10 seconds everytime to let elements appear
    b.implicitly_wait(10)

    # return the webdriver instance
    yield b

    # quit the driver instance
    b.quit()