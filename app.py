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
    questions = survey.questions
    # responses = session['responses']
    if len(session['responses']) != post_id:
        flash("Don't go out of order!")
        return redirect(f"/questions/{len(session['responses'])}")

    if len(questions) == len(session['responses']):
        return redirect('/completion')

    return render_template(
        'question.html',
        post_id = post_id,
        questions = questions[post_id].question,
        choices = questions[post_id].choices
    )

@app.route('/answers', methods = ["POST"])
def answers():

    responses = session['responses']
    responses.append(request.form.get('answer'))
    session['responses'] = responses

    return redirect(f"/questions/{len(session['responses'])}")

@app.route('/begin', methods = ['POST'])
def init():
    session['responses'] = []
    return redirect(f'/questions/0')
    



