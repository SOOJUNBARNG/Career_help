import time
import pyperclip

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 고정 아이피
# https://docs.google.com/spreadsheets/d/1v4VS6LGvv7RGQMJbCWYN624npR-GEQZ8LdQWwdaUMS4/edit#gid=0

# https://www.reddit.com/r/programmingquestions/comments/112w1bl/hi_guys_im_making_an_automated_system_for_testing/?rdt=42411
# proxy_host = "YOUR_PROXY_HOST"
# proxy_port = "YOUR_PROXY_PORT"
# proxy_username = "YOUR_PROXY_USERNAME"
# proxy_password = "YOUR_PROXY_PASSWORD"

# proxy = Proxy()
# proxy.proxy_type = ProxyType.MANUAL
# proxy.http_proxy = f"{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
# proxy.ssl_proxy = f"{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}"
# capabilities = webdriver.DesiredCapabilities.CHROME proxy.add_to_capabilities(capabilities)
# driver = webdriver.Chrome(desired_capabilities=capabilities)

# Replace with your Naver credentials
username = "powwerer@daum.net"
password = "Ghostkill92!"
title = "동경시내 테슬라 차량 나라시 2만엔"
text = "주말만 가능\n핸드폰 : 08075328620\n카톡 : Ghost91114\nLine : jay911114\n직장인 기사님들 4명팀으로 운영중입니다. 안심하고 이용해주시면 감사하겠습니다."
repeats = 20  # Number of repetitions
interval = 10

def perform_action():
    count = 0
    while count < repeats:
        
        # Set the path to your Chrome WebDriver
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("webdriver.chrome.driver=C:/Users/staff/Documents/UDH/BeautyDarum/chromedriver.exe")  # Replace this path with your actual path to chromedriver.exe
        # chrome_options.add_argument("--headless") 
        
        # Start a browser session
        browser = webdriver.Chrome(options=chrome_options)

        # Open Naver login page
        browser.get('https://logins.daum.net/accounts/loginform.do?status=-401&url=https%3A%2F%2Flogins.daum.net%2Faccounts%2Fksso.do%3Frescue%3Dtrue%26url%3Dhttps%253A%252F%252Fcafe.daum.net%252F_c21_%252Fbbs_list%253Fgrpid%253DsT2%2526fldid%253D59QN')

        try:
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mArticle"]/div/div/div/div[2]/a/span[2]'))).click()
            time.sleep(4)

            pyperclip.copy(username)
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="loginId--1"]'))).send_keys(Keys.CONTROL, 'v')
            time.sleep(2)

            pyperclip.copy(password)
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="password--2"]'))).send_keys(Keys.CONTROL, 'v')
            time.sleep(1)

            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mainContent"]/div/div/form/div[4]/button[1]'))).click()
            time.sleep(5)

            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="cafe_write_article_btn"]/img'))).click()
            time.sleep(3)

            pyperclip.copy(title)
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="article-title"]/input'))).send_keys(Keys.CONTROL, 'v')
            time.sleep(1)

            pyperclip.copy(text)
            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="article-title"]/input'))).send_keys(Keys.CONTROL, 'v')
            time.sleep(1)

            WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="primaryContent"]/div/div[5]/div[2]/button'))).click()
            time.sleep(4)

        except Exception as e:
            print("Exception: ", e)

        browser.quit()
        count += 1

    time.sleep(interval)

def main():
    perform_action()

# Main実行
if __name__ == "__main__":

    # データを頂く
    main()