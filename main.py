from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import city

options = Options()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.217 Safari/537.3")
options.add_experimental_option("debuggerAddress", "127.0.0.1:9030")
service = Service(executable_path = "C:\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(options = options)

city_number = input('Please select city number.' + '\n' + '1. Madrid' + '\n' + '2. Cáceres' + '\n' + '3. Albacete' + '\n' + '4. Valladolid' + '\n' + '5. Segovia' + '\n')

if city_number == '1':
    city.madrid(driver, city_number)
if city_number == '2':
    city.caceres(driver, city_number)
if city_number == '3':
    city.albacete(driver, city_number)
if city_number == '4':
    city.valladolid(driver, city_number)
if city_number == '5':
    city.segovia(driver, city_number)
