from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask import Flask, render_template
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email


secret_email = "admin@email.com"
secret_password = "12345678"


class MyForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email(message="Invalid Email, bruh")])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, message="Password is too short, just like your...")])
    submit = SubmitField(label="Lessss goo")


app = Flask(__name__)
app.secret_key = "123321"
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def get_login():
    login_form = MyForm()
    if login_form.validate_on_submit():
        if login_form.email.data == secret_email and login_form.password.data == secret_password:
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
