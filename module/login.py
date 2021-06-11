from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver import ActionChains
from datetime import datetime
import sys

class Login():

    SETTINGS = {
        'web': {
            'login'     : 'https://opensource-demo.orangehrmlive.com/index.php/auth/login',
            'dashboard' : 'https://opensource-demo.orangehrmlive.com/index.php/dashboard',
            'logout'    : ''
        },
        'remote_driver' : 'http://192.168.1.3:4444/wd/hub',
        'screenshot': {
            'path'      : 'output',
            'captured_images': {
                'login_form'      : '1-login-form.png',
                'login_prefilled' : '2-login-prefilled.png',
                'login_success'   : '3-login-success.png',
                'login_failed'    : '3-login-failed.png',
                'error'           : 'error.png'
            }
        },
        'test_account': {
            'username'  : 'Admin',
            'password'  : 'admin123'
        }
    }

    def __init__(self):
        
        driver = webdriver.Remote(f"{self.SETTINGS['remote_driver']}", webdriver.DesiredCapabilities.CHROME)

        print(self.get_datetime() + ' [INFO] Starting smoke testing.')

        driver.get(f"{self.SETTINGS['web']['login']}")
        print(self.get_datetime() + ' [INFO] Logging in url:' + driver.current_url + ' with page title:' + driver.title + '.')
        driver.save_screenshot(f"{self.SETTINGS['screenshot']['path']}/{self.SETTINGS['screenshot']['captured_images']['login_form']}")

        print(self.get_datetime() + ' [INFO] Typing a username.')
        input_username = driver.find_element_by_xpath('//*[@id="txtUsername"]')
        input_username.clear()
        input_username.send_keys(f"{self.SETTINGS['test_account']['username']}")
        
        print(self.get_datetime() + ' [INFO] Typing a password.')
        input_password = driver.find_element_by_xpath('//*[@id="txtPassword"]')
        input_password.clear()
        input_password.send_keys(f"{self.SETTINGS['test_account']['password']}")
        driver.save_screenshot(f"{self.SETTINGS['screenshot']['path']}/{self.SETTINGS['screenshot']['captured_images']['login_prefilled']}")

        print(self.get_datetime() + ' [INFO] Clicking the login button.')
        driver.find_element_by_xpath('//*[@id="btnLogin"]').click()
        
        print(self.get_datetime() + ' [INFO] Waiting for redirection.')

        try:
            WebDriverWait(driver,20).until(presence_of_element_located((By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/h1")))
        except:
            print(self.get_datetime() + ' [ERROR] Unable to redirect.')
            driver.save_screenshot(f"{self.SETTINGS['screenshot']['path']}/{self.SETTINGS['screenshot']['captured_images']['error']}")
            driver.close()
            sys.exit(self.get_datetime() + ' [ERROR] Automated smoke testing is unsuccessful. Process terminated.')

        if driver.current_url == f"{self.SETTINGS['web']['dashboard']}":
            print(self.get_datetime() + ' [INFO] Login successful and was redirected to page:' + driver.current_url + ' with page title:' + driver.title + '.')
            driver.save_screenshot(f"{self.SETTINGS['screenshot']['path']}/{self.SETTINGS['screenshot']['captured_images']['login_success']}")
        else:
            print(self.get_datetime() + ' [ERROR] Unable to login.')
            driver.save_screenshot(f"{self.SETTINGS['screenshot']['path']}/{self.SETTINGS['screenshot']['captured_images']['error']}")
            driver.close()
            sys.exit(self.get_datetime() + ' [ERROR] Automated smoke testing is unsuccessful. Process terminated.')

        print(self.get_datetime() + ' [INFO] Automated smoke testing is completed successfully. Closing the selenium webdriver.')
        driver.close()

    def get_datetime(self):

        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")