from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3)
print(driver.find_element_by_id('content').text)
driver.close()

'''
driver.find_element_by_css_selector("#content")
driver.find_element_by_name("div")

driver.find_elements_by_css_selector("#content")
driver.find_elements_by_name("div")

pageSource = driver.page_source
bsObj = BeautifulSoup(pageSource)
print(bsObj.find(id="content").get_text())
'''

