
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import Select

driver = webdriver.Firefox()


driver.get("http://vtop2.vitap.ac.in:8070/onlineexam/processStudentLogin")


username = driver.find_element_by_id("applnum");
username.send_keys("2018019866");


select1 = Select(driver.find_element_by_name("bdd"))
select1.select_by_visible_text("22")

select2 = Select(driver.find_element_by_name("bmm"))
select2.select_by_visible_text("03 (MAR)")

select = Select(driver.find_element_by_name("byyyy"))
select.select_by_visible_text("2000")


button = driver.find_element_by_class_name("btn")
button.click()
