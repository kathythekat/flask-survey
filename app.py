from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

#responses = []

@app.route('/')
def index():
    return render_template(
        'survey_start.html'
    )

@app.route('/completion')
def final():
    return render_template(
        'completion.html'
    )
    
@app.route('/questions/<int:post_id>')
#need URL parameter
def questions(post_id):
    questions = survey.questions #array of question objects

    if len(questions) == len(session['responses']):
        return redirect('/completion')
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
def answers():

    responses = session['responses']
    responses.append(request.form.get('answer'))
    print(request.form.get('value'))
    session['responses'] = responses

    return redirect(f"/questions/{len(session['responses'])}")

@app.route('/begin', methods = ['POST'])
def init():
    session['responses'] = []

    return redirect(f'/questions/0')
    



