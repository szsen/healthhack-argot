from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
@app.route('/poop')
def poop():
	return "this is poop"