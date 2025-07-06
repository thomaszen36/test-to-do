
import pytest



@pytest.fixture (scope="function")
def scenario_page(playwright, request) :
    new_browser = playwright.chromium.launch(headless=False)    #returns Browser obj/instance
    new_context = new_browser.new_context()     #returns Context obj/instance
    new_page = new_context.new_page()       #returns Page obj/instance
    yield new_page
    new_context.close()
    new_browser.close()



