# pytest -v --driver Chrome --driver-path /mvideo-/Desktop/chrome/chromedriver.exe tests_rost.py

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from settings import *
import time


# 1. Ссылка на пользовательское соглашение работает

def test_terms_of_use_link_works():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'app-footer')))
    pytest.driver.find_element(By.LINK_TEXT, 'пользовательского соглашения').click()
    pytest.driver.switch_to.window(pytest.driver.window_handles[1])
    url = pytest.driver.current_url
    assert url == 'https://b2c.passport.rt.ru/sso-static/agreement/agreement.html'

# 2. Ссылка "Забыл пароль" ведёт на страницу восстановления пароля

def test_forgot_passport_link_redirection_correct():
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    pytest.driver.find_element(By.ID, 'forgot_password').click()
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    assert pytest.driver.find_element(By.CLASS_NAME, 'card-container__title').get_attribute("innerHTML") == 'Восстановление пароля'


# 3. На странице восстановления пароля присутствуют все необходимые поля.

def test_forgot_password_page_loading_correctly(go_to_forgot_password_page):
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'page-right')))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "captcha")))
    assert WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "rt-captcha__image")))


#4 Проверка названия кнопки "Продолжить" в форме "Регистрация"

def test_registration_page_use_continue_button():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[2]'))).send_keys(region)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[3]/div/input'))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        valid_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/button').text == 'Продолжить'



#5.Авторизация клиента по почте, раздел "Почта" с пустым полем Электронная почта

def test_empty_email_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите адрес, указанный при регистрации'


#6.Регистрация нового пользователя с паролем без единой цифры или спецсимвола

def test_no_numbers_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(no_numbers_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        no_numbers_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[4]/div[1]/span').text == 'Пароль должен содержать хотя бы 1 спецсимвол или хотя бы одну цифру'

# 6.Регистрация нового пользователя с паролем без букв

def test_no_letters_and_caps_password():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
    (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(
        no_letters_and_caps_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        no_letters_and_caps_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]').text == 'Пароль должен содержать хотя бы одну заглавную букву'



#7.Авторизация по почте с неверным емаилом и верным паролем

def test_invalid_email_valid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="form-error-message"]').text == 'Неверный логин или пароль'



#8.Авторизация через email с пустыми полями почта и пароль

def test_empty_email_empty_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(empty_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="username-meta"]').text == 'Введите адрес, указанный при регистрации'



#9.Регистрация с паролем более 20 символов

def test_big_password_sign_up():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-register"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[1]/div/input'))).send_keys(valid_name)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(
        (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/input'))).send_keys(valid_surname)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "address"))).send_keys(new_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(big_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password-confirm"))).send_keys(
        big_password)
    time.sleep(5)
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]').text == 'Длина пароля должна быть не более 20 символов'
