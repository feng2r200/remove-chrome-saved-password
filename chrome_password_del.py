#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import os

options = Options()
options.add_experimental_option('debuggerAddress', '127.0.0.1:9222')

path_webdriver = os.popen('which chromedriver').readlines()[0].rstrip()
driver = webdriver.Chrome(executable_path=path_webdriver, options=options)

def expand_shadow_element(element):
    return driver.execute_script('return arguments[0].shadowRoot', element)

driver.get('chrome://settings/passwords')

root1 = expand_shadow_element(driver.find_element_by_css_selector("body > settings-ui"))
root2 = expand_shadow_element(root1.find_element_by_css_selector("#main"))
root3 = expand_shadow_element(root2.find_element_by_css_selector("settings-basic-page"))
root4 = expand_shadow_element(root3.find_element_by_css_selector("#basicPage > settings-section.expanded > settings-autofill-page"))

root5 = expand_shadow_element(root4.find_element_by_css_selector("#pages > settings-subpage"))
root6 = expand_shadow_element(root5.find_element_by_css_selector("#headerLine > cr-search-field"))
root7 = expand_shadow_element(root6.find_element_by_css_selector("#searchInput"))

input_text = root7.find_element_by_css_selector("#input")
input_text.send_keys('root') # 该处内容填写指定需要删除密码的用户名

root_password = expand_shadow_element(root4.find_element_by_css_selector('#passwordSection'))
while True:
    try:
        item = root_password.find_element_by_css_selector('#passwordList > password-list-item:nth-child(2)')
    except:
        break
    item_password = expand_shadow_element(item).find_element_by_id('passwordMenu')
    item_password.click()
    btn_remove = root_password.find_element_by_css_selector('#menuRemovePassword')
    btn_remove.click()
