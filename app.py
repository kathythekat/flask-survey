from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def index():
    return render_template(
        'survey_start.html'
    )
    
@app.route('/questions/<post_id>', methods = ["POST"])
#need URL parameter
def questions(post_id):
    questions = survey.questions #array

    if len(questions) == len(responses):
        return redirect('/completion.html')
    question_list = []
    choices_list = []
    
    for question in questions:
        question_list.append(question.question)
        choices_list.append(question.choices)

    #questions is an array of questions object
    return render_template(
        'question.html',
        post_id = post_id,
        questions = question_list[post_id],
        choices = choices_list[post_id]
    )

@app.route('/answers', methods = ["POST"])
#TODO:
    # append to responses array
    #get URL parameter: response.form[]
  
#append to responses list what user clicked on 
#if question/0 then go to questions/1
def answers():
    return redirect(f'/questions/{len(responses)}')
    



