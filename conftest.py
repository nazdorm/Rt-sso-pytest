import pytest
from selenium import webdriver

@pytest.fixture(autouse=True)
def browser():
    driver = webdriver.Chrome(executable_path="./chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

