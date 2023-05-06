from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class Poe:
    def __init__(self):
        s = Service('chromedriver_mac64/chromedriver')
        self.driver = webdriver.Chrome(service=s)
        self.driver.get("https://poe.com/ChatGPT")
        time.sleep(2)
    # def scrape(self,mess):
    #         get_box1 = driver.find_element_by_css_selector("[data-replicated-value]")
    #         get_box2 = get_box.get_attribute("data-replicated-value")

    #         new_value = "new value"
    #         driver.execute_script("arguments[0].setAttribute('data-replicated-value', arguments[1]);", element, new_value)
    #         updated_value = element.get_attribute("data-replicated-value")
    #         assert updated_value == new_value, f"Expected value: {new_value}, Actual value: {updated_value}"
            
            
    #         button = self.driver.find_element_by_class_name('Button_buttonBase__0QP_m Button_primary__pIDjn ChatMessageInputView_sendButton__reEpT')
    #         button.click()
    #         time.sleep(2.5)
    #         button.click()
    #         time.sleep(1.5)