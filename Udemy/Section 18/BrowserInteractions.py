"""
Section 18: Working with Web Elements
"""
from selenium import webdriver


class BrowserInteractions:

    def open(self):
        base_url = "https://letskodeit.teachable.com/p/practice"
        driver = webdriver.Chrome()

        # Window Maximize
        driver.maximize_window()

        # Open the URL
        driver.get(base_url)

        # Get Title
        title = driver.title
        print("The title of the current web page is: " + title)

        # Get Current URL
        current_url = driver.current_url
        print("Current URL: " + str(current_url))

        # Browser Refresh
        driver.refresh()
        print("Browser refreshed 1st time")

        driver.get(driver.current_url)
        print("Browser refreshed 2nd time")

        # Open another URL
        driver.get("https://learn.letskodeit.com/sign_in")
        current_url = driver.current_url
        print("Current URL: " + str(current_url))

        # Browser Back
        driver.back()
        print("Go backwards in browser")
        current_url = driver.current_url
        print("Current URL: " + str(current_url))

        # Browser Forward
        driver.forward()
        print("Go forwards in browser")
        current_url = driver.current_url
        print("Current URL: " + str(current_url))

        # Get Page Source
        page_source = driver.page_source
        print("#*" * 20)
        print(page_source)
        # Browser Close / Quit
        driver.quit()


gc = BrowserInteractions()
gc.open()
