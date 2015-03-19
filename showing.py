import config
import requests
import smtplib
import email.mime.multipart
import email.mime.text
from bs4 import BeautifulSoup

session = requests.session()


def catch():
    r = session.get('http://movie.douban.com/nowplaying/'+config.city)
    nowplaying = BeautifulSoup(r.text).find(id='nowplaying')
    movies = nowplaying.contents[3].contents[1].contents

    id_list = []
    for movie_id in open('movie', 'r'):
        id_list.append(int(movie_id))

    send_list = []
    f = open('movie', 'a')
    for movie in movies:
        if str(movie).strip() != '':
            if int(movie['id']) not in id_list:
                f.write(movie['id']+'\n')
                if compare(movie):
                    send_list.append(movie)
    if len(send_list) > 0:
        send_email(send_list)
    f.close()


def send_email(movies):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = config.s_email
    msg['to'] = config.c_email
    msg['subject'] = config.title.format(len(movies),config.rating)
    content = config.content.format(config.rating,config.ratings_count)
    for movie in movies:
        content = content + config.content_2.format(movie['data-title'],
                                                    movie['data-actors'],
                                                    movie['data-director'],
                                                    movie['data-region'],
                                                    movie['data-score'],
                                                    movie['data-votecount'],
                                                    movie.ul.li.a['href'])
    msg.attach(email.mime.text.MIMEText(content))
    print(content)
    smtp=smtplib.SMTP()
    smtp.connect('smtp.aliyun.com','25')
    smtp.login(config.s_email, config.s_password)
    smtp.sendmail(config.s_email, config.c_email,str(msg))
    smtp.quit()


def compare(movie):
    if int(movie['data-votecount']) > config.ratings_count and float(movie['data-score']) > config.rating:
        return True
    return False
