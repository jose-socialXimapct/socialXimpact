from flask import Flask, render_template, request

#config is used to store passwords and other critical variables
from config import Config

## config all forms are inside the forms
import forms

### Creates Flask website and sets the config class [variables and passwords]
web_site = Flask(__name__)
web_site.config.from_object(Config)


#Routes
@web_site.route('/')
def index():
	return render_template('index.html')

@web_site.route('/ourvariables')
def ourvariables():
	return render_template('ourvariables.html')

@web_site.route("/twitter_analyzer", methods=['GET', 'POST'])
def twitter_analyzer():
  form = forms.TwitterForm()
  if form.is_submitted():
    data ={"name": True}
    return render_template("/twitter.html", form=form, data =True)
  else:
    return render_template("/twitter.html", form=form, data = False)



#Runs website
web_site.run(host='0.0.0.0', port=8080)