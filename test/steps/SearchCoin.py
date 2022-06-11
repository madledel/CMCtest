from behave import *
from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from pytest_bdd import scenario, given, when, then
import requests
from flask import Flask, jsonify
import json


use_step_matcher("re")
app = Flask(__name__)
driver = webdriver

@scenario('SearchCoin.feature', 'Check dollars changes within 7 days')
def searchcoin_feature():
    pass


@given('I am on CoinMarketCap homepage')
def step_impl(context):
    desired_caps = {
        'deviceName': '1946d9de0402',
        'platformName': 'Android',
        'platformVersion': '10',
        'deviceName': 'redmi',
        'appPackage': 'com.coinmarketcap.android',
        'appActivity': '.MainActivity',
        'noReset': True,  # no reset app
        'newCommandTimeout': 6000
    }
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    app.run(host="http://localhost:4723/wd/hub")
    sleep(4)


@when('I am on Static page')
def step_impl(context):
    driver.find_element(AppiumBy.ID, "tab_explore").click()
    sleep(2)
    pass


@then('I search hi coin with search bar')
def step_impl(context):
    TouchAction(driver).tap(None, 171, 189, 1).release().perform()
    sleep(2)
    driver.find_element(AppiumBy.ID, "etContent").send_keys("hi")
    sleep(2)
    pass


@then('I navigate to hi dollars info page')
def step_impl(context):
    driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'hi')]").click()
    sleep(3)
    pass


@then('I check hi dollars changes within 7 days')
def step_impl(context):
    TouchAction(driver).long_press(None, 900, 339, 1).move_to(None, 100, 339).release().perform()
    sleep(1)
    # go to historical data page
    driver.find_element(AppiumBy.ID, "historicalDataTab").click()
    sleep(3)
    driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'7d')]").click()
    sleep(1)
    # get change data
    print(driver.find_element(AppiumBy.ID, "change").text)
    sleep(3)
    driver.save_screenshot("C:\\Users\\user\\desktop\\endScreen.png")  # screenshot
    # request API data
    response = requests.post(driver)
    @app.route("/", methods=["GET"])
    def getdata():
        response = requests.get("http://localhost:4723/wd/hub")
    return print(response.json())

    driver.quit()
