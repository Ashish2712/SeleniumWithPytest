"""
This module contains shared fixtures which will work as a 
setup and tear down for the test cases.
"""

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
import json

@pytest.fixture
def config(scope='session'):

    # read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    # Assert values are acceptable
    assert config['browser'] in ['Firefox', 'Chrome', 'Headless Chrome']
    assert isinstance(config['implicit_wait'], int)
    assert config['implicit_wait'] > 0

    # Return config so it can be used
    return config

@pytest.fixture
def browser(config):

    # Intialize a webdriver instance based on config file
    if config['browser'] == 'Firefox':
        b = webdriver.Firefox(GeckoDriverManager().install())
    elif config['browser'] == 'Chrome':
        b = webdriver.Chrome(ChromeDriverManager().install())
    elif config['browser'] == 'Headless Chrome':
        opts = webdriver.chrome.options.Options()
        opts.add_argument('--headless')
        b = webdriver.Chrome(ChromeDriverManager().install(), options=opts)
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    # Implicity wait for 10 seconds everytime to let elements appear
    b.implicitly_wait(config['implicit_wait'])

    # return the webdriver instance
    yield b

    # quit the driver instance
    b.quit()