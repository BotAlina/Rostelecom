# pytest -v --driver Chrome --driver-path /mvideo-/Desktop/chrome/chromedriver.exe tests_rost.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from settings import *



#1. Регистрация пользователя со всеми верно заполненными полями

def test_register_positive(go_to_register_page):
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(valid_password)
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Зарегистрироваться'


#2. Регистрация пользователя с пустым полем "Имя"

def test_registration_page_with_empty_name_field():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(empty_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        valid_password)
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Зарегистрироваться'


#3. Регистрация пользователя с пустым полем "Фамилия"

def test_registration_page_with_empty_surname_field():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(empty_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        valid_password)
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Зарегистрироваться'


#4.Регистрация, если поле "Фамилия" содержит более 30-и символов


def test_registracion_page_with_big_surname():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(big_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(valid_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == ('Необходимо заполнить поле кириллицей. От 2 до 30 символов')

    #5.Регистрация с паролем менее 8 символов (3 символа)


def test_lesser_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(small_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        small_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Длина пароля должна быть не менее 8 символов'


#6.Регистрация если поля "Пароль" и "Подтверждение пароля" не совпадают

def test_password_and_passvord_confirm_is_not_are_the_same():
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.get(login_url)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
            (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
        WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
            big_password)
        time.sleep(5)
        assert driver.find_element(By.XPATH,
                                   '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]').text == 'Пароли не совпадают'


