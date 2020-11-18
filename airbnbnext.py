from selenium import webdriver
import pickle
import time
import os
"""
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/"
"""
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', os.getcwd())
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')

driver = webdriver.Firefox(firefox_profile=profile)

driver.get('https://www.airbnb.it/hosting/reservations/upcoming')

cookies = pickle.load(open("cookiesairbnb.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)
    #print(cookie)

driver.get('https://www.airbnb.it/hosting/reservations/upcoming')
csvUrl='https://www.airbnb.it/hosting/reservations/export.csv?sort_field=status&sort_order=asc&status=accepted&tab=upcoming&page=1'
listaPaginePath='/html/body/div[3]/div/div[1]/div[2]/div/section/footer/div/nav/span/div/ul'
listaPagine=driver.find_element_by_xpath(listaPaginePath)
print(listaPagine.getSize())
#driver.get(csvUrl)

time.sleep(10)
pickle.dump( driver.get_cookies() , open("cookiesairbnb.pkl","wb"))
