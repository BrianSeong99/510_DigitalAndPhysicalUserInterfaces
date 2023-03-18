"""Flask application with embedded chatbot and analytics"""
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import pandas as pd
import requests

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'bdqVBWEsRebA4d@GiXm7'

index = 0

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

class ChatbotBrian(FlaskForm):
    response = StringField("How was your day?", validators=[DataRequired()])
    submit = SubmitField('Submit')

class Chatbot(FlaskForm):
    response = StringField('How are you feeling today?',
                           validators=[DataRequired()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', e=e), 404


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    name = None
    instr = "Please proceed to the Chatbot"
    if form.validate_on_submit():
        name = form.name.data
    return render_template('index.html', form=form, name=name, instr=instr)


@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    form = Chatbot()
    response = None
    if form.validate_on_submit():
        response = form.response.data
    return render_template('chatbot.html', form=form, response=response)


@app.route('/chatbot/brian', methods=['GET', 'POST'])
def chatbotbrian():
    positive_list = list(pd.read_csv("data/positive_words.txt", header=0).iloc[:,0].values)
    negative_list = list(pd.read_csv("data/negative_words.txt", header=0).iloc[:,0].values)
    
    positive_count = 0
    negative_count = 0

    form = ChatbotBrian()
    response = None
    if form.validate_on_submit():
        data = form.response.data
        for word in data.split(' '):
            if word in negative_list:
                negative_count = negative_count + 1
            if word in positive_list:
                positive_count = positive_count + 1
        if positive_count > negative_count:
            response = "Great"
        elif positive_count < negative_count:
            response = "Too Bad!"
        else:
            response = "I see."
    return render_template('chatbot.html', form=form, response=response)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
