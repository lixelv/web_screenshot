from url import *

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--force-dark-mode')
chrome_options.add_argument("--dark-mode")
chrome_options.add_argument(r"user-data-dir=C:\Users\user\AppData\Local\Google\Chrome\User Data\Default")

driver = webdriver.Chrome(options=chrome_options)

url = input('Введите ссылку на сайт: ')
while True:
    url = input('Введите ссылку на сайт: ')
    if url == '':
        break
    print(capture_full_page_screenshot(driver, url, width=width))
    
driver.quit()