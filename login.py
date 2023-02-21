import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
 
    def test_a_success_login(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("problem_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)
    
    def test_b_failed_login_username_password_wrong(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs
        driver.find_element(By.ID,"user-name").send_keys("test") #isi email salah
        driver.find_element(By.ID,"password").send_keys("test") #isi password salah
        driver.find_element(By.ID, "login-button").click()

        #validasi
        response_data = driver.find_element(By.XPATH,"//*[@id='login_button_container']/div/form/div[3]/h3").text
        self.assertEqual(response_data, "Epic sadface: Username and password do not match any user in this service")

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()