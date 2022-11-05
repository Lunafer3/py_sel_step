from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        wd.get("http://suninjuly.github.io/simple_form_find_task.html")
        wd.find_element_by_name("first_name").click()
        wd.find_element_by_name("first_name").clear()
        wd.find_element_by_name("first_name").send_keys("Иван")
        wd.find_element_by_name("last_name").click()
        wd.find_element_by_name("last_name").clear()
        wd.find_element_by_name("last_name").send_keys("Иванов")
        wd.find_element_by_xpath("/html/body/div[1]/form/div[3]/input").click()
        wd.find_element_by_xpath("/html/body/div[1]/form/div[3]/input").clear()
        wd.find_element_by_xpath("/html/body/div[1]/form/div[3]/input").send_keys("Иван")
        wd.find_element_by_id("country").click()
        wd.find_element_by_id("country").clear()
        wd.find_element_by_id("country").send_keys("Иван")
        wd.find_element_by_id("submit_button").click()
        time.sleep(30)
        

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()