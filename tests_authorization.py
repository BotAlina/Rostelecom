# pytest -v --driver Chrome --driver-path /mvideo-/Desktop/chrome/chromedriver.exe tests_rost.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from settings import *

#1.Авторизация по емаил

def test_email_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email


#2.Авторизация через email и неверным паролем

def test_valid_email_invalid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(invalid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'


#3.  Авторизация по номеру телефона, где поле "Моб.телефон" будет пустым

def test_empty_phone_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(empty_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/span').text == 'Введите номер телефона'


#4.Авторизация с неверными логином и паролем

def test_invalid_email_invalid_password_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-mail"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(invalid_email)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(invalid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    time.sleep(5)
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Авторизация'

#5.Авторизация клиента по номеру телефона

def test_phone_login():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(login_url)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "t-btn-tab-phone"))).click()
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "username"))).send_keys(valid_phone_number)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(valid_password)
    WebDriverWait(driver, 7).until(EC.visibility_of_element_located((By.ID, "kc-login"))).click()
    assert driver.find_element(By.XPATH,
                               '//*[@id="app"]/main/div/div[2]/div[1]/div[2]/div[2]/div/span[2]/span').text == valid_email
