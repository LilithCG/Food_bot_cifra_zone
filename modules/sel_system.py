from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def launch(links: [], phone, fio,street, house, comment):
    s = Service('modules\cdriver\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(0.5)
    phone = phone[1:len(phone)]
    for link in links:
        driver.get(link)
    element = driver.find_element(By.NAME, 'order')
    driver.execute_script("arguments[0].click();", element)

    # Курьер
    element = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div/div/form/div[1]/ul/li[2]/label')
    driver.execute_script("arguments[0].click();", element)

    # Картой при получении
    element = driver.find_element(By.XPATH, '/html/body/main/div/div/div[1]/div/div/form/div[3]/ul/li[1]/label')
    driver.execute_script("arguments[0].click();", element)

    # phone
    element = driver.find_element(By.NAME, 'phone')
    element.send_keys(phone)

    # fio
    element = driver.find_element(By.NAME, 'fio')
    element.send_keys(fio)

    # street
    element = driver.find_element(By.NAME, 'address_street')
    element.send_keys(street)

    # house
    element = driver.find_element(By.NAME, 'address_house')
    element.send_keys(house)

    # comment
    element = driver.find_element(By.NAME, 'info')
    element.send_keys(comment)

    # END Send order
    # element = driver.find_element(By.NAME, 'toOrder')
    # driver.execute_script("arguments[0].click();", element)
    driver.quit()
