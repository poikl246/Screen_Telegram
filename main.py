import keyboard
import telebot
import pyautogui
import time
import os
# options



try:
    os.mkdir('files')
except:
    pass


with open('data.txt') as conf:
    bot_api = (conf.readline())[:-1]
    admin_l = conf.readlines()
    admin_list = []
    for admin in admin_l[:-1]:
        admin_list.append(admin[:-1])

    if list(admin_l[-1])[-1] != '\n':
        admin_list.append(int(admin_l[-1]))
    else:
        admin_list.append(int((admin_l[-1])[:-1]))
    print(admin_list)

bot = telebot.TeleBot(bot_api)


def main():

    try:
        # os.system('start cmd_stop.bat')
        i = 0
        a = '0'
        while True:
            b = a
            a = keyboard.read_key()
            print(a)
            if a == b and (a == '`' or a == '~' or a == "ё" or a == 'Ё'):
                pyautogui.screenshot(f'files/screenshot{i}.png')
                nado(i)
                i += 1
                a = '0'


    except Exception as ex:
        pass
        # print(ex)



def nado(i):

    try:
        if os.path.exists(f'files/screenshot{i}.png'):
            for admin in admin_list:
                bot.send_photo(admin, open(f"files/screenshot{i}.png", "rb"))
                bot.send_document(admin, open(f"files/screenshot{i}.png", "rb"))


        else:
            print("ОШИБКА")
            nado(i)
    except:
        nado(i)







if __name__ == '__main__':
    main()

