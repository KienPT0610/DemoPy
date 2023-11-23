from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests
from bs4 import BeautifulSoup
import yagmail
import getpass
import telebot
import smtplib
def getNew():
    href = []
    r = requests.get('https://baomoi.com/tag/LITE.epi')
    soup = BeautifulSoup(r.text, 'html.parser')
    mydiv = soup.find_all('h3', {'class':'bm_F'})
    for new in mydiv:
        href.append('http://baomoi.com/' + new.a.get('href'))
    return href

def infMylove():
    body = '''
    Name: Vu Thi Thu Trang
    Age: 20
    Date: 17/03/2003
    Day'love: 10/03/2023
    Day: 259
    https://www.facebook.com/seri.kimberly
    '''
    return body

def Album():
    arrImg = []
    fi = open(r'ArrImg.txt', 'r', encoding='utf8')
    r = fi.read().split()
    arrImg.append(r)
    return arrImg

async def album(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    img = Album()
    for i in img:
        file = open({i}, "rb").read()
        # await update.message.reply_text(f'{file}')
        await update.message.reply_photo(photo=file)
def getlove():
    text = 'Anh yeu bao boi'
    return text

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hi! {update.effective_user.first_name} \nI am Kien PT')


async def news(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    title = getNew()
    for i in title:
        await update.message.reply_text(f'News!: \n {i}')

async def mylove(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    info = infMylove()
    await update.message.reply_text(f'{info}')
    photo_url = "ThuChang.jpg"
    await update.message.reply_photo(photo=photo_url)

async def love(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    title = getlove()
    for _ in range(100):
        await update.message.reply_text(f'Kien said: \n {title}')

app = ApplicationBuilder().token("6759211540:AAEKCO04kstujuNG95bdFhCYtGICNWEpsjM").build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("News", news))
app.add_handler(CommandHandler("Love", love))
app.add_handler(CommandHandler("Mylove", mylove))
app.add_handler(CommandHandler("Album", album))
app.run_polling()
