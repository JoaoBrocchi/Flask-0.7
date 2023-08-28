from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,EmailField,SubmitField
from wtforms.validators import DataRequired, Email, Length
from wtforms.validators import email_validator
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "any-string-you-want-just-keep-it-secret"
Bootstrap(app)

class LoginForm(FlaskForm):
    email = EmailField('Email',validators=[Length(min=1,max=30),Email(message="oi")])
    password = PasswordField('Password',validators=[DataRequired()])
    submit = SubmitField(label="log in")






@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@email.com" and login_form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template("denied.html")

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)