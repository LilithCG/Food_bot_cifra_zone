import os

import requests
from bs4 import BeautifulSoup
from modules.database import connect_database, insert_food, create_tables


def menu_parse(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    quotes = soup.find_all('a', class_='title')
    titles = []
    links = []
    prices = []
    descriptions = []
    images = []
    sel_links = []

    # наименования
    for quote in quotes:
        titles.append(quote.text.strip())
        links.append(quote.get('href'))
    # цены
    quotes_price = soup.find_all('div', class_='product-price')
    for quote in quotes_price:
        prices.append(quote.text.strip().split('\n', 1)[0])

    # достаю описания
    for link in links:
        response_desc = requests.get(link)
        soup_desc = BeautifulSoup(response_desc.text, 'lxml')
        desc_quotes = soup_desc.find('div', class_='tab active content')
        try:
            description = " ".join(desc_quotes.text.strip().split())
        except:
            description = " "
        descriptions.append(description)

    # достаю картинки
    img_quotes = soup.find_all('img', class_='mg-product-image js-catalog-item-image')
    for quote in img_quotes:
        image_url = quote.get('src')
        img_data = requests.get(image_url).content
        image_name = image_url.rpartition('/')
        image_name = image_name[len(image_name) - 1]
        images.append(image_name)
        with open(f"parsers/pc_img/{image_name}", 'wb') as handler:
            handler.write(img_data)

    sel_quotes = soup.find_all('a', class_='product-buy')

    for quote in sel_quotes:
        sel_links.append(quote.get('href'))

    return titles, descriptions, prices, images, sel_links


if __name__ == '__main__':
    menu_urls = ['https://pizza-cheddar.ru/burgery',
                 'https://pizza-cheddar.ru/rolly',
                 'https://pizza-cheddar.ru/sety',
                 'https://pizza-cheddar.ru/sushi',
                 'https://pizza-cheddar.ru/lapsha',
                 'https://pizza-cheddar.ru/supy',
                 'https://pizza-cheddar.ru/salaty',
                 'https://pizza-cheddar.ru/zakuski',
                 'https://pizza-cheddar.ru/deserty',
                 'https://pizza-cheddar.ru/napitki',
                 'https://pizza-cheddar.ru/sousy']
    category_names = ['Бургеры',
                      'Роллы',
                      'Сеты',
                      'Суши',
                      'Лапша-Паста',
                      'Супы',
                      'Салаты',
                      'Закуски',
                      'Десерты',
                      'Напитки',
                      'Соусы']

    os.chdir('../')
    connect_database()
    create_tables()

    # pizza
    food_data = [('Пицца', 'Пицца Жульен Маленькая(25 см)', 'Куриное филе, Шампиньоны, Сыр Моцарелла, Сыр Пармезан, Соус сливочный', '285', '30_IMG_0726_2021-08-02_15-40-05.jpg', 'https://pizza-cheddar.ru/catalog?inCartProductId=14'),
                 ('Пицца', 'Пицца Жульен Средняя (35 см)', 'Куриное филе, Шампиньоны, Сыр Моцарелла, Сыр Пармезан, Соус сливочный', '494',
                  '30_IMG_0726_2021-08-02_15-40-05.jpg', 'https://pizza-cheddar.ru/catalog?inCartProductId=14'),

                 ('Пицца', 'Пицца Гавайи Маленькая(25 см)', 'Ананас, Куриное филе, Сливочный соус, Сыр Моцарелла', '285', '30_IMG_0787_2021-08-02_15-52-08.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=21'),
                 ('Пицца', 'Пицца Гавайи Средняя (35 см)', 'Ананас, Куриное филе, Сливочный соус, Сыр Моцарелла', '427',
                  '30_IMG_0787_2021-08-02_15-52-08.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=21'),

                 ('Пицца', 'Пицца Маргарита Маленькая(25 см)', 'Томатный соус, Помидор Черри, Сыр Моцарелла, Зелень', '285', '30_IMG_0782_2021-08-02_15-53-22.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=22'),
                 ('Пицца', 'Пицца Маргарита Средняя (35 см)', 'Томатный соус, Помидор Черри, Сыр Моцарелла, Зелень', '408,50',
                  '30_IMG_0782_2021-08-02_15-53-22.jpg', 'https://pizza-cheddar.ru/catalog?inCartProductId=22'),

                 ('Пицца', 'Пицца 4 сыра Маленькая(25 см)', 'Сыр Пармезан, Сыр Чеддер, Сыр Моцарелла, Сыр Дор Блю', '294,50', '30_IMG_0714_2021-08-02_15-36-59.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=12'),
                 ('Пицца', 'Пицца 4 сыра Средняя (35 см)', 'Сыр Пармезан, Сыр Чеддер, Сыр Моцарелла, Сыр Дор Блю', '475',
                  '30_IMG_0714_2021-08-02_15-36-59.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=12'),

                 ('Пицца', 'Пицца Эфунги Маленькая(25 см)', 'Ветчина, Грибы Шампиньоны, Сливочный соус, Сыр Моцарелла', '332,50', '30_IMG_0751_2021-08-02_16-00-54.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=25'),
                 ('Пицца', 'Пицца Эфунги Средняя (35 см)', 'Ветчина, Грибы Шампиньоны, Сливочный соус, Сыр Моцарелла', '484,50',
                  '30_IMG_0751_2021-08-02_16-00-54.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=25'),

                 ('Пицца', 'Пицца Пикассо Маленькая(25 см)', 'Шампиньоны, Перец Болгарский, Корнишон, Помидор Черри, Салат Руккола, Соус Томатный', '332,50', '30_pitstsa-pikasso_2022-03-10_19-00-16.png','https://pizza-cheddar.ru/catalog?inCartProductId=140'),
                 ('Пицца', 'Пицца Пикассо Средняя (35 см)',
                  'Шампиньоны, Перец Болгарский, Корнишон, Помидор Черри, Салат Руккола, Соус Томатный', '551',
                  '30_pitstsa-pikasso_2022-03-10_19-00-16.png','https://pizza-cheddar.ru/catalog?inCartProductId=140'),

                 ('Пицца', 'Пицца Пепперони Маленькая(25 см)', 'Колбаса пепперони, Сыр Моцарелла, Соус Томатный, Соус Шрирача ( только в оcтром ) ', '342', '30_pitstsa-pepperoni_2022-02-11_14-39-56.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=128'),
                 ('Пицца', 'Пицца Пепперони Средняя (35 см)',
                  'Колбаса пепперони, Сыр Моцарелла, Соус Томатный, Соус Шрирача ( только в оcтром ) ', '465,50',
                  '30_pitstsa-pepperoni_2022-02-11_14-39-56.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=128'),

                 ('Пицца', 'Пицца Пепперони Маленькая (25 см) Острая',
                  'Колбаса пепперони, Сыр Моцарелла, Соус Томатный, Соус Шрирача ( только в оcтром ) ', '351,50',
                  '30_pitstsa-pepperoni_2022-02-11_14-39-56.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=128'),
                 ('Пицца', 'Пицца Пепперони Средняя (35 см) Острая',
                  'Колбаса пепперони, Сыр Моцарелла, Соус Томатный, Соус Шрирача ( только в оcтром ) ', '475',
                  '30_pitstsa-pepperoni_2022-02-11_14-39-56.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=128'),

                 ('Пицца', 'Пицца Мексиканская Маленькая(25 см)', 'Соус Томатный, Сыр Моцарелла, Колбаса Салями, Колбаса пепперони, Индейка копченая,  Лук красный', '342', '30_pitstsa-meksikanskaya_2022-03-10_19-05-08.png','https://pizza-cheddar.ru/catalog?inCartProductId=141'),
                 ('Пицца', 'Пицца Мексиканская Средняя (35 см)',
                  'Соус Томатный, Сыр Моцарелла, Колбаса Салями, Колбаса пепперони, Индейка копченая,  Лук красный',
                  '589', '30_pitstsa-meksikanskaya_2022-03-10_19-05-08.png','https://pizza-cheddar.ru/catalog?inCartProductId=141'),

                 ('Пицца', 'Пицца Барбекю Маленькая(25 см)', 'Салями, Сыр копченный, Ветчина, Курица, Соус Барбекю, Сыр Моцарелла', '351,50', '30_IMG_0788_2021-08-02_15-42-09.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=15'),
                 ('Пицца', 'Пицца Барбекю Средняя (35 см)', 'Салями, Сыр копченный, Ветчина, Курица, Соус Барбекю, Сыр Моцарелла',
                  '522,50', '30_IMG_0788_2021-08-02_15-42-09.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=15'),

                 ('Пицца', 'Пицца Маэстро Маленькая(25 см)', 'Соус томатный, Соус Барбекю, Копченная Индейка, Колбаса сырокопченая, Колбаса варёнокопченая, Куриное филе, Сыр Моцарелла, Сыр Чеддер, Зелень', '351,50', '30_pitstsa-maestro_2022-03-10_18-52-13.png','https://pizza-cheddar.ru/catalog?inCartProductId=139'),
                 ('Пицца', 'Пицца Маэстро Средняя (35 см)',
                  'Соус томатный, Соус Барбекю, Копченная Индейка, Колбаса сырокопченая, Колбаса варёнокопченая, Куриное филе, Сыр Моцарелла, Сыр Чеддер, Зелень',
                  '598,50', '30_pitstsa-maestro_2022-03-10_18-52-13.png','https://pizza-cheddar.ru/catalog?inCartProductId=139'),

                 ('Пицца', 'Руккола с креветками Маленькая(25 см)', 'Помидор Черри, Тигровые креветки, Салат Руккола, Сыр  Моцарелла, Сыр Пармезан, Томатный соус', '361', '30_IMG_0790_2021-08-02_15-50-54.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=20'),
                 ('Пицца', 'Руккола с креветками Средняя (35 см)',
                  'Помидор Черри, Тигровые креветки, Салат Руккола, Сыр  Моцарелла, Сыр Пармезан, Томатный соус', '655,50',
                  '30_IMG_0790_2021-08-02_15-50-54.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=20'),

                 ('Пицца', 'Баварская пицца Маленькая(25 см)', 'Салями, Ветчина, Колбаса сырокопченая, Маслины,Соус томатный. Халапеньо, Сыр, Моцарелла', '370,50', '30_IMG_0809_2021-08-02_15-47-40.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=17'),
                 ('Пицца', 'Баварская Пицца Средняя (35 см)',
                  'Салями, Ветчина, Колбаса сырокопченая, Маслины,Соус томатный. Халапеньо, Сыр, Моцарелла', '570',
                  '30_IMG_0809_2021-08-02_15-47-40.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=17'),

                 ('Пицца', 'Пицца Салями Маленькая(25 см)', 'Томатный соус, Сыр Моцарелла, Салями', '389,50', '30_IMG_0766_2021-08-02_15-45-52.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=16'),
                 ('Пицца', 'Пицца Салями Средняя (35 см)', 'Томатный соус, Сыр Моцарелла, Салями', '521,55',
                  '30_IMG_0766_2021-08-02_15-45-52.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=16'),

                 ('Пицца', 'Пицца Поло Маленькая(25 см)', 'Огурчики маринованные, Томатный соус, Курица, Болгарский перец, Халапеньо', '389,50', '30_IMG_0762_2021-08-02_16-35-35.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=24'),
                 ('Пицца', 'Пицца Поло Средняя (35 см)', 'Огурчики маринованные, Томатный соус, Курица, Болгарский перец, Халапеньо',
                  '541,50', '30_IMG_0762_2021-08-02_16-35-35.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=24'),

                 ('Пицца', 'Пицца Чеддер Маленькая(25 см)', 'Куриное филе, Болгарский перец, Помидор, Сыр Моцарелла, Соус сливочный', '399', '30_IMG_0753_2021-08-02_15-34-46.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=11'),
                 ('Пицца', 'Пицца Чеддер Средняя (35 см)', 'Куриное филе, Болгарский перец, Помидор, Сыр Моцарелла, Соус сливочный',
                  '570', '30_IMG_0753_2021-08-02_15-34-46.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=11'),

                 ('Пицца', 'Пицца Цезарь Маленькая(25 см)', 'Сыр Моцарелла, Помидор Черри, Куринная грудка, Салат Ромэн', '456', '30_IMG_0743_2021-08-02_15-38-28.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=13'),
                 ('Пицца', 'Пицца Цезарь Средняя (35 см)', 'Сыр Моцарелла, Помидор Черри, Куринная грудка, Салат Ромэн', '570',
                  '30_IMG_0743_2021-08-02_15-38-28.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=13'),

                 ('Пицца', 'Охотничья Пицца Маленькая(25 см)', 'Колбаса охотничья, Томатный соус,  Огурчики маринованные, Шампиньоны, Сыр Моцарелла, Помидор Черри', '484,50', '30_IMG_0774_2021-08-02_15-56-03.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=23'),
                 ('Пицца', 'Охотничья Пицца Средняя (35 см)',
                  'Колбаса охотничья, Томатный соус,  Огурчики маринованные, Шампиньоны, Сыр Моцарелла, Помидор Черри',
                  '646', '30_IMG_0774_2021-08-02_15-56-03.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=23'),

                 ('Пицца', 'Пицца Салмоне Маленькая(25 см)', 'Лосось, Помидоры Черри, Сыр Моцарелла, Соус Сливочный', '541,50', '30_pitstsa-salmone_2022-07-18_15-13-01.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=23'),
                 ('Пицца', 'Пицца Салмоне Средняя (35 см)', 'Лосось, Помидоры Черри, Сыр Моцарелла, Соус Сливочный', '636,50',
                  '30_pitstsa-salmone_2022-07-18_15-13-01.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=23'),

                 ('Пицца', 'Пицца Филадельфия Маленькая(25 см)', 'Лосось, Сыр Филадельфия, Сливочный соус, Сыр Моцарелла', '598,50', '30_IMG_0802_2021-08-02_15-50-00.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=19'),
                 ('Пицца', 'Пицца Филадельфия Средняя (35 см)', 'Лосось, Сыр Филадельфия, Сливочный соус, Сыр Моцарелла', '703',
                  '30_IMG_0802_2021-08-02_15-50-00.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=19'),

                 ('Пицца', 'Морская Пицца Маленькая(25 см)', 'Маслины, Снежный краб, Лосось, Креветки Тигровые, Лимон,Сыр Моцарелла, Соус сливочный', '617,50', '30_IMG_0805_2021-08-02_15-48-57.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=18'),
                 ('Пицца', 'Морская Пицца Средняя (35 см)',
                  'Маслины, Снежный краб, Лосось, Креветки Тигровые, Лимон,Сыр Моцарелла, Соус сливочный', '741',
                  '30_IMG_0805_2021-08-02_15-48-57.jpg','https://pizza-cheddar.ru/catalog?inCartProductId=18')

                 ]
    insert_food(food_data)
    for _ in range(len(menu_urls)):
        titles, descriptions, prices, images, sel_links = menu_parse(menu_urls[_])

        food_data = []
        for i in range(len(titles)):
            row = (category_names[_], titles[i], descriptions[i], prices[i], images[i], sel_links[i])
            food_data.append(row)
        insert_food(food_data)
