from selenium import webdriver
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector("#num1")
#x1 = x.get_attribute("span")
y = browser.find_element_by_css_selector("#num2")
x = int (x.text)
y = int (y.text)
z = str (x+y)
print (z)
from selenium.webdriver.support.ui import Select
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(z)
#browser.find_element_by_tag_name("select").click()
#browser.find_element_by_xpath("//option[text()= '+z+']").click()
button = browser.find_element_by_css_selector("button.btn")
button.click()


