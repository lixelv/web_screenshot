from url import *

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--force-dark-mode')

driver = webdriver.Chrome(options=chrome_options)

url = input('Введите ссылку на сайт: ')
while url != '':
    print(capture_full_page_screenshot(driver, url, width=width))
    url = input('Введите ссылку на сайт: ')
driver.quit()