from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    coffe_list = ["✘", "☕", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"]
    wifi_list = ["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"]
    power_list = ["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"]

    cafe = StringField('Cafe name', validators=[DataRequired()])
    cafe_location = StringField('Cafe Location on Google Maps', validators=[DataRequired(), URL()])
    cafe_open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    cafe_close = StringField('Closing Time e.g. 9PM', validators=[DataRequired()])
    cafe_coffee = SelectField('Coffee Rating', choices=coffe_list, validators=[DataRequired()])
    cafe_wifi = SelectField('Wifi Strength Rating', choices=wifi_list, validators=[DataRequired()])
    cafe_power = SelectField('Power Socket Availability', choices=power_list, validators=[DataRequired()])

    submit = SubmitField('Submit')


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe_data = [
            form.cafe.data,
            form.cafe_location.data.strip(),
            form.cafe_open.data,
            form.cafe_close.data,
            form.cafe_coffee.data,
            form.cafe_wifi.data,
            form.cafe_power.data
        ]
        with open('cafe-data.csv', 'a', newline='', encoding='utf8') as csv_file:
            csv_receive_file = csv.writer(csv_file, delimiter=",")
            csv_receive_file.writerow(new_cafe_data)

    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            print(row)
    return render_template('cafes.html', cafes=list_of_rows, cafe_len=len(list_of_rows) + 2)


if __name__ == '__main__':
    app.run(debug=True)
