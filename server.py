from flask import Flask, render_template, url_for

app= Flask(__name__)
print(__name__) 



@app.route('/index.html')
def my_home():
	return render_template('index.html')

@app.route('/')
def hone():
	return render_template('index.html')


@app.route('/wishes.html')
def wishes():
	return render_template('wishes.html')

# @app.route('/components.html')
# def components():
# 	return render_template('components.html')

# @app.route('/')
# def my_home():
# 	return render_template('index.html')