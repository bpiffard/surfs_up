# Importing flask dependency
from flask import Flask

# Creating an instance of a Flask app
app = Flask(__name__)

# Creating routes
@app.route('/')
def tavern():
    return 'welcome adventurer! stay a while! Choose respite, pick_fight, find_quest, or drink!'

@app.route('/respite')
def rest():
    return 'sit, have some tea. stay here as long as you want traveller'

@app.route('/pick_fight')
def bar_fight():
    return 'you encounter a brute! a struggle ensues!'

@app.route('/find_quest')
def quest():
    return 'you apporach a hooded stranger... he beckons you to follow him. do you dare?'

@app.route('/drink')
def drunk():
    return 'you wake up to an angry innkeeper, head pounding, body weak... what happened last night?'