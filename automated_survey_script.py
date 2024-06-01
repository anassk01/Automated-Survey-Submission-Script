import time
import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configure Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

chrome_driver_path = "./chromedriver.exe"

# Initialize Chrome webdriver
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the Google Form
url = "https://docs.google.com/forms/d/e/1FAIpQLSdsCsQulq48RnAj_aGI_Uf8LlCwS3psJcFenWz-gxOERSqobQ/viewform"

# read survey responses from CSV file
with open('./fijii.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    survey_responses_list = []
    for row in reader:
        cleaned_row = {key.replace('\ufeff', ''): value for key, value in row.items()}
        survey_responses_list.append(cleaned_row)

# Iterate over each row of survey responses
for survey_responses in survey_responses_list:
    driver.get(url)
    
    # wait for the page to load 
    time.sleep(3)

    # find all question containers
    question_containers = driver.find_elements(By.CSS_SELECTOR, '.z12JJ')

    # loop through each question container
    for question_container in question_containers:
        # Get the question text
        question_text = question_container.find_element(By.CSS_SELECTOR, '.HoXoMd').text.strip()
        print(f"Question: {question_text}")  # Debugging statement

        # find the corresponding answers container
        answers_container = question_container.find_element(By.XPATH, './..').find_element(By.CSS_SELECTOR, '.lLfZXe')
        
        # get the desired answer from the CSV data
        desired_answer = survey_responses.get(question_text.strip())
        print(f"Desired Answer: {desired_answer}")  # Debugging statement
        
        if desired_answer:
            try:
                # find the radio button or checkbox with the desired answer
                answer_option = answers_container.find_element(By.XPATH, f".//label[normalize-space(.)='{desired_answer}']")
                print(f"Found Answer Option: {answer_option.text}")           
                # click the radio button or checkbox
                answer_option.click()
            except Exception as e:
                print(f"Error selecting answer for question '{question_text}': {str(e)}")  # Debugging statement

    # Submit the form 
    time.sleep(2)
    submit_button = driver.find_element(By.CSS_SELECTOR, '#mG61Hd > div.RH5hzf.RLS9Fe > div > div.ThHDze > div > div.lRwqcd > div > span')
    driver.execute_script("arguments[0].click();", submit_button)

    time.sleep(3)

driver.quit()
