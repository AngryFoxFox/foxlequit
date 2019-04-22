#!/usr/bin/env python
import sys
sys.path.insert(0, '../')

from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
from boto.s3.connection import S3Connection
import random
import time
import json
from vk_api.utils import sjson_dumps

#login, password='login','password'
# vk_session = vk_api.VkApi(login, password)
#edcfc72412b0b9cd52974cba1cba97315d3eb820406044d3dda58dd66299745f6e37f4e1fc576b09c46c0 
#71ab264bb90f343cd9f54cd737818e618c91feb797c1d8b3ac10753f31037f6717b839e4e6b2fa918f0ab test
# vk_session.auth()
token ='token'
vk_session = vk_api.VkApi(token="0c9fb4a1d62e25bc3c56dde20ea81b7fc3760f0fb21c2fda6f07e50bb8d792fa10c818fce7c8d08bb17b3")

longpoll = VkLongPoll(vk_session)



def create_keyboard(response):
    keyboard = VkKeyboard(one_time=False)

    if response == 'начать':
        'начать'.replace('н', 'Н')

        keyboard.add_button('Оплата и доставка', color=VkKeyboardColor.DEFAULT)
        keyboard.add_button('Выбрать размер', color=VkKeyboardColor.POSITIVE)

        keyboard.add_line()  # Переход на вторую строку

        keyboard.add_button('Оформить заказ', color=VkKeyboardColor.PRIMARY)
        keyboard.add_button('Помощь', color=VkKeyboardColor.PRIMARY)


    elif response == 'привет':
        keyboard.add_button('Тест', color=VkKeyboardColor.POSITIVE)

    elif response == 'котики':
        keyboard.add_button('Котики!', color=VkKeyboardColor.POSITIVE)

    elif response == 'закрыть':
        print('закрываем клаву')
        return keyboard.get_empty_keyboard()

    keyboard = keyboard.get_keyboard()
    return keyboard


def send_message(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',{id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648), "attachment": attachment, 'keyboard': keyboard})

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print(ascii ('Текст сообщения: ' + str (event.text)))
            print(event.user_id)
            response = event.text.lower()
            keyboard = create_keyboard(response)

            if event.from_user and not event.from_me:
                if response == "Начать":
                    send_message(vk_session, 'user_id', event.user_id, message='Выбери нужное', keyboard=keyboard)

                elif response == "начать":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Выбери нужное',keyboard=keyboard)
                    
                          
                elif response == "оплата и доставка":
                    send_message(vk_session, 'user_id', event.user_id, message='Доставка осуществляется по всей России, стоимость доставки зависит от вашего региона. Оплатить заказ можно следующими способами: Перевод на карту Сбербанк, QIWI кошелек или используя "Товары ВКонтакте"')

                elif response == "помощь":
                    send_message(vk_session, 'user_id', event.user_id, message='Пиши сюда свой вопрос. Скоро мы ответим на него')

                elif response == "выбрать размер":
                    send_message (vk_session, 'user_id', event.user_id, message='Напиши свой рост и вес, мы поможем выбрать тебе размер')
                    
                elif response == "оформить заказ":
                    send_message(vk_session, 'user_id', event.user_id, message= 'Для оформления заказа напиши 1.Что хочешь купить 2.Полный адрес 3.Индекс 4.Размер или используй "Магазин ВКонтакте"')
                    



            print('-' * 30)
