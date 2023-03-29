from selenium.webdriver.common.by import By
from base_page import BasePage

class AuthLocators:
    LOCATOR_AUTH_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_AUTH_TAB_MAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_AUTH_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_AUTH_LOGIN_FIELD = (By.ID, "username")
    LOCATOR_AUTH_PASS_FIELD = (By.ID, "password")
    LOCATOR_AUTH_BUTTON = (By.ID, "kc-login")
    LOCATOR_AUTH_ERROR = (By.ID, "form-error-message")
    LOCATOR_AGREEMENTS_LINK = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/a[1]")
    LOCATOR_AUTH_OUT_BUTTON = (By.XPATH, "//div[@id='logout-btn']")
    LOCATOR_AUTH_OUT_RES = (By.XPATH, "//h1[contains(text(),'Авторизация')]")

class AuthHelper(BasePage):
    def enter_login(self, login):
        tab_login = self.find_element(AuthLocators.LOCATOR_AUTH_TAB_LOGIN)
        tab_login.click()
        login_field = self.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_FIELD)
        login_field.send_keys(login)
        return login_field

    def enter_number(self, number):
        tab_number = self.find_element(AuthLocators.LOCATOR_AUTH_TAB_PHONE)
        tab_number.click()
        number_field = self.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_FIELD)
        number_field.send_keys(number)
        return number_field

    def enter_mail(self, mail):
        tab_mail = self.find_element(AuthLocators.LOCATOR_AUTH_TAB_MAIL)
        tab_mail.click()
        mail_field = self.find_element(AuthLocators.LOCATOR_AUTH_LOGIN_FIELD)
        mail_field.send_keys(mail)
        return mail_field


    def enter_password(self, password):
        password_field = self.find_element(AuthLocators.LOCATOR_AUTH_PASS_FIELD)
        password_field.send_keys(password)
        return password_field

    def click_on_auth_button(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_BUTTON, time=3).click()

    def check_error(self):
        message = self.find_element(AuthLocators.LOCATOR_AUTH_ERROR, time=3)
        return message

    def into_agreements(self):
        try:
            self.driver.get("https://b2c.passport.rt.ru/")
            self.find_element(AuthLocators.LOCATOR_AGREEMENTS_LINK, time=3).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as ex:
            print(ex)

    def out_button(self):
        return self.find_element(AuthLocators.LOCATOR_AUTH_OUT_BUTTON, time=3).click()
    def check_out(self):
        res = self.find_elements(AuthLocators.LOCATOR_AUTH_OUT_RES)
        return [x.text for x in res]


