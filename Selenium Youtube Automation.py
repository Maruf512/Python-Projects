from selenium import webdriver

a = input("What do you want to search: ")

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)


driver.get("https://www.youtube.com/")
driver.find_element_by_name("search_query").send_keys(a)
driver.find_element_by_id("search-icon-legacy").click()
driver.find_element_by_id("dismissable").click()
driver.maximize_window()
#driver.fullscreen_window()