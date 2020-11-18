from selenium import webdriver
import pickle
import time 
browser = webdriver.Firefox()
browser.get('https://www.airbnb.it/')

time.sleep(120)


pickle.dump( browser.get_cookies() , open("cookiesairbnb.pkl","wb"))
browser.quit()