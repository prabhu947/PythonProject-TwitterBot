from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# here you paste your chrome driver executing path otherwise it will not work
driver = webdriver.Chrome(executable_path='C:\\path\\to\\chromedriver.exe')

# Log in to your Twitter account
driver.get("https://twitter.com/login")
time.sleep(2)  

# Replace 'your_username' and 'your_password' with your Twitter credentials
username = driver.find_element_by_name("session[username_or_email]")
password = driver.find_element_by_name("session[password]")
username.send_keys("prabhunarayansingh2001@gmail.com")
password.send_keys("your_password")
password.send_keys(Keys.RETURN)
time.sleep(2)  # Allow time for the login to complete

#we can tweet, for that u must pass ur tweet in tweet_text
tweet_text = "Hello, Twitter! My name is prabhu narayan singh i have designed this twitter bot as a project #Automation"
tweet_box = driver.find_element_by_xpath('//div[@aria-label="Tweet text"]')
tweet_box.send_keys(tweet_text)
time.sleep(2)  # Allow time for typing
tweet_button = driver.find_element_by_xpath('//div[@data-testid="tweetButtonInline"]')
tweet_button.click()

# Close the browser after posting the tweet (you can modify this as needed)
time.sleep(5)  # Keep the browser open for a while to check the tweet
driver.quit()

