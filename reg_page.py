from selenium.webdriver.common.by import By
from base_page import BasePage

class RegLocators:
    LOCATOR_REGISTRATION = (By.XPATH, "//a[@id='kc-register']")
    LOCATOR_REG_FIELD_FNAME = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/div[1]/input[1]")
    LOCATOR_REG_FIELD_SNAME = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/div[1]/input[1]")
    LOCATOR_REG_FIELD_NUMAIL = (By.XPATH, "//input[@id='address']")
    LOCATOR_REG_FIELD_PASS = (By.XPATH, "//input[@id='password']")
    LOCATOR_REG_FIELD_CONFPASS = (By.XPATH, "//input[@id='password-confirm']")
    LOCATOR_REG_BUTTON = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/button[1]")
    LOCATOR_REG_FNAME_ERROR_LENGTH = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    LOCATOR_REG_FNAME_ERROR_LAT = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    LOCATOR_REG_FNAME_ERROR_SYM = (By.XPATH, "//span[contains(text(),'Необходимо заполнить поле кириллицей. От 2 до 30 с')]")
    LOCATOR_REG_SNAME_ERROR = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]")
    LOCATOR_REG_SNAME_ERROR_LENGTH = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]")
    LOCATOR_REG_SNAME_ERROR_LAT = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]")
    LOCATOR_REG_SNAME_ERROR_SYM = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]")
    LOCATOR_REG_NUMAIL_ERROR = (By.XPATH, "//span[contains(text(),'Введите телефон в формате +7ХХХХХХХХХХ или +375XXX')]")
    LOCATOR_REG_PASS_ERROR_SHORT = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]")
    LOCATOR_REG_PASS_ERROR_LEGTH = (By.XPATH, "//span[contains(text(),'Длина пароля должна быть не более 20 символов')]")
    LOCATOR_REG_PASS_ERROR_KIRRIL = (By.XPATH, "//span[contains(text(),'Пароль должен содержать только латинские буквы')]")
    LOCATOR_REG_CONFPASS_ERROR = (By.XPATH, "//body/div[@id='app']/main[@id='app-container']/section[@id='page-right']/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]")
    LOCATOR_REG_AGREEMENTS_LINK = (By.LINK_TEXT, "пользовательского соглашения")
    LOCATOR_REG_NOT_FREE_MAIL = (By.XPATH, "//h2[contains(text(),'Учётная запись уже существует')]")

class RegHelper(BasePage):
    def push_to_reg(self):
        return self.find_element(RegLocators.LOCATOR_REGISTRATION, time=3).click()

    def enter_fname(self, fname):
        fname_field = self.find_element(RegLocators.LOCATOR_REG_FIELD_FNAME)
        fname_field.send_keys(fname)
        return fname_field

    def enter_sname(self, sname):
        sname_field = self.find_element(RegLocators.LOCATOR_REG_FIELD_SNAME)
        sname_field.send_keys(sname)
        return sname_field

    def enter_mail(self, mail):
        mail_field = self.find_element(RegLocators.LOCATOR_REG_FIELD_NUMAIL)
        mail_field.send_keys(mail)
        return mail_field

    def enter_number(self, number):
        number_field = self.find_element(RegLocators.LOCATOR_REG_FIELD_NUMAIL)
        number_field.send_keys(number)
        return number_field

    def enter_pass(self, password):
        pass_field = self.find_element(RegLocators.LOCATOR_REG_FIELD_PASS)
        pass_field.send_keys(password)
        return pass_field

    def enter_confpass(self, confpassword):
        cpass_field = self.find_element(RegLocators.LOCATOR_REG_FIELD_CONFPASS)
        cpass_field.send_keys(confpassword)
        return cpass_field

    def click_on_button(self):
        return self.find_element(RegLocators.LOCATOR_REG_BUTTON, time=3).click()

    def check_fname_short(self):
        short_message = self.find_element(RegLocators.LOCATOR_REG_FNAME_ERROR_LENGTH)
        return short_message

    def check_fname_length(self):
        length_message = self.find_element(RegLocators.LOCATOR_REG_FNAME_ERROR_LENGTH)
        return length_message

    def check_fname_lat(self):
        lat_message = self.find_element(RegLocators.LOCATOR_REG_FNAME_ERROR_LAT)
        return lat_message
    def check_fname_sym(self):
        sym_message = self.find_element(RegLocators.LOCATOR_REG_FNAME_ERROR_SYM)
        return sym_message
    def check_sname_short(self):
        short_message = self.find_element(RegLocators.LOCATOR_REG_SNAME_ERROR_LENGTH)
        return short_message
    def check_sname_length(self):
        length_message = self.find_element(RegLocators.LOCATOR_REG_SNAME_ERROR_LENGTH)
        return length_message
    def check_sname_lat(self):
        lat_message = self. find_element(RegLocators.LOCATOR_REG_SNAME_ERROR_LAT)
        return lat_message
    def check_sname_sym(self):
        sym_message = self.find_element(RegLocators.LOCATOR_REG_SNAME_ERROR_SYM)
        return sym_message
    def into_agreements_reg(self):
        try:
            self.driver.get("https://b2c.passport.rt.ru/")
            self.find_element(RegLocators.LOCATOR_REG_AGREEMENTS_LINK, time=3).click()
            self.driver.switch_to.window(self.driver.window_handles[1])
        except Exception as ex:
            print(ex)

    def check_free_mail(self):
        free_message = self.find_element(RegLocators.LOCATOR_REG_NOT_FREE_MAIL)
        return free_message