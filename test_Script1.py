from selenium import webdriver

def test_setup():
    global driver
    driver = webdriver.Chrome(executable_path="C:/Users/rl/PycharmProjects/Agathiyan/Resources/chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.find_element_by_id("txtUsername").send_keys("Admin")
    driver.find_element_by_id("txtPassword").send_keys("admin123")
    driver.find_element_by_id("btnLogin").click()

def test_teardown():
    driver.close()
    driver.quit()
    print("test completed")