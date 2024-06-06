PRICE_WEIGHT_BISH = 3.6  # для цены по весу в Караколе
PRICE_VOLUME_BISH = 370 # для цены по обьему в Караколе

ADMIN_PASSWORD = '1'

LINK_WHATSAPP = ''


ADRESS_BISH = '收货人:佛FO-{}\n☎️:+8615547009391\n{}\n地址:广东省广州市白云区江高镇南岗三元南路广新元素54云创港1119-佛FO-{}库房 ({})'
PINDUODUO = 'link1'
TAOBAO = 'link2'
ONE_AND_SIX = 'link3' #1688
POIZON = 'link4'

def send_adress(id,phone_number,lang,city,ADRESS_BISH):
    if lang == 'RU':
        if city == 'BISH':
            return ADRESS_BISH.format(id,'Полный адрес',id,phone_number)
    else:
        if city == 'BISH':
            return ADRESS_BISH.format(id,'Толук адрес',id,phone_number)
    

def send_profile(kwargs):
    if kwargs['language'] == 'RU':
        text = '📃Ваш профиль📃\n🪪 Персональный id: {}\n👤 Имя: {}\n👤 Фамилия: {}\n📞 Номер: {}\n🌍 Геопозиция: {}'
    if kwargs['language'] == 'KG':
        text = '📃Сиздин профилиниз📃\n🪪 Жеке id: {}\n👤 Аты: {}\n👤 Фамилия: {}\n📞 Номер: {}\n🌍 Турган жери: {}'
    if kwargs["city"] == 'BISH':
        city = 'Бишкек'

    if kwargs['language'] == 'RU':
        return text.format(kwargs['id'], kwargs['name'], kwargs['full_name'], kwargs['phone_number'], city)
    elif kwargs['language'] == 'KG':
        return text.format(kwargs['id'], kwargs['name'], kwargs['full_name'], kwargs['phone_number'], city)

def cancel_sender(lang):
    if lang == 'RU':
        return f'Вы отменили последнее действие'
    else:
        return f'Акыркы аракетиңизди артка кайтардыңыз'
    