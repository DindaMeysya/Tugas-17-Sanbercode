import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_d_remove_product_from_cart(self):
        # steps
        driver = self.browser #buka web browser
        driver.get("https://www.saucedemo.com/") #buka situs
        driver.find_element(By.ID,"user-name").send_keys("problem_user") #isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") #isi password
        driver.find_element(By.ID, "login-button").click()
        driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack").click() #klik add to cart
        driver.find_element(By.ID,"remove-sauce-labs-backpack").click() #klik remove untuk menghapus produk  dari keranjang

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"shopping_cart_link").text
        self.assertIn('', response_data)   

def tearDown(self):
    self.browser.close()

if __name__ == "__main__":
    unittest.main() 