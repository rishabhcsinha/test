from flask import Flask,request,render_template,redirect,url_for,flash

app = Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = 'a|\x92_,\xc5\xb3\x1ez\x11\xd4=RwK\x92;\xa6f\xbc\xcfD\rM'

# import os
# basedir = os.path.abspath(os.path.dirname(__file__))



from views import *
 
if __name__ == '__main__':
	app.run()