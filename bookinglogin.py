from selenium import webdriver
import pickle
import time 
browser = webdriver.Firefox()
browser.get('https://admin.booking.com/')

time.sleep(120)


pickle.dump( browser.get_cookies() , open("cookiesbooking.pkl","wb"))
browser.quit()