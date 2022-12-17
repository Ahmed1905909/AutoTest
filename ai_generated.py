from selenium import webdriver
def ai_gen_script(driver):
    driver=webdriver.chrome()
    driver.get("amazon.com")
    driver.find_element_by_id("cart-view").click()


