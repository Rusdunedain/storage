
import telebot
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import threading

#pip install pytelegrambotapi

#МОСКВА

def get_html(url):
  response = urllib.request.urlopen(url)
  return response.read()

def parse(html):
  threading.Timer(3600.0, parse).start()
  global temp, temp1, temp2, temp3, temp4
  soup = BeautifulSoup(html, 'html.parser')
  temp = soup.find('div', class_='temp fact__temp fact__temp_size_s')
  temp1 = soup.find('div', class_='link__feelings fact__feelings')
  temp1 = temp1.find('div', class_='link__condition day-anchor i-bem')
  temp2 = soup.find('div', class_='forecast-briefly__day swiper-slide')
  temp3 = temp2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')
  temp4 = temp2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')

def main():
  pars=(get_html('https://yandex.ru/pogoda/moscow'))
  parse(pars)

if __name__ == '__main__':
  main()

#СЕВАН

def get_html(url):
  response = urllib.request.urlopen(url)
  return response.read()

def parse(html):
  threading.Timer(3600.0, parse).start()
  global temps, temps1, temps2, temps3, temps4, temps5
  soup = BeautifulSoup(html, 'html.parser')
  temps = soup.find('div', class_='temp fact__temp fact__temp_size_s')
  temps1 = soup.find('div', class_='link__feelings fact__feelings')
  temps1 = temps1.find('div', class_='link__condition day-anchor i-bem')
  temps2 = soup.find('div', class_='forecast-briefly__day swiper-slide')
  temps3 = temps2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')
  temps4 = temps2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')

def main():
  pars=(get_html('https://yandex.ru/pogoda/10263?via=srp'))
  parse(pars)

if __name__ == '__main__':
  main()

#ТАТЕВ
  
def get_html(url):
  response = urllib.request.urlopen(url)
  return response.read()

def parse(html):
  threading.Timer(3600.0, parse).start()
  global tempt, tempt1, tempt2, tempt3, tempt4, tempt5
  soup = BeautifulSoup(html, 'html.parser')
  tempt = soup.find('div', class_='temp fact__temp fact__temp_size_s')
  tempt1 = soup.find('div', class_='link__feelings fact__feelings')
  tempt1 = tempt1.find('div', class_='link__condition day-anchor i-bem')
  tempt2 = soup.find('div', class_='forecast-briefly__day swiper-slide')
  tempt3 = tempt2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')
  tempt4 = tempt2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')

def main():
  pars=(get_html('https://yandex.ru/pogoda/?lat=39.38433838&lon=46.24163055'))
  parse(pars)

if __name__ == '__main__':
  main()

#ЕРЕВАН

def get_html(url):
  response = urllib.request.urlopen(url)
  return response.read()

def parse(html):
  threading.Timer(3600.0, parse).start()
  global tempy, tempy1, tempy2, tempy3, tempy4, tempy5
  soup = BeautifulSoup(html, 'html.parser')
  tempy = soup.find('div', class_='temp fact__temp fact__temp_size_s')
  tempy1 = soup.find('div', class_='link__feelings fact__feelings')
  tempy1 = tempy1.find('div', class_='link__condition day-anchor i-bem')
  tempy2 = soup.find('div', class_='forecast-briefly__day swiper-slide')
  tempy3 = tempy2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_day')
  tempy4 = tempy2.find ('div', class_='temp forecast-briefly__temp forecast-briefly__temp_night')
  #tempy5 = tempy4.find ('div', class_='forecast-briefly__condition')

def main():
  pars=(get_html('https://yandex.ru/pogoda/yerevan'))
  parse(pars)

if __name__ == '__main__':
  main()

#КОРОНАВИРУС

def get_html(url):
  #req = Request(url)
  #req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36')
  #content = urlopen(req).read()
  response = urllib.request.urlopen(url)
  return response.read()
  #return content

def parse(html):
  threading.Timer(3600.0, parse).start()
  global full, rus, arm, death
  soup = BeautifulSoup(html, 'html.parser')
  full = soup.find('div', class_='maincounter-number')
  #rus = soup.find ('tbody')
  #rus = rus.find('tr', style="font-weight: bold; font-size:15px; text-align:left; padding-left:3px;")
  arm = soup.find('table', id='main_table_countries')
  death = soup.find('div', id='maincounter-wrap', style='margin-top:15px')
  death = death.nextSibling.nextSibling('span')
  #print (full.text)
  print (death[0].text)
  #print (rus)
def main():
  pars=(get_html('https://www.worldometers.info/coronavirus/#countries'))
  #pars=(get_html('https://multimedia.scmp.com/widgets/china/wuhanvirus'))
  parse(pars)

if __name__ == '__main__':
  main()


bot = telebot.TeleBot('1101151244:AAH3UjFnCwpW2HeoRSMvdFQvza4IsPXf8t0')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Москва', 'Армения', 'Коронавирус ебаный')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'москва':
        bot.send_message(message.chat.id, 'В Москве сейчас (яндекс): ' + temp.text +' '+ temp1.text +';\n'+ temp3.text+'\n'+temp4.text)
    elif message.text.lower() == 'армения':
        bot.send_message(message.chat.id, 'В Ереване сейчас (яндекс): '+ tempy.text +' '+ tempy1.text +';\n'+ tempy3.text+'\n'+tempy4.text+'\n\nВ Татеве сейчас (яндекс): '+tempt.text +' '+ tempt1.text +';\n'+ tempt3.text+'\n'+tempt4.text+'\n\nНа Севане сейчас (яндекс): '+ temps.text +' '+ temps1.text +';\n'+ temps3.text+'\n'+temps4.text)
    elif message.text.lower() == 'коронавирус ебаный':
        bot.send_message(message.chat.id, 'Всего случаев: '+full.text+'\nКол-во смертей: '+death[0].text+'\nСтатискика по странам:'+arm.text)

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

bot.polling() 
