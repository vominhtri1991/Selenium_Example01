from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options=Options()
options.add_argument("--ignore-certificate-errors")
options.add_argument("--incognito")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.name.com/account/login")

element=driver.find_element_by_link_text("CREATE NEW ACCOUNT")
element.click()
time.sleep(1)
#driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

element=driver.find_element_by_name("username")
element.send_keys("tto1991")

element=driver.find_element_by_name("password")
element.send_keys("123456789")

element=driver.find_element_by_xpath("//div[@class='checkbox form-tos control-group']/*/input")
print(element.tag_name)
time.sleep(1)
driver.execute_script("arguments[0].click();", element)

time.sleep(1)
select_country=driver.find_element_by_name("new-contact-country")
all_options=select_country.find_elements_by_tag_name("option")
for option in all_options:
	if(option.get_attribute("value")=="VN"):
		print(option.tag_name)
		option.click()
		
time.sleep(2)