from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com/")
inputGoogle = driver.find_element(By.NAME,"q")
inputGoogle.send_keys("kodlama.io")
searchButton = driver.find_element(By.NAME,"btnK")
#print(searchButton)
sleep(2)
searchButton.click()
sleep(2)
firstResult = driver.find_element(By.XPATH,"/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a")
firstResult.click()
listOfCourses = driver.find_elements(By.CLASS_NAME, "course-listing")
print(f"Kodlama.io sitesinde şu anda {len(listOfCourses)} adet kurs var.")
#/html/body/div[7]/div/div[11]/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div/div/div[1]/a
# //*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a
input()