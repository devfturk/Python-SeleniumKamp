from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep 
from selenium.webdriver.common.by import By
#devfturk

class TestSauce:
    def test_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text =="Epic sadface: Username is required"
        print(f"TEST SONUCU: {testResult}")


    def test_password(self):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("user")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text =="Epic sadface: Password is required"
        print(f"TEST SONUCU: {testResult}")


    def test_locked_out_user(self):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("locked_out_user")
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(1)
        errorMessage = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[2]/div[1]/div/div/form/div[3]/h3")
        testResult = errorMessage.text =="Epic sadface: Sorry, this user has been locked out."
        print(f"TEST SONUCU: {testResult}")


    def test_page(self):
        driver = webdriver.Chrome(ChromeDriverManager().install()) 
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(2)
        usernameInput = driver.find_element(By.ID,"user-name")
        usernameInput.send_keys("standard_user")
        passwordInput = driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        sleep(2)
        loginBtn = driver.find_element(By.ID, "login-button")
        loginBtn.click()
        sleep(5)
        testResult = driver.current_url == "https://www.saucedemo.com/inventory.html"
        print(f"TEST SONUCU : {testResult}")
        sleep(2)
        listOfItems = driver.find_elements(By.CLASS_NAME, "inventory_item")
        sleep(2)
        countResult = len(listOfItems) == 6
        print(f"Saucedemo sitesinde şu anda {len(listOfItems)} adet kurs var.")
        print(f"COUNT SONUCU : {countResult}")
        sleep(1000)

testClass = TestSauce()
#testClass.test_user()
#testClass.test_password()
#testClass.test_locked_out_user()
testClass.test_page()