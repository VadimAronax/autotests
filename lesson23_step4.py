from selenium import webdriver
import math
import time
import os
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element_by_css_selector("#input_value")
    x = int (x_element.text)
    input1 = browser.find_element_by_css_selector("#answer")
    input1.send_keys(calc(x))

    
   
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
   
    

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

