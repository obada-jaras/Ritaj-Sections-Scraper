import asyncio
import contextlib
from seleniumbase import SB
from telegram import Bot

from config import STUDENT_ID, PASSWORD
from config import TELEGRAM_API_TOKEN



CHECK_EVERY = 3 # seconds

sb = None
bot = Bot(TELEGRAM_API_TOKEN)
counter = 0

async def main():
    global sb
    send_telegram_message("Bot started!")

    with SB(uc=True) as sb:
        await login()
        await check_if_secion_available()


async def check_if_secion_available():
    global sb

    while True:
        try:
            await check_if_login_needed()
            
            sb.open("https://ritaj.birzeit.edu/reg")
            print("Entered reg page")
            sb.wait(3)

            regetered_courses_xpath = "/html/body/div[2]/div[3]/div[1]/div[2]/div/div/div/div[1]/ul/li[2]/a"
            sb.click(regetered_courses_xpath)
            sb.click(regetered_courses_xpath)
            sb.click(regetered_courses_xpath)
            print("Entered regetered courses page")
            sb.wait(3)

            nlp_selector = "#reg > div > table > tbody > tr:nth-child(5) > td:nth-child(10) > a"
            sb.click(nlp_selector)
            print("Entered nlp page")
            sb.wait(3)

            current_students_number_selector = "#ccInfo > tbody > tr.full > td:nth-child(4)"
            current_students_number_sec2 = sb.get_text(current_students_number_selector)
            current_students_number_sec2 = int(current_students_number_sec2)
            print("nlp current students number: " + str(current_students_number_sec2))
            if current_students_number_sec2 < 45:
                send_telegram_message("NLP is available!\t" + str(current_students_number_sec2))

            sb.click(regetered_courses_xpath)
            sb.click(regetered_courses_xpath)
            sb.click(regetered_courses_xpath)
            print("Entered regetered courses page again")
            sb.wait(3)

            compiler_selector = "#reg > div > table > tbody > tr:nth-child(4) > td:nth-child(10) > a"
            sb.click(compiler_selector)
            print("Entered compiler page")
            sb.wait(3)

            compiler_current_students_number_sec2_xpath = "/html/body/div[2]/div[3]/div[7]/div[2]/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[3]/td[4]"
            current_students_number_sec2 = sb.get_text(
                compiler_current_students_number_sec2_xpath)
            current_students_number_sec2 = int(current_students_number_sec2)
            print("compiler sec2 current students number: " + str(current_students_number_sec2))
            if current_students_number_sec2 >= 43:
                send_telegram_message("Complier is about to full!\t" + str(current_students_number_sec2))
                # send_telegram_message("Compiler is available!\t" + str(current_students_number))

            compiler_current_students_number_sec1_xpath = "/html/body/div[2]/div[3]/div[7]/div[2]/div/div[1]/table/tbody/tr[2]/td/div/table/tbody/tr[2]/td[4]"
            current_students_number_sec1 = sb.get_text(
                compiler_current_students_number_sec1_xpath)
            current_students_number_sec1 = int(current_students_number_sec1)
            print("compiler sec1 current students number: " + str(current_students_number_sec1))
            if current_students_number_sec1 < 45:
                send_telegram_message("Compiler is available!\t" + str(current_students_number_sec1))

            global counter
            counter += 1
            print(counter)
            if counter % 100 == 0:
                send_telegram_message("Still running!\t" + counter)
            
            sb.wait(CHECK_EVERY)

        except Exception as e:
            print(e)
            # send_telegram_message("An error occured!\t" + str(e))
            sb.wait(10)







async def login():
    global sb

    sb.open("https://ritaj.birzeit.edu")
    sb.wait(7)

    with contextlib.suppress(Exception):
        human_checkbox_selector1 = "#cf-stage > div.ctp-checkbox-container > label > input[type=checkbox]"
        human_checkbox_selector2 = "#challenge-stage > div > input"
        if human_checkbox := sb.find_element(human_checkbox_selector1):
            sb.click(human_checkbox)
        elif human_checkbox := sb.find_element(human_checkbox_selector2):
            sb.click(human_checkbox)
        sb.wait(5)

    studentID_selector = "#register-login > form > table > tbody > tr:nth-child(1) > td.form-widget > input[type=text]"
    sb.update_text(studentID_selector, STUDENT_ID)
    sb.wait(0.5)

    password_selector = "#register-login > form > table > tbody > tr:nth-child(2) > td.form-widget > input[type=password]"
    sb.update_text(password_selector, PASSWORD)
    sb.wait(0.5)

    loginButton_selector = "#register-login > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"
    sb.click(loginButton_selector)
    sb.wait(3)

    send_telegram_message("Login successful!")

async def check_if_login_needed():
    global sb

    with contextlib.suppress(Exception):
        loginButton_selector = "#register-login > form > table > tbody > tr:nth-child(3) > td > input[type=submit]"
        sb.find_element(loginButton_selector)
        await login()

def send_telegram_message(course):
    chat_id = 6123911846
    bot.send_message(chat_id=chat_id, text=course)


if __name__ == '__main__':
    asyncio.run(main())
