from selenium import webdriver
import pickle
import time
"""
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.binary_location = "/"
"""
driver = webdriver.Firefox()
driver.implicitly_wait(15)

driver.get('')
time.sleep(3)
cookies = pickle.load(open("cookiesbooking.pkl", "rb"))
for cookie in cookies:
	if cookie["domain"]!="admin.booking.com":
		driver.add_cookie(cookie)
		


time.sleep(1)
driver.get('')
time.sleep(1)
driver.find_element_by_id("loginname").send_keys("")
buttonXPath="/html/body/div/div/div[2]/div/div[1]/div[2]/div/div/div/form/div[3]/button"
driver.find_element_by_xpath(buttonXPath).click()
time.sleep(1)
buttonSingIn="/html/body/div/div/div[2]/div/div[1]/div[2]/div/div/div/form/button/span"
time.sleep(1)
driver.find_element_by_id("password").send_keys("")
driver.find_element_by_xpath(buttonSingIn).click()
time.sleep(5)

pickle.dump( driver.get_cookies() , open("cookiesbooking.pkl","wb"))
reservationLink=driver.find_element_by_partial_link_text('Reservations')
reservationLink.click()
time.sleep(1)
downloadButtonX="/html/body/main/section/div[2]/div/div/div[1]/div/button/span/span"
driver.find_element_by_xpath(downloadButtonX).click()
pickle.dump( driver.get_cookies() , open("cookiesbooking.pkl","wb"))

