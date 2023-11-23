from flask import Flask, render_template
import random
f1 = str('Большинство людей, страдающих технологической зависимостью, испытывают сильный стресс, когда они находятся вне зоны покрытия сети или не могут использовать свои устройства.')
f2 = str('Согласно исследованию, проведенному в 2018 году, более 50% людей в возрасте от 18 до 34 лет считают себя зависимыми от своих смартфонов.')
f3 = str('Изучение технологической зависимости является одной из наиболее актуальных областей научных исследований в настоящее время.')
facts_list = [f1, f2, f3]

number = 'abcdefghijklmnopqrstuvwz1234567890'
password = ''
for i in range(8):
    password += random.choice(number)


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')



@app.route('/index1')
def index1():
    return f"<p>{random.choice(facts_list)}</p>"

@app.route('/index2')
def index2():
    return f"<p>{password}</p>"


if __name__ == '__main__':
    app.run(debug=True)
