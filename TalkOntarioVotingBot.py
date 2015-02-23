from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
#Change this URL to the topic to be voted on
url = "https://talk.ontario.ca/idea/disenfranchise-beer-store-monopoly-celebrate-ontario-craft-beer-culture"
driver.get(url)

for i in range(0, 100):

	#Clear cookies to re-allow voting
	driver.delete_all_cookies()
	#Navigate to page
	driver.get(url)

	print "First: "
	print driver.find_element_by_css_selector('.rate-number-up-down-rating').text

	#Clicks upvote
	upvoteButton = driver.find_element_by_css_selector('[title=\'+1\']').click()
	time.sleep(3)
	
	print "After: "
	time.sleep(1)
	print driver.find_element_by_css_selector('.rate-number-up-down-rating').text


driver.close()