from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import time   
import pytesseract
from PIL import Image 

def open():

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options = options)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://glauniversity.in:8085/")

    click_login = "/html/body/div[2]/section[1]/div/div/div/div/div[2]/div/div/form[1]/ul/li/input"
    first_click = driver.find_element(By.XPATH, click_login)
    first_click.click()

    roll_no = "/html/body/section[4]/div[1]/div/div[2]/form/div[1]/div/input"
    roll_send = driver.find_element(By.XPATH, roll_no)
    roll_send.click()
    roll_send.send_keys("2315001065")

    password = "/html/body/section[4]/div[1]/div/div[2]/form/div[2]/div/input"
    password_send = driver.find_element(By.XPATH, password)
    password_send.click()
    password_send.send_keys("BIYC")

    captcha = "/html/body/section[4]/div[1]/div/div[2]/form/div[3]/div[2]/div/img"
    captcha_read = driver.find_element(By.XPATH, captcha)
    image1 = captcha_read.screenshot('img.png')

    pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
    captcha_text = pytesseract.image_to_string(Image.open('img.png'))

    captcha_feild = "/html/body/section[4]/div[1]/div/div[2]/form/div[3]/div[1]/div/input"
    captcha_feild_find = driver.find_element(By.XPATH, captcha_feild)
    captcha_feild_find.click()
    captcha_feild_find.send_keys(captcha_text)

    login_button = "/html/body/section[4]/div[1]/div/div[2]/form/div[5]/div/a"
    login_button_find = driver.find_element(By.XPATH, login_button)
    
    try:
        login_button_find.click()
    except StaleElementReferenceException as sere:
        pass

    # result_button = "/html/body/div[1]/div[3]/div[1]/div[4]/div[1]/ul/li[13]/a"
    # result_button_find = driver.find_element(By.XPATH, result_button)
    # result_button_find.click()

    time.sleep(1000)

open()