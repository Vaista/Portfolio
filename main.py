import os

from flask import Flask, render_template, request
from datetime import datetime
from smtplib import SMTP


app = Flask(__name__)
app.secret_key = "d34@#@#f3sd54f3sd4gsf54g3%^^5sdf73d8f34g1%^^&*sd%$%G^43d468t4r6j4jh47j4,3j4./i4hu3fg1bsd34/a6r4f3dfn4h"
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
            msg_status = 'Success'
        except:
            msg_status = 'Failure'
            pass
        return render_template('index.html', year=date, flash_message="sending_message", msg_status=msg_status)

    return render_template('index.html', year=date)


if __name__ == '__main__':
    app.run(debug=True)
