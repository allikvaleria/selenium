from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

try:
    driver.maximize_window()
    print("Brauser avatud ja maksimeeritud")

    driver.get("https://www.google.com")
    print("Google.com avatud")

    # Küpsiste aktsepteerimine
    try:
        noustu_nupp = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[div[text()='Nõustun kõigega']]"))
        )
        noustu_nupp.click()
    except:
        pass

    otsing_kast = driver.find_element(By.NAME, "q")
    otsing_kast.send_keys("Python Selenium automatiseerimine")
    
    # Otsingukasti tühjendamine
    otsing_kast.send_keys(Keys.CONTROL + "a")
    otsing_kast.send_keys(Keys.BACKSPACE)
    
    otsing_kast.send_keys("Kassid armsad fotod")
    otsing_kast.send_keys(Keys.RETURN)
    print("Otsing käivitatud")

    # Mineme piltide sektsiooni
    pildid_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Pildid']"))
    )
    pildid_link.click()

    # Avame esimese pildi
    esimene_pilt = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='islrc']//img[1]"))
    )
    esimene_pilt.click()

    time.sleep(2)
    driver.back()

    # Mineme videote sektsiooni
    video_link = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Videod']"))
    )
    video_link.click()

    # Tagasi avalehele
    logo = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//a[@title='Google avalehele']"))
    )
    logo.click()

    # Kasutame "Veab" nuppu
    veab_nupp = driver.find_element(By.NAME, "btnI")
    veab_nupp.click()
    print("Veab nuppu kasutatud")

    time.sleep(3)
    driver.back()

    # Avame ja sulgeme rakenduste menüü
    rakendused_nupp = driver.find_element(By.XPATH, "//a[@aria-label='Google rakendused']")
    rakendused_nupp.click()
    logo = driver.find_element(By.XPATH, "//img[@alt='Google']")
    logo.click()

    print("Kõik tegevused edukalt tehtud!")

finally:
    driver.quit()
    print("Brauser suletud")
