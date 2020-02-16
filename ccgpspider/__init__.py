from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "http://search.ccgp.gov.cn/bxsearch"
executable_path = "/snap/bin/chromium.chromedriver"


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(
    executable_path=executable_path,
    chrome_options=chrome_options
    )

browser.get(url)
print(browser.page_source)
browser.quit()
