from selenium import webdriver


class LoginTests:

    def test_valid_login(self):
        base_url = "https://letskodeit.teachable.com/"

        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(base_url)

        login_link = driver.find_element_by_link_text("Login")
        login_link.click()

        email_field = driver.find_element_by_id("user_email")
        email_field.send_keys("test@email.com")

        password_field = driver.find_element_by_id("user_password")
        password_field.send_keys("abcabc")

        login_btn = driver.find_element_by_name("commit")
        login_btn.click()

        user_icon = driver.find_element_by_xpath(".//*[@id='navbar']//span[text()='Test User']")
        if user_icon is not None:
            print("Login successful.")
        else:
            print("Login failed")


c = LoginTests()
c.test_valid_login()
