from selenium.webdriver.common.by import By

BASE_URL = "https://katalon-demo-cura.herokuapp.com/"
username = "John Doe"
password = "ThisIsNotAPassword"

class login:
    MAKE_APPOINTMENT = By.XPATH, "//a[@id='btn-make-appointment']"
    USERNAME = By.XPATH, "//input[@name='username']"
    PASSWORD = By.XPATH, "//input[@name='password']"
    LOGINBTN = By.XPATH, "//button[@id='btn-login']"


class appointment:
    FACILITY = By.XPATH, "//select[@name='facility']"
    READDMISSION = By.XPATH, "//input[@name='hospital_readmission']"
    MEDICAL_AID = By.XPATH, "//label[normalize-space()='Medicaid']"
    DATE = By.XPATH, "//input[@name='visit_date']"
    MONT_YEAR_HEADER = By.CSS_SELECTOR, "div[class='datepicker-days'] th[class='datepicker-switch']"
    YEAR_HEADER = By.CSS_SELECTOR, "div[class='datepicker-months'] th[class='datepicker-switch']"
    YEAR_2025 = By.XPATH, "//span[normalize-space()='2025']"
    MONTH_FOCUSED = By.CSS_SELECTOR, ".month.focused"
    DAY_25 = By.XPATH, "//td[normalize-space()='25']"
    COMMENT = By.XPATH, "//textarea[@name='comment']"
    BOOK_APPOINTMENT = By.XPATH, "//button[@id='btn-book-appointment']"