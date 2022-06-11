from time import sleep
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
import requests
from flask import Flask

app = Flask(__name__)
app.run(host="http://localhost:4723/wd/hub")

desired_caps = {
    'deviceName': '1946d9de0402',
    'platformName': 'Android',
    'platformVersion': '10',
    'deviceName': 'redmi',
    'appPackage': 'com.coinmarketcap.android',
    'appActivity': '.MainActivity',
    'noReset': True,  # no reset app
    'newCommandTimeout': 6000,
    'automationName': "UiAutomator2"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
sleep(5)
# go to static page
driver.find_element(AppiumBy.ID, "tab_explore").click()
sleep(2)
# select search bar
TouchAction(driver).tap(None, 171, 189, 1).release().perform()
sleep(2)
# input 'hi' to search bar
driver.find_element(AppiumBy.ID, "etContent").send_keys("hi")
sleep(2)
# select hi coin and go to info page
driver.find_element(AppiumBy.XPATH, "//*[contains(@text,'hi')]").click()
sleep(3)
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
driver.save_screenshot("C:\\Users\\user\\desktop\\endScreen.png")
# get API endpoint
driver.get_logs('driver')


# get API response
@app.route("/", methods=["GET"])
def getdata():
    response = requests.get("http://localhost:4723/wd/hub")
    return print(response.json())


sleep(5)
driver.quit()
