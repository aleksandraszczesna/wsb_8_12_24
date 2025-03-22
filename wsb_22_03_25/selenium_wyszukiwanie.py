from selenium import webdriver  #importowanie webdrivera
import time #import biblioteki time do użycia sleep
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()  #inicjalizacja przeglądarki chrome

url = "https://www.google.com"

#pobranie konkretnego adresu strony w przeglądarce
driver.get(url)

#rozmiar okna przeglądarki
driver.maximize_window()

#lokalizacja przycisku, żeby zaakceptować zgody
accept_cookies = driver.find_element("id", "L2AGLb")
accept_cookies.click()

#wprowadzenie hasła do wyszukiwania i szukania
search_text = driver.find_element("name", "q")
search_text.send_keys("Pogoda")
#search_text.send_keys(Keys.ENTER)   #kliknięcie enter na klawiaturze
search_text.submit()

#zatrzymanie skryptu
time.sleep(100)

#zamykanie przeglądarki
driver.quit()   #zamyka całą przeglądarkę
