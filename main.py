from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = '111222'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

# db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        user_to_register = User(
            email=request.form["email"],
            password=generate_password_hash(request.form["password"],
                                            method='pbkdf2:sha256',
                                            salt_length=8),
            name=request.form["name"]
        )
        if user_to_register.email in User.query.all():
            flash("This e-mail already registered!")
        else:
            db.session.add(user_to_register)
            db.session.commit()
            login_user(user_to_register)
            return redirect(url_for('secrets'))
    return render_template("register.html")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_email = request.form["email"]
        login_pass = request.form["password"]
        user = User.query.filter_by(email=login_email).first()
        if user:
            if check_password_hash(user.password, login_pass):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash("password is incorrect", "info")
        else:
            flash("That email does not exist, try again.")
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_required
@app.route('/download')
def download():
    return send_from_directory("static/files", "cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
