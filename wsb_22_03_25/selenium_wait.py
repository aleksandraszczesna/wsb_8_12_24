from selenium import webdriver  #importowanie webdrivera
import time #import biblioteki time do użycia sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()  #inicjalizacja przeglądarki chrome

#implicity wait - oczekiwanie na pojawienie się każdego elementu na stronie przez maksymalnie x sek
#driver.implicitly_wait(15)

url1 = "https://www.w3schools.com/"

#pobranie konkretnego adresu strony w przeglądarce
driver.get(url1)

#rozmiar okna przeglądarki
driver.maximize_window()

#lokalizacja przycisku, żeby zaakceptować zgody
time.sleep(5)
accept_cookies1 = driver.find_element("id", "accept-choices")
accept_cookies1.click()

#tutorials
menu = driver.find_element("id", "navbtn_tutorials")
#menu.click()
webdriver.ActionChains(driver).move_to_element(menu).click().perform()

#learn HTML
learnHTML = driver.find_element('xpath',  '//a[@title="HTML Tutorial"]')
learnHTML.click()

#explicitly wait - czekamy na konkretny element
wait = WebDriverWait(driver, 15, 0.5)
#warunek oczekiwania
#wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))
wait.until(lambda x: len(x.find_elements('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')))

#input types
menuInput = driver.find_element('xpath', '//*[@id="leftmenuinnerinner"]/a[43]')
menuInput.click()

#zatrzymanie skryptu
time.sleep(100)

#zamykanie przeglądarki
driver.quit()   #zamyka całą przeglądarkę
