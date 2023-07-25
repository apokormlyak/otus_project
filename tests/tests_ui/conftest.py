import pytest
import os.path
from selenium import webdriver
from selenium.webdriver.chrome import service


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome')
    parser.addoption('--driver_folder', default='/home/alisapokormlyak/Desktop/drivers')
    parser.addoption('--url', default='https://www.openbrewerydb.org/')
    parser.addoption("--executor", action="store", default="127.0.0.1")
    parser.addoption("--bversion", action="store", default="114.0")
    parser.addoption("--vnc", action="store_true", default=False)
    parser.addoption("--logs", action="store_true", default=False)
    parser.addoption("--videos", action="store_true", default=False)


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('--browser')
    driver_folder = request.config.getoption('--driver_folder')
    executor = request.config.getoption("--executor")
    version = request.config.getoption("--bversion")
    vnc = request.config.getoption("--vnc")
    logs = request.config.getoption("--logs")
    videos = request.config.getoption("--videos")

    driver = None

    if executor == 'local':

        if browser_name.lower() == 'chrome':
            driver = webdriver.Chrome(executable_path=os.path.join(driver_folder, '/chromedriver'))
        elif browser_name.lower() == 'firefox':
            driver = webdriver.Firefox(executable_path=os.path.join(driver_folder, '/geckodriver'))
        elif browser_name.lower() == 'opera':
            webdriver_service = service.Service(executable_path=os.path.join(driver_folder, '/operadriver'))
            webdriver_service.start()
            capabilities = {
                'operaOptions': {
                    'binary': '/usr/lib/x86_64-linux-gnu/opera'
                }
            }

            driver = webdriver.Remote(webdriver_service.service_url, capabilities)

    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        chrome_options = webdriver.ChromeOptions()
        chrome_options.set_capability("browserVersion", version)
        chrome_options.set_capability("screenResolution", "1280x1024")
        chrome_options.set_capability("selenoid:options", {
                "sessionTimeout": "60s",
                "enableVNC": vnc,
                "enableVideo": videos,
                "enableLog": logs
            })

        driver = webdriver.Remote(
            command_executor=executor_url,
            options=chrome_options
        )

    yield driver

    driver.close()


@pytest.fixture
def url(request):
    return request.config.getoption('--url')
