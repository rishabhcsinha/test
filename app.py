from flask import Flask,request,render_template,redirect,url_for,flash

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'a|\x92_,\xc5\xb3\x1ez\x11\xd4=RwK\x92;\xa6f\xbc\xcfD\rM'

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/',methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file_list=['test1','test2']
        if request.form['file'] in file_list:
            return 'sahi hai boss'
        else :
            flash ('galat value daala hai')
            return redirect(url_for('index'))

    else :
    	return render_template('index.html')

# from views import *
 
if __name__ == '__main__':
	app.run()