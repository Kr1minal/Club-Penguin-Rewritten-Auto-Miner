import json
from time import sleep
from math import floor
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()
driver.set_window_position(0, 0)
driver.get("https://play.cprewritten.net/")
delay = 3

try:
    print("[-] Loading Page...")
    waitingForSite = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'cpr_client')))
    print("[+] Page is ready!\n")
except TimeoutException:
    print("Loading timed out.")

def start(positions):
    pos_obj = json.loads(positions)

    try:
        while True:
            for formula in pos_obj:
                e = driver.find_element_by_xpath('//*[@id="cpr_client"]')

                canvWidth = e.size['width']
                canvHeight = e.size['height']

                xFormula = formula['xFormula']
                yFormula = formula['yFormula']

                xAxis = floor(canvWidth / xFormula)
                yAxis = floor(canvHeight / yFormula)

                print(f"[+] Moving to X: {xAxis}, Y: {yAxis}")
                action = webdriver.common.action_chains.ActionChains(driver)
                action.move_to_element_with_offset(e, xAxis, yAxis)
                action.click()
                action.perform()
                sleep(.5)

                actions = webdriver.common.action_chains.ActionChains(driver)
                actions.send_keys("D")
                actions.perform()
                sleep(12)

    except KeyboardInterrupt:
        print("[!] Keyboard Interrupt")

positions = '[{"xFormula": 1.363076923076923, "yFormula": 1.6},{"xFormula": 1.363076923076923, "yFormula": 1.436182113882212},{"xFormula": 1.4190400390625, "yFormula": 1.513818984902872}]'

while True:
    option = input("[+] Type 'Start' To Start AutoMiner ").lower()
    if option == "start":
        start(positions)
    else:
        pass