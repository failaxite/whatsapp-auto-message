from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from urllib.parse import quote
import os

def load_language_config(language):
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)
        return config_data.get(language, {})

def load_translation(language):
    try:
        with open(f"translations/{language}.json", "r") as translation_file:
            return json.load(translation_file)
    except FileNotFoundError:
        return {}

def set_language():
    with open("config.json", "r") as config_file:
        config_data = json.load(config_file)
        return config_data.get("language", "en_US")

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")

os.system("")
os.environ["WDM_LOG_LEVEL"] = "0"

class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print("**********************************************************")
print("**********************************************************")
print("*****                                               ******")
print(f"***** {translations.get('welcome_message')} ******")
print(f"***** {translations.get('github_link')} ******")
print("*****                                               ******")
print("**********************************************************")
print("**********************************************************")
print(style.RESET)

f = open("msg.txt", "r", encoding="utf8")
message = f.read()
f.close()

print(style.YELLOW + '\n' + message_display)
print(style.GREEN + message)
print("\n" + style.RESET)
message = quote(message)

numbers = []
f = open("phones.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()
total_number=len(numbers)
print(style.RED + translations.get('found_numbers', 'We found {total_number} numbers in the file').format(total_number=total_number) + style.RESET)
delay = 30

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
input(style.MAGENTA + whatsapp_web_login_prompt + style.RESET)
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + sending_message.format(current=(idx+1), total=total_number, number=number) + style.RESET)
	try:
		url = 'https://web.whatsapp.com/send?phone=' + number + '&text=' + message
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					send_button = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, "//span[@data-icon='send']")))
                    send_button.click()
                    sent = True
                    sleep(5)
                    print(style.GREEN + {translations.get('message_sent')} + style.RESET)
				except Exception as e:
					print(style.RED + f"\n{error_messages.get('failed_to_send')}")
					print(error_messages.get('internet_connection_issue'))
                    print(error_messages.get('alert_dismissal') + style.RESET)
	except Exception as e:
		print(style.RED + {translations.get('failed_to_send')} + str(e) + style.RESET)
driver.close()