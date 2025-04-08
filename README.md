# Асинхронный чат-бот для телеграмм.


## Функционал
Задача, которую должен решать бот:
1. В боте должно быть меню из 3 кнопок: «Получить информацию по товару», «Остановить уведомления», «Получить информацию из БД».
2. Нажимая на кнопку «Получить информацию по товару», Пользователь отправляет в бота артикул товара с Wildsberries (например: 211695539).
3. Бот должен выдать информацию о товаре (карточке) - Название, артикул, цена, рейтинг товара, количество товара на всех складах.
Все эти данные получаются по запросу: https://card.wb.ru/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={артикул товара}
4. Под сообщением, которые присылает бот, должна быть inline-кнопка - «подписаться». По нажатию на которую должны приходить уведомления от бота каждые 5 минут с сообщением, что было выше. (Название, артикул, цена, рейтинг товара, количество товара на всех складах)
5. При нажатии на кнопку «Остановить уведомления» - уведомления останавливаются.
6. При нажатии на кнопку «Получить информацию из БД» бот должен прислать сообщение с последними 5 записями из БД.

Бот должен быть написан на Python 3.9+, с использованием библиотек: Aiogram 3. Реализовать взаимодействие с базой данных для сохранения истории запросов (использовать SQLAlchemy и PostgreSQL). Должны сохраняться id пользователя, время запроса, артикул товара. Бота упакован в docker, развернут на сервере.

Оформление внутри бота — сообщений и тд на ваше усмотрение, но приветствуется оригинальный подход.


## Стек 
* Python 3.12
* Aiogram
* SQLAlchemy
* APScheduler
* Python-dotenv

