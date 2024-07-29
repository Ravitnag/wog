from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import ChromiumOptions
from selenium.webdriver.common.by import By
import sys

chrome_options = ChromiumOptions()
service = Service(ChromeDriverManager().install(), options=chrome_options)

driver = webdriver.Chrome(service=service)

def test_score_service(url):
    driver.get(url)
    score = driver.find_element(By.ID, 'score').text
    print(score)
    score = int(score)
    return 1 <= score <= 1000


def main_function(url):
    if test_score_service(url):
        sys.exit(0)
    else:
        sys.exit(1)


main_function("http://localhost:8777")
