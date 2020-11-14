import threading
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = "C:\chromedriver.exe"

def runTest():
  chrome_options = Options()
  chrome_options.add_argument("--headless")
  driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
  driver.get("http://localhost/Proyecto_OpenPay0/")
  driver.maximize_window()

  name_field = driver.find_element_by_id("name-field")
  name_field.send_keys("alan morales")

  card_field = driver.find_element_by_id("card-field")
  card_field.send_keys("4242424242424242")

  expiration_month_field = driver.find_element_by_id("expitarion-month-field")
  expiration_month_field.send_keys("12")

  expiration_year_field = driver.find_element_by_id("expiration-year-field")
  expiration_year_field.send_keys("21")

  cvv_field = driver.find_element_by_id("cvv-field")
  cvv_field.send_keys("123")

  send_button = driver.find_element_by_id("btn-enviar")
  send_button.click()

  # waits until the success/error pages loads.
  driver.implicitly_wait(30)
  transaction_status_element = driver.find_element_by_id("transaction-status")
  print(transaction_status_element.get_attribute("class"))


number_of_tests = 4

for i in range(number_of_tests):
  test_thread = threading.Thread(target=runTest)
  test_thread.start()

