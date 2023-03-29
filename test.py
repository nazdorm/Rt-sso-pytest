#python3 -m pytest -v test.py
from auth_page import AuthHelper
from lk_page import LkHelper
from reg_page import RegHelper
from agreement_page import AgreementHelper
from settings import VALID_LOGIN
from settings import VALID_PASS
from settings import VALID_NUMBER
from settings import VALID_EMAIL
from settings import INVALID_LOGIN
from settings import INVALID_EMAIL
from settings import INVALID_NUMBER
from settings import INVALID_PASS
import time


#1[Авторизация] Авторизация по логину
def test_auth_login_p(browser):
    auth_login = AuthHelper(browser)
    auth_check_bar = LkHelper(browser)
    auth_login.go_to_site()
    auth_login.enter_login(VALID_LOGIN)
    auth_login.enter_password(VALID_PASS)
    auth_login.click_on_auth_button()
    element = auth_check_bar.check_lk_bar()

    assert "Выйти" in element

#2[Авторизация] Авторизация по номеру телефона
def test_auth_number_p(browser):
    auth_number = AuthHelper(browser)
    auth_check_bar = LkHelper(browser)
    auth_number.go_to_site()
    auth_number.enter_number(VALID_NUMBER)
    auth_number.enter_password(VALID_PASS)
    auth_number.click_on_auth_button()
    element = auth_check_bar.check_lk_bar()

    assert "Выйти" in element

#3[Авторизация] Авторизация по почте
def test_auth_mail_p(browser):
    auth_mail = AuthHelper(browser)
    auth_check_bar = LkHelper(browser)
    auth_mail.go_to_site()
    auth_mail.enter_mail(VALID_EMAIL)
    auth_mail.enter_password(VALID_PASS)
    auth_mail.click_on_auth_button()
    element = auth_check_bar.check_lk_bar()

    assert "Выйти" in element

#4[Авторизация] Выход из учетной записи
def test_auth_out(browser):
    auth_login = AuthHelper(browser)
    auth_check_bar = LkHelper(browser)
    auth_login.go_to_site()
    auth_login.enter_login(VALID_LOGIN)
    auth_login.enter_password(VALID_PASS)
    auth_login.click_on_auth_button()
    element = auth_check_bar.check_lk_bar()
    assert "Выйти" in element
    auth_login.out_button()
    out = auth_login.check_out()
    assert "Авторизация" in out


#5[Авторизация] Авторизация c неверным логином отображает ошибку
def test_auth_login_n(browser):
    auth_login_n = AuthHelper(browser)
    auth_check = AuthHelper(browser)
    auth_login_n.go_to_site()
    auth_login_n.enter_login(INVALID_LOGIN)
    auth_login_n.enter_password(VALID_PASS)
    auth_login_n.click_on_auth_button()
    message = auth_check.check_error()

    assert message.text == "Неверный логин или пароль"

#6[Авторизация] Авторизация с неверным номером телефона отображает ошибку
def test_auth_number_n(browser):
    auth_number_n = AuthHelper(browser)
    auth_check = AuthHelper(browser)
    auth_number_n.go_to_site()
    auth_number_n.enter_number(INVALID_NUMBER)
    auth_number_n.enter_password(VALID_PASS)
    auth_number_n.click_on_auth_button()
    message = auth_check.check_error()

    assert message.text == "Неверный логин или пароль"

#7[Авторизация] Авторизация с неверной почтой отображает ошибку
def test_auth_mail_n(browser):
    auth_mail_n = AuthHelper(browser)
    auth_check = AuthHelper(browser)
    auth_mail_n.go_to_site()
    auth_mail_n.enter_mail(INVALID_EMAIL)
    auth_mail_n.enter_password(VALID_PASS)
    auth_mail_n.click_on_auth_button()
    message = auth_check.check_error()

    assert message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки" #Не удаётся обойти капчу

#8[Авторизация] Авторизация с неверным паролем отображает ошибку
def test_auth_pass_n(browser):
    auth_pass_n = AuthHelper(browser)
    auth_check = AuthHelper(browser)
    auth_pass_n.go_to_site()
    auth_pass_n.enter_mail(VALID_EMAIL)
    auth_pass_n.enter_password(INVALID_PASS)
    auth_pass_n.click_on_auth_button()
    message = auth_check.check_error()

    assert message.text == "Неверный логин или пароль" or "Неверно введен текст с картинки" #Не удаётся обойти капчу

#9[Авторизация] Переход по ссылке к пользовательскому соглашению
def test_auth_into_lic(browser):
    into_agree = AuthHelper(browser)
    agree_check = AgreementHelper(browser)
    into_agree.go_to_site()
    into_agree.into_agreements()
    header = agree_check.check_agreement_header()

    assert 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»' in list(header)

#10[Регистрация] Валидация поля "Имя" на длину короче 2х символов
def test_reg_short_fname(browser):
    reg_short_fname = RegHelper(browser)
    reg_short_fname.go_to_site()
    reg_short_fname.push_to_reg()
    reg_short_fname.enter_fname("ы")
    reg_short_fname.click_on_button()
    message = reg_short_fname.check_fname_short()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#11[Регистрация] Валидация поля "Имя" на длину более 30 символов
def test_reg_length_fname(browser):
    reg_length_fname = RegHelper(browser)
    reg_length_fname.go_to_site()
    reg_length_fname.push_to_reg()
    reg_length_fname.enter_fname("ффффффффффффффффффффффффффффффф")
    reg_length_fname.click_on_button()
    message = reg_length_fname.check_fname_length()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#12[Регистрация] Валидация поля "Имя" на ввод латиницы
def test_reg_lat_fname(browser):
    reg_lat_fname = RegHelper(browser)
    reg_lat_fname.go_to_site()
    reg_lat_fname.push_to_reg()
    reg_lat_fname.enter_fname("ssss")
    reg_lat_fname.click_on_button()
    message = reg_lat_fname.check_fname_lat()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#13[Регистрация] Валидация поля "Имя" на ввод спец.символов
def test_reg_sym_fname(browser):
    reg_sym_fname = RegHelper(browser)
    reg_sym_fname.go_to_site()
    reg_sym_fname.push_to_reg()
    reg_sym_fname.enter_fname("!!!!")
    reg_sym_fname.click_on_button()
    message = reg_sym_fname.check_fname_sym()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#14[Регистрация] Валидация поля "Фамилия" на длину короче 2х символов
def test_reg_short_sname(browser):
    reg_short_sname = RegHelper(browser)
    reg_short_sname.go_to_site()
    reg_short_sname.push_to_reg()
    reg_short_sname.enter_sname("ы")
    reg_short_sname.click_on_button()
    message = reg_short_sname.check_sname_short()

    assert message. text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#15[Регистрация] Валидация поля "Фамилия" на длину более 30 символов
def test_reg_legth_sname(browser):
    reg_length_sname = RegHelper(browser)
    reg_length_sname.go_to_site()
    reg_length_sname.push_to_reg()
    reg_length_sname.enter_sname("ффффффффффффффффффффффффффффффф")
    reg_length_sname.click_on_button()
    message = reg_length_sname.check_sname_length()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#16[Регистрация] Валидация поля "Фамилия" на ввод латинницы
def test_reg_lat_sname(browser):
    reg_lat_sname = RegHelper(browser)
    reg_lat_sname.go_to_site()
    reg_lat_sname.push_to_reg()
    reg_lat_sname.enter_sname("ssss")
    reg_lat_sname.click_on_button()
    message = reg_lat_sname.check_sname_lat()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#17[Регистрация] Валидация поля "Фамилия" на ввод спецсимволов
def test_reg_sym_sname(browser):
    reg_sym_sname = RegHelper(browser)
    reg_sym_sname.go_to_site()
    reg_sym_sname.push_to_reg()
    reg_sym_sname.enter_sname("!!!!")
    reg_sym_sname.click_on_button()
    message = reg_sym_sname.check_sname_sym()

    assert message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."

#18[Регистрация] Переход к пользовательскому соглашению
def test_auth_into_lic(browser):
    reg_into_agree = RegHelper(browser)
    agree_check = AgreementHelper(browser)
    reg_into_agree.go_to_site()
    reg_into_agree.push_to_reg()
    reg_into_agree.into_agreements_reg()
    header = agree_check.check_agreement_header()

    assert 'Публичная оферта о заключении Пользовательского соглашения на использование Сервиса «Ростелеком ID»' in list(header)

#19[Регистрация] Регистрация с занятой почтой
def test_reg_free_mail(browser):
    reg_mail = RegHelper(browser)
    reg_mail.go_to_site()
    reg_mail.push_to_reg()
    reg_mail.enter_fname("аааа")
    reg_mail.enter_sname("бббб")
    reg_mail.enter_mail(VALID_EMAIL)
    reg_mail.enter_pass(VALID_PASS)
    reg_mail.enter_confpass(VALID_PASS)
    reg_mail.click_on_button()
    alert = reg_mail.check_free_mail()

    assert alert.text == "Учётная запись уже существует"

#20[регистрация] Регистрация с занятым телефоном
def test_reg_free_number(browser):
    reg_number = RegHelper(browser)
    reg_number.go_to_site()
    reg_number.push_to_reg()
    reg_number.enter_fname("аааа")
    reg_number.enter_sname("бббб")
    reg_number.enter_mail(VALID_NUMBER)
    reg_number.enter_pass(VALID_PASS)
    reg_number.enter_confpass(VALID_PASS)
    reg_number.click_on_button()
    alert = reg_number.check_free_mail()

    assert alert.text == "Учётная запись уже существует"

#Не удалось извлечь актуальное имя пользователя
"""#19[Личный кабинет] Проверка сохранения изменений Имени
def test_change_fname(browser):
    lk_auth = AuthHelper(browser)
    lk_fname = LkHelper(browser)
    lk_fname.go_to_site()
    lk_auth.enter_number(VALID_NUMBER)
    lk_auth.enter_password(VALID_PASS)
    lk_auth.click_on_auth_button()
    fname = lk_fname.check_lk_fname()
    print(fname)"""

