from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

BASE_URL = "https://loto.mk/Results"
YEARS = [2022, 2023, 2024, 2025]
MAX_KOLO = 104

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

for year in YEARS:
    print("\n" + "=" * 50)
    print(f" Година {year}")

    for kolo in range(1, MAX_KOLO + 1):
        url = f"{BASE_URL}?drawNo={kolo}&gameNo=6&drawYear={year}"
        driver.get(url)

        time.sleep(2.5)

        nums = driver.find_elements(By.CLASS_NAME, "Rez_Brojevi_Txt_Gray")
        numbers = [int(n.text) for n in nums if n.text.isdigit()][:7]

        if len(numbers) == 7:
            print(f"Коло {kolo:3d} → {numbers}")
        else:
            print(f"Коло {kolo:3d} → нема податок")

        time.sleep(1.5)

driver.quit()
