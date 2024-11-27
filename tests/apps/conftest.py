import os
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from dotenv import load_dotenv
# from utils.attach import attach_video
from selene.support.shared import browser


def pytest_addoption(parser):
    parser.addoption(
        '--platform',
        action='store',
        default='ios')


@pytest.fixture(scope='function', autouse=True)
def mobile_management(request):
    load_dotenv()
    username = os.getenv('userName')
    accesskey = os.getenv('accessKey')
    remote_url = os.getenv('remote_url')
    platform = request.config.getoption('--platform')

    if platform == 'ios':
        options = XCUITestOptions().load_capabilities({
            "platformName": "ios",
            "platformVersion": "16.0",
            "deviceName": "Iphone 13",
            "app": "bs://sample.app",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": username,
                "accessKey": accesskey
            }
        })
        browser.config.driver = webdriver.Remote(remote_url, options=options)
    else:
        options = UiAutomator2Options().load_capabilities({
            "platformName": "android",
            "platformVersion": "9.0",
            "deviceName": "Google Pixel 3",
            "app": "bs://sample.app",
            'bstack:options': {
                "projectName": "First Python project",
                "buildName": "browserstack-build-1",
                "sessionName": "BStack first_test",
                "userName": "bsuser_ImvQHC",
                "accessKey": "c7LWdmq1gr4AJ1BR5V4g"
            }
        })
        browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()

