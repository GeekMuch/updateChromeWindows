import sys
import time
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# logger = logging.getLogger('')
# logger.setLevel(logging.DEBUG)
# fh = logging.FileHandler('my_log_info.log')
# sh = logging.StreamHandler(sys.stdout)
# formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(filename)s.%(funcName)s:%(lineno)d] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
# fh.setFormatter(formatter)
# sh.setFormatter(formatter)
# logger.addHandler(fh)
# logger.addHandler(sh)


pw = ""
with open("pass","r") as passwd:
    for x in passwd:
        pw = x

options = Options()
options.add_argument("--headless")
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)



def setup():
    driver.get("https://discord.com/login")
    time.sleep(1)
    print("\n[ * ] Logging in")

    time.sleep(3)
    print("\n[ * ] Finding sever & channel")
    driver.get("https://discord.com/channels/560130078453923840/892169248376512523")
    
    time.sleep(5)

def SirSpamAlot():
    count = 0
    # driver.find_element_by_css_selector('.closeButton-3PJ-TM').click()
    time.sleep(3)
    print("\n[ * ] Starting to spam")
    # logger.info("Starting SirSpamAlot")
    while(1):
        with open("profanity________list.txt","r") as dd:
            for i in dd:
                count += 1
                actions = ActionChains(driver)
                actions.send_keys('!urban '+i)
                actions.perform()
                send = driver.find_element_by_css_selector(".slateTextArea-1Mkdgw")
                send.send_keys(Keys.ENTER)
                
                print("[ + ] Word -> %s\t :\t Count -> %d " % (i.strip("\n"), count))
                time.sleep(5)
        dd.close()

if __name__ == "__main__":
    setup()
    # SirSpamAlot()
    