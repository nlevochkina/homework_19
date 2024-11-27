import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


def test_search():

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type("Appium")

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


def test_open_settings():
    with allure.step('Открываем меню'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/menu_overflow_button")).click()

    with allure.step('Заходим в настройки'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/explore_overflow_settings")).click()
        browser.all((AppiumBy.CLASS_NAME, "android.widget.TextView")).element_by(have.text('Settings')).should(be.visible)