from selenium import webdriver
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from time import sleep
import message_telegram

def Find_Element(driver : webdriver.Chrome, by, value : str) -> WebElement:
    while True:
        try:
            element = driver.find_element(by, value)
            break
        except:
            pass
        sleep(0.1)
    return element

def Find_Elements(driver : webdriver.Chrome, by, value : str) -> list[WebElement]:
    while True:
        try:
            elements = driver.find_elements(by, value)
            if len(elements) > 0:
                break
        except:
            pass
        sleep(0.1)
    return elements

def Send_Keys(element : WebElement, content : str):
    element.clear()
    for i in content:
        element.send_keys(i)
        sleep(0.2)

def wait_url(driver : webdriver.Chrome, url : str):
    # print(url)
    while True:
        cur_url = driver.current_url
        if cur_url == url:
            break
        sleep(1)

def madrid(driver, city_number):
    nie = input('Please input N.I.E : ')
    fullname = input('Please input Fullname : ')
    date = input('Please input date : ')
    driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    sleep(0.5)
    while True:
        region_menu = Find_Element(driver, By.CSS_SELECTOR, 'select[autocomplete="address-level1"]')
        region_items = region_menu.find_element(By.TAG_NAME, 'option')
        Select(region_menu).select_by_index(33)
        sleep(1)
        accept_btn1 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplustiem/citar?p=28&locale=es')
        sleep(0.5)
        police_menu = Find_Element(driver, By.NAME, 'tramiteGrupo[0]')
        police_items = police_menu.find_element(By.TAG_NAME, 'option')
        Select(police_menu).select_by_index(2)
        sleep(1)
        accept_btn2 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn2)
        sleep(1)

        # wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplustiem/acInfo')
        enter_btn = Find_Element(driver, By.ID, 'btnEntrar')
        driver.execute_script('arguments[0].click();', enter_btn)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplustiem/acEntrada')
        sleep(0.5)
        input_nie = Find_Element(driver, By.ID, 'txtIdCitado')
        Send_Keys(input_nie, nie)
        sleep(1)
        input_fullname = Find_Element(driver, By.ID, 'txtDesCitado')
        Send_Keys(input_fullname, fullname)
        sleep(1)
        input_date = Find_Element(driver, By.CSS_SELECTOR, 'input[title="Fecha de Caducidad de tu tarjeta actual"]')
        Send_Keys(input_date, date)
        sleep(1)
        next_btn1 = Find_Element(driver, By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplustiem/acValidarEntrada')
        sleep(0.5)
        next_btn2 = driver.find_element(By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn2)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplustiem/acCitar')
        sleep(0.5)
        try:
            sign_btn = driver.find_element(By.ID, 'btnSiguiente')
            driver.execute_script('arguments[0].click();', sign_btn)
            print('Success!')
            message_telegram.send_message(city_number)
            break
        except:
            pass
        try:
            back_btn = driver.find_element(By.ID, 'btnSalir')
            driver.execute_script('arguments[0].click();', back_btn)
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)
        except:
            driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)

def caceres(driver, city_number):
    nie = input('Please input N.I.E : ')
    fullname = input('Please input Fullname : ')
    birth = input('Please input year of birth : ')
    nationality_number = input('Please input Nationality Number in Excel file : ')
    driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    sleep(0.5)
    while True:
        region_menu = Find_Element(driver, By.CSS_SELECTOR, 'select[autocomplete="address-level1"]')
        region_items = region_menu.find_element(By.TAG_NAME, 'option')
        Select(region_menu).select_by_index(12)
        sleep(1)
        accept_btn1 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/citar?p=10&locale=es')
        sleep(0.5)
        police_menu = Find_Element(driver, By.NAME, 'tramiteGrupo[1]')
        police_items = police_menu.find_element(By.TAG_NAME, 'option')
        Select(police_menu).select_by_index(2)
        sleep(1)
        accept_btn2 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn2)
        sleep(1)

        # wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acInfo')
        enter_btn = Find_Element(driver, By.ID, 'btnEntrar')
        driver.execute_script('arguments[0].click();', enter_btn)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acEntrada')
        sleep(0.5)
        input_nie = Find_Element(driver, By.ID, 'txtIdCitado')
        Send_Keys(input_nie, nie)
        sleep(1)
        input_fullname = Find_Element(driver, By.ID, 'txtDesCitado')
        Send_Keys(input_fullname, fullname)
        sleep(1)
        input_birth = Find_Element(driver, By.ID, 'txtAnnoCitado')
        Send_Keys(input_birth, birth)
        nationality_menu = Find_Element(driver, By.ID, 'txtPaisNac')
        nationality_items = nationality_menu.find_element(By.TAG_NAME, 'option')
        Select(nationality_menu).select_by_index(nationality_number)
        sleep(1)
        next_btn1 = Find_Element(driver, By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acValidarEntrada')
        sleep(0.5)
        next_btn2 = driver.find_element(By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn2)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acCitar')
        sleep(0.5)
        try:
            sign_btn = driver.find_element(By.ID, 'btnSiguiente')
            driver.execute_script('arguments[0].click();', sign_btn)
            print('Success!')
            message_telegram.send_message(city_number)
            break
        except:
            pass
        try:
            back_btn = driver.find_element(By.ID, 'btnSalir')
            driver.execute_script('arguments[0].click();', back_btn)
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)
        except:
            driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)

def albacete(driver, city_number):
    nie = input('Please input N.I.E : ')
    fullname = input('Please input Fullname : ')
    birth = input('Please input year of birth : ')
    nationality_number = input('Please input Nationality Number in Excel file : ')
    driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    sleep(0.5)
    while True:
        region_menu = Find_Element(driver, By.CSS_SELECTOR, 'select[autocomplete="address-level1"]')
        region_items = region_menu.find_element(By.TAG_NAME, 'option')
        Select(region_menu).select_by_index(2)
        sleep(1)
        accept_btn1 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/citar?p=2&locale=es')
        sleep(0.5)
        police_menu = Find_Element(driver, By.NAME, 'tramiteGrupo[0]')
        police_items = police_menu.find_element(By.TAG_NAME, 'option')
        Select(police_menu).select_by_index(13)
        sleep(1)
        accept_btn2 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn2)
        sleep(1)

        # wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acInfo')
        enter_btn = Find_Element(driver, By.ID, 'btnEntrar')
        driver.execute_script('arguments[0].click();', enter_btn)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acEntrada')
        sleep(0.5)
        input_nie = Find_Element(driver, By.ID, 'txtIdCitado')
        Send_Keys(input_nie, nie)
        sleep(1)
        input_fullname = Find_Element(driver, By.ID, 'txtDesCitado')
        Send_Keys(input_fullname, fullname)
        sleep(1)
        input_birth = Find_Element(driver, By.ID, 'txtAnnoCitado')
        Send_Keys(input_birth, birth)
        sleep(1)
        nationality_menu = Find_Element(driver, By.ID, 'txtPaisNac')
        nationality_items = nationality_menu.find_element(By.TAG_NAME, 'option')
        Select(nationality_menu).select_by_index(nationality_number)
        sleep(1)
        next_btn1 = Find_Element(driver, By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acValidarEntrada')
        sleep(0.5)
        next_btn2 = driver.find_element(By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn2)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acCitar')
        sleep(0.5)
        try:
            sign_btn = driver.find_element(By.ID, 'btnSiguiente')
            driver.execute_script('arguments[0].click();', sign_btn)
            print('Success!')
            message_telegram.send_message(city_number)
            break
        except:
            pass
        try:
            back_btn = driver.find_element(By.ID, 'btnSalir')
            driver.execute_script('arguments[0].click();', back_btn)
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)
        except:
            driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)

def valladolid(driver, city_number):
    nie = input('Please input N.I.E : ')
    fullname = input('Please input Fullname : ')
    birth = input('Please input year of birth : ')
    nationality_number = input('Please input Nationality Number in Excel file : ')
    driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    sleep(0.5)
    while True:
        region_menu = Find_Element(driver, By.CSS_SELECTOR, 'select[autocomplete="address-level1"]')
        region_items = region_menu.find_element(By.TAG_NAME, 'option')
        Select(region_menu).select_by_index(50)
        sleep(1)
        accept_btn1 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/citar?p=47&locale=es')
        sleep(0.5)
        police_menu = Find_Element(driver, By.NAME, 'tramiteGrupo[1]')
        police_items = police_menu.find_element(By.TAG_NAME, 'option')
        Select(police_menu).select_by_index(3)
        sleep(1)
        accept_btn2 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn2)
        sleep(1)

        # wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acInfo')
        enter_btn = Find_Element(driver, By.ID, 'btnEntrar')
        driver.execute_script('arguments[0].click();', enter_btn)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acEntrada')
        sleep(0.5)
        input_nie = Find_Element(driver, By.ID, 'txtIdCitado')
        Send_Keys(input_nie, nie)
        sleep(1)
        input_fullname = Find_Element(driver, By.ID, 'txtDesCitado')
        Send_Keys(input_fullname, fullname)
        sleep(1)
        input_birth = Find_Element(driver, By.ID, 'txtAnnoCitado')
        Send_Keys(input_birth, birth)
        sleep(1)
        nationality_menu = Find_Element(driver, By.ID, 'txtPaisNac')
        nationality_items = nationality_menu.find_element(By.TAG_NAME, 'option')
        Select(nationality_menu).select_by_index(nationality_number)
        sleep(1)
        next_btn1 = Find_Element(driver, By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acValidarEntrada')
        sleep(0.5)
        next_btn2 = driver.find_element(By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn2)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acCitar')
        sleep(0.5)
        try:
            sign_btn = driver.find_element(By.ID, 'btnSiguiente')
            driver.execute_script('arguments[0].click();', sign_btn)
            print('Success!')
            message_telegram.send_message(city_number)
            break
        except:
            pass
        try:
            back_btn = driver.find_element(By.ID, 'btnSalir')
            driver.execute_script('arguments[0].click();', back_btn)
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)
        except:
            driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)

def segovia(driver, city_number):
    nie = input('Please input N.I.E : ')
    fullname = input('Please input Fullname : ')
    birth = input('Please input year of birth : ')
    nationality_number = input('Please input Nationality Number in Excel file : ')
    driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
    sleep(0.5)
    while True:
        region_menu = Find_Element(driver, By.CSS_SELECTOR, 'select[autocomplete="address-level1"]')
        region_items = region_menu.find_element(By.TAG_NAME, 'option')
        Select(region_menu).select_by_index(43)
        sleep(1)
        accept_btn1 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/citar?p=40&locale=es')
        sleep(0.5)
        police_menu = Find_Element(driver, By.NAME, 'tramiteGrupo[1]')
        police_items = police_menu.find_element(By.TAG_NAME, 'option')
        Select(police_menu).select_by_index(2)
        sleep(1)
        accept_btn2 = Find_Element(driver, By.ID, 'btnAceptar')
        driver.execute_script('arguments[0].click();', accept_btn2)
        sleep(1)

        # wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acInfo')
        enter_btn = Find_Element(driver, By.ID, 'btnEntrar')
        driver.execute_script('arguments[0].click();', enter_btn)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acEntrada')
        sleep(0.5)
        input_nie = Find_Element(driver, By.ID, 'txtIdCitado')
        Send_Keys(input_nie, nie)
        sleep(1)
        input_fullname = Find_Element(driver, By.ID, 'txtDesCitado')
        Send_Keys(input_fullname, fullname)
        sleep(1)
        input_birth = Find_Element(driver, By.ID, 'txtAnnoCitado')
        Send_Keys(input_birth, birth)
        sleep(1)
        nationality_menu = Find_Element(driver, By.ID, 'txtPaisNac')
        nationality_items = nationality_menu.find_element(By.TAG_NAME, 'option')
        Select(nationality_menu).select_by_index(nationality_number)
        sleep(1)
        next_btn1 = Find_Element(driver, By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn1)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acValidarEntrada')
        sleep(0.5)
        next_btn2 = driver.find_element(By.ID, 'btnEnviar')
        driver.execute_script('arguments[0].click();', next_btn2)
        sleep(1)

        wait_url(driver, 'https://icp.administracionelectronica.gob.es/icpplus/acCitar')
        sleep(0.5)
        try:
            sign_btn = driver.find_element(By.ID, 'btnSiguiente')
            driver.execute_script('arguments[0].click();', sign_btn)
            print('Success!')
            message_telegram.send_message(city_number)
            break
        except:
            pass
        try:
            back_btn = driver.find_element(By.ID, 'btnSalir')
            driver.execute_script('arguments[0].click();', back_btn)
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)
        except:
            driver.get('https://icp.administracionelectronica.gob.es/icpplus/index.html')
            driver.delete_all_cookies()
            print('Failed!')
            sleep(1)