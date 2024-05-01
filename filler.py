from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By 
import re
import time


def write_link_in_file(link):
    f = open("link.txt", "a")
    f.write(f"{link}\n")
    f.close()

def get_id_question(data):
    number = re.findall("\[\[(\d+),", data)[0]
    return number

def reconstruct_URL(numbers):
    responses = ""
    for idx, number in enumerate(numbers):
        response = input(f"qu'elle est la réponse choisis pour la question {idx}: ")
        if " " in response:
            response = response.replace(" ", "%20")
        responses =  responses + f"entry.{number}={response}&"
    number_link = input(f"Combien voulez-vous de lien avec ces réponses? ")
    number = int(number_link)
    while number > 0:
        write_link_in_file(f"{url}{responses}")
        number = number -1

with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())) as driver: 
    entry_numbers = []
    url = "https://docs.google.com/forms/d/e/1FAIpQLSfhksfXOmToYLq0G5JTfWiQJHYda6bvb3Vr9iMkACdk-M05dA/viewform?" 
    driver.get(url)
    parent_elements = driver.find_elements(By.XPATH, "//div[@class='Qr7Oae']")
    for parent_element in parent_elements:
        question_id = parent_element.find_element(By.XPATH, ".//div") 
        id = question_id.get_attribute("data-params")
        entry_numbers.append(get_id_question(id))
    reconstruct_URL(entry_numbers)
    time.sleep(5)






