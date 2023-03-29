from selenium.webdriver.common.by import By
from base_page import BasePage

class LkPageLocators:
    LOCATOR_LK_BAR = (By.XPATH, "//header/div[1]/div[2]/div[1]")
    LOCATOR_LK_LOGOUT = (By.XPATH, "//div[@id='logout-btn']")
    LOCATOR_LK_FNAME = (By.XPATH, "//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]")
    LOCATOR_LK_SNAME = (By.XPATH,"//body/div[@id='app']/main[1]/div[1]/div[2]/div[1]/div[1]/div[1]/h2[1]/span[2]")

class LkHelper(BasePage):
    def check_lk_bar(self):
        all_list = self.find_elements(LkPageLocators.LOCATOR_LK_LOGOUT)
        return [x.text for x in all_list]
    def check_lk_fname(self):
        name = self.find_elements(LkPageLocators.LOCATOR_LK_FNAME, time=5)
        return [x.text for x in name]
