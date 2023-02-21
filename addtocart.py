import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_c_add_to_cart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs
        driver.find_element(By.ID,"user-name").send_keys("problem_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()
        cart_link = driver.find_element(By.CLASS_NAME,"shopping_cart_link").text
        cart_badge=0
        if (self.assertIn('', cart_link) == False): 
            cart_badge = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() #klik add to cart untuk memasukan ke keranjang

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
        self.assertIn(str(cart_badge+1), response_data)

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main()