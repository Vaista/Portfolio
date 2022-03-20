import os

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from smtplib import SMTP


app = Flask(__name__)
smtp_email = os.environ.get('outlook_email')
receiving_email = 'vsharma5295@gmail.com'
smtp_pwd = os.environ.get('outlook_pwd')


@app.route('/', methods=['GET', 'POST'])
def home():
    date = datetime.now().year
    if request.method == 'POST':
        name = request.form.get('username')
        email = request.form.get('email')
        message = request.form.get('msg')
        try:
            connection = SMTP("smtp.office365.com", port=587)
            connection.starttls()
            connection.login(smtp_email, smtp_pwd)
            connection.sendmail(from_addr=smtp_email,
                                to_addrs=receiving_email,
                                msg=f"Subject:Message received from website\n\n{message}\nSender Name: {name}\nSender Email: {email}")
            connection.close()
        except:
            pass
        return redirect(url_for('home'))
    return render_template('index.html', year=date)


if __name__ == '__main__':
    app.run(debug=True)
