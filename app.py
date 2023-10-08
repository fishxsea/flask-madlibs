from flask import Flask, render_template, request
from stories import story

app = Flask(__name__)



# ===============================================
# Displays questions
@app.route('/')
def questions():
    form_prompts = story.prompts
    return render_template('homepage.html', form_prompts=form_prompts)

# Displays story
@app.route('/story')
def show_story():
    output = story.generate(request.args)
    return render_template('story-page.html', output=output)
