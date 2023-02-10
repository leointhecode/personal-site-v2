import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, send_from_directory
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
import smtplib
from email.message import EmailMessage
import requests
from bs4 import BeautifulSoup

#load_dotenv()

#FLASK CONFIG

app = Flask(__name__)
app.config['SECRET_KEY'] = "SECRET" #os.getenv("FLASK_SECRET_KEY")
Bootstrap(app)

#EMAIL

MY_EMAIL = "leoworkcode@gmail.com"
MY_PASSWORD = "rfycgaqtakopitvx"

#DATA

URL = "https://github.com/leointhecode"

headers = {
    'User-Agent':
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Accept-Language':
    'en-US, en;q=0.9'
}


def getData():
    response = requests.get(url=URL, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    boxes = soup.find_all(name='div', class_='pinned-item-list-item')

    data_list =  []

    for box in boxes:

        title = box.find(name='span', class_='repo').getText().replace('-', ' ') #Funcionando, obtiene el titulo de los repositorios 
        description_raw = box.find(name='p', class_='pinned-item-desc')
        description = description_raw.getText().replace('\n', '').replace("  ", "") #Funcionando obtiene la descripcion de los repositorios
        main_language = box.find(name='span', itemprop='programmingLanguage')
        
        try:
            data = {
                'title' : title,
                'description': description,
                'main_language': main_language.getText(),
            }
        except:
             data = {
                'title' : title,
                'description': description,
                'main_language': "not used",
            }
        
        finally:
            data_list.append(data)

    return data_list



@app.route("/", methods=['GET', 'POST'])
def entrance():
    
    #Sending Mail

    if request.method == 'GET':

        name = request.args.get('name')
        email = request.args.get('email')
        message = request.args.get('message')

        if type(name) == str:

            msg = EmailMessage()

            msg['Subject'] = 'Hey, we got a new proposal.'
            msg['From'] = MY_EMAIL
            msg['To'] = 'leointhecode@gmail.com'
            msg.set_content(f"The proposal was sent from {email}. \n\n It says the following: \n\n {message}")

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(MY_EMAIL, MY_PASSWORD)
                smtp.send_message(msg)

            return redirect('/')

    return render_template('index.html', data=getData())

@app.route("/resume")
def download():
    return send_from_directory(directory="static/documents/", path="cv.pdf")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
