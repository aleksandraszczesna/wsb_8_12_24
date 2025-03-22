#instalacja selenium - można z konsoli pip install selenium

from selenium import webdriver  #importowanie webdrivera
import time #import biblioteki time do użycia sleep

driver = webdriver.Chrome()  #inicjalizacja przeglądarki chrome

url = "https://www.google.com"
new_url = "https://www.wp.pl"

#pobranie konkretnego adresu strony w przeglądarce
driver.get(url)

#rozmiar okna przeglądarki
driver.maximize_window()
#driver.set_window_size(1000,500)   - zdefiniować na stałe rozmiar okna, a nie maksymalizować

#otwarcie drugiej zakładki
driver.execute_script("window.open('');")

#przełączanie do nowego okna
driver.switch_to.window(driver.window_handles[1])
driver.get(new_url)
driver.close()  #do zamykania tylko zakładki

#zatrzymanie skryptu
time.sleep(15)

#zamykanie przeglądarki
driver.quit()   #zamyka całą przeglądarkę