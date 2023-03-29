from selenium import webdriver
from selenium.webdriver.common.by import By
from base_page import BasePage

class AgreementLocators:
    LOCATOR_AGREEMENT_HEADER = (By.XPATH, "/html/body/div[1]/h1")



class AgreementHelper(BasePage):
    def check_agreement_header(self):
        all_list = self.find_elements(AgreementLocators.LOCATOR_AGREEMENT_HEADER, time=3)
        return [x.text for x in all_list]
