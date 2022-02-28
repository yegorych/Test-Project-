import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.events import EventFiringWebDriver
from allure_commons.types import AttachmentType

class ScreenshotListener(AbstractEventListener):
    def on_exception(self, exception, driver):
        allure.attach(driver.get_screenshot_as_png(), name='screenError', attachment_type=AttachmentType.PNG)

def pytest_addoption(parser):
    """Опции командной строки.
    В командную строку передается параметр вида '--language="es"'
    По умолчанию передается параметр, включающий английский интерфейс в браузере
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption('language')

    # Инициализируются опции браузера
    options = Options()

    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    prebrowser = webdriver.Chrome(options=options)
    browser = EventFiringWebDriver(prebrowser, ScreenshotListener())
    #browser = webdriver.Remote(command_executor="http://selenium__standalone-chrome:4444/wd/hub")
    browser.implicitly_wait(5)
    yield browser
    browser.quit()