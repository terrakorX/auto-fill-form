from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
from dotenv import load_dotenv
import os
import time

def autoclicker():
    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver: 
        entry_numbers = []
        with open(FILENAME) as f:
            for line in f:
                # line = "https://docs.google.com/forms/d/e/1FAIpQLSfj4fPpW7BzuefIDtIqqgSgT2r-m7Zxu1a5tKWgEwo_fd5PSQ/viewform?entry.1417948202=chien" 
                driver.get(line)
                results = driver.find_elements(By.XPATH,"//div[@role='button' and .//span[text()='Envoyer']]")
                for button in results:
                    driver.implicitly_wait(10)
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(20)



load_dotenv()

FILENAME = os.getenv('FILENAME')
autoclicker()
       






# def main():
#     print("enter an url of the form")




# if __name__ == "__main__":
#     main()
