from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

url = 'http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html'
driver = webdriver.Firefox()
driver.maximize_window()
driver.get(url)
source_list = ['//*[@id="box3"]', '//*[@id="box5"]', '//*[@id="box1"]',
               '//*[@id="box2"]', '//*[@id="box4"]', '//*[@id="box6"]', '//*[@id="box7"]']
destination_list = ['//*[@id="box103"]', '//*[@id="box105"]', '//*[@id="box101"]',
                    '//*[@id="box102"]', '//*[@id="box104"]', '//*[@id="box106"]', '//*[@id="box107"]']

for i in range(len(source_list)):
    source = driver.find_element_by_xpath(source_list[i])
    destination = driver.find_element_by_xpath(destination_list[i])
    actions = ActionChains(driver)
    actions.drag_and_drop(source, destination).perform()
