from selenium.webdriver.common.by import By

BASE_URL = "https://katalon-demo-cura.herokuapp.com/"
username = "John Doe"
password = "ThisIsNotAPassword"

class login:
    MAKE_APPOINTMENT = By.XPATH, "//a[@id='btn-make-appointment']"
    USERNAME = By.XPATH, "//input[@name='username']"
    PASSWORD = By.XPATH, "//input[@name='password']"
    LOGINBTN = By.XPATH, "//button[@id='btn-login']"
    LOGIN_FAILED_VALIDATION = By.XPATH, "//p[@class='lead text-danger']"

class appointment:
    FACILITY = By.XPATH, "//select[@name='facility']"
    READDMISSION = By.XPATH, "//input[@name='hospital_readmission']"
    MEDICAL_AID = By.XPATH, "//label[normalize-space()='Medicaid']"
    DATE = By.XPATH, "//input[@name='visit_date']"
    MONT_YEAR_HEADER = By.CSS_SELECTOR, "div[class='datepicker-days'] th[class='datepicker-switch']"
    YEAR_HEADER = By.CSS_SELECTOR, "div[class='datepicker-months'] th[class='datepicker-switch']"
    YEAR_2025 = By.XPATH, "//span[normalize-space()='2025']"
    MONTH = By.XPATH, "//span[@class='month' and text()='Dec']"
    DAY_25 = By.XPATH, "//td[@class='day' and text()='25']"
    COMMENT = By.XPATH, "//textarea[@name='comment']"
    BOOK_APPOINTMENT = By.XPATH, "//button[@id='btn-book-appointment']"

    TEXT_APPT_CONFIRMATION = By.XPATH, "//h2[normalize-space()='Appointment Confirmation']"
    FACILITY_LABEL = By.XPATH, "//p[@id='facility']"
    READMISSION_LABEL = By.XPATH, "//p[@id='hospital_readmission']"
    PROGRAM_LABEL =By.XPATH, "//p[@id='program']"
    DATE_LABEL = By.XPATH, "//p[@id='visit_date']"
    COMMENT_LABEL= By.XPATH, "//div[@class='col-xs-8']/p[@id='comment']"

    NONE_PROGRAMS = By.XPATH, "//input[@type='radio' and @value='None']"
class history:
    MENU_TOGGLE = By.XPATH, "//a[@id='menu-toggle']"

    #item in a menu
    HISTORY = By.XPATH, "//a[text()='History']"

    DATE_HISTORY = By.XPATH, "//div[@class='panel-heading'][1]"
    FACILITY_HISTORY = By.XPATH, "//p[@id='facility'][1]"
    READMISSIOM_HISTORY = By.XPATH, "//p[@id='hospital_readmission'][1]"
    MEDICA_AID_HISTORY = By.XPATH, "//p[@id='program'][1]"
    COMMENT_HISTORY = By.XPATH, "//p[@id='comment'][1]"

    GO_TO_HOMEPAGE = By.XPATH, "//a[@href='https://katalon-demo-cura.herokuapp.com/']"

    #2nd history appointment
    DATE_HISTORY_2 = By.XPATH, "//div[@class='panel-heading'][2]"
    FACILITY_HISTORY_2 = By.XPATH, "//p[@id='facility'][2]"
    READMISSIOM_HISTORY_2 = By.XPATH, "//p[@id='hospital_readmission'][2]"
    MEDICA_AID_HISTORY_2 = By.XPATH, "//p[@id='program'][2]"
    COMMENT_HISTORY_2 = By.XPATH, "//p[@id='comment'][2]"

class profile:
    PROFILE = By.XPATH, "//a[text()='Profile']"
    LOG_OUT_BTN = By.XPATH, "//a[@href='https://katalon-demo-cura.herokuapp.com/authenticate.php?logout']"