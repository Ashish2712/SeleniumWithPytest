"""
These tests cover DuckDuckGo searches
"""
import time

import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_basic_duckduckgo_search(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "polar bear"
    search_page.search_by_click(phrase)

    # Then the search result title contains "polar bear"
    assert phrase in result_page.title()

    # And the search result query is "polar bear"
    assert phrase == result_page.search_input_value()

    # And the search result links pertain to "polar bear"
    for title in result_page.result_link_titles():
        assert phrase.lower() in title.lower()

@pytest.mark.parametrize('phrase', ['panda', 'python', 'polar bear'])
def test_search_results_are_clickable(browser, phrase):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    search_page.load()
    search_page.search_by_click(phrase)

    # explicit wait for the conidition to appear true
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    WebDriverWait(browser, 10).until(EC.title_contains(phrase))
    assert phrase == result_page.search_input_value()
    result_page.click_search_result()
    time.sleep(10)
    result_page.title()



