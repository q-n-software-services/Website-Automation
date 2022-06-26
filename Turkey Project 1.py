from plyer import notification
import time
from selenium import webdriver
import pywhatkit
import pyautogui as pt
import keyboard

# send the email
import smtplib

# email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import datetime
import os
cwd = os.getcwd()
path = cwd + '/chromedriver.exe'
os.environ['PATH'] += path

while True:
    driver = webdriver.Chrome()
    driver.get("https://ais.usvisa-info.com/en-tr/iv/users/sign_in")

    email_input = driver.find_element_by_id('user_email')
    email_input.send_keys('salmanmahad34@gmail.com')
    password_input = driver.find_element_by_id('user_password')
    password_input.send_keys('G6@Lp6b76ZqY!w!')
    check_box = driver.find_element_by_css_selector('label[for="policy_confirmed"]')
    check_box.click()
    sign_in_button = driver.find_element_by_name('commit')
    sign_in_button.click()

    url = driver.current_url

    continue_button = driver.find_element_by_xpath("//a[@href='/en-tr/iv/schedule/40218114/continue_actions']")
    continue_button.click()

    url2 = driver.current_url

    schedule_appointment = driver.find_elements_by_class_name('accordion-item')
    schedule_appointment[0].click()
    new = driver.current_url.split('/')
    new.pop(-1)
    a = '/'
    new = a.join(new)
    new += '/continue'
    driver.get(new)
    driver.implicitly_wait(30)
    time.sleep(2)
    text = driver.find_element_by_xpath(
        '/html/body/div[4]/main/div[4]/div/div/form/fieldset/ol/fieldset/div/div[1]/div[2]/small')
    print(text)
    print(text.text)
    data = str(text.text)
    time.sleep(2)

    driver.close()
    time.sleep(2)

    if data != 'There are no available appointments at the selected location. Please try again later.':
        pywhatkit.sendwhatmsg_instantly('+905524360865', data)
        position = pt.locateOnScreen('send_button.png', confidence=0.9)
        pt.moveTo(position)
        pt.click()
        time.sleep(1)
        keyboard.press_and_release('ctrl+w')
        keyboard.press('space')

        now = datetime.datetime.now()
        # email content placeholder
        content = ''
        cnt = "<h1>{}</h1>".format(data)
        content += cnt
        content += ('<br>------<br>')
        content += ('<br><br>End of Message')

        # Update your Email Details

        SERVER = 'smtp-relay.sendinblue.com'  # your smtp server
        PORT = 587  # your Port Number
        FROM = 'qnsoftwareservices12272@gmail.com'  # "Your From Email ID"
        TO = 'salmanmahad34@gmail.com'  # "Your To Email Ids " Can be a list
        PASS = '5Yq9UA7dWMCGLx3v'  # "Your Email Id's Password

        # Create a text/plain message
        msg = MIMEMultipart()
        msg.add_header('Content-Disposition', 'attachment', filename='HongKong project.py')
        msg['Subject'] = 'UPDATE :\t\t' + '' + str(now.day) + '-' + str(now.month) + '-' + str(
            now.year) + '\ttime :\t\t' + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        msg['From'] = FROM
        msg['To'] = TO
        msg.attach(MIMEText(content, 'html'))

        print("Initializing Server....")
        server = smtplib.SMTP(SERVER, PORT)
        server.set_debuglevel(0)
        server.ehlo()
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, TO, msg.as_string())

        print('Email Sent !')
        server.quit()

        notification.notify(
            title="\t\tUPDATE",
            message=data,
            timeout=12
        )

    time.sleep(300)






