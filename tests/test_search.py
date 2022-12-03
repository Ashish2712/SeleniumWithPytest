"""
These tests cover DuckDuckGo searches
"""
from Selenium.pages.result import DuckDuckGoResultPage
from Selenium.pages.search import DuckDuckGoSearchPage

def test_basic_duckduckgo_search(browser):
    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "polar bear"
    # Given the DuckDuckGo home page is displayed
    search_page.load()

    # When the user searches for "polar bear"
    search_page.search(PHRASE)

    # Then the search result title contains "polar bear"
    assert PHRASE in result_page.title()

    # And the search result query is "polar bear"
    assert PHRASE == result_page.search_input_value()

    # And the search result links pertain to "polar bear"
    for title in result_page.result_link_titles():
        assert PHRASE.lower() in title.lower()

