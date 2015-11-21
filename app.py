from flask import Flask, render_template, request
import requests
from datetime import datetime
app = Flask(__name__)


@app.route("/")
def main():
    url = 'https://solstice.applauncher.com/external/contacts.json'
    response = requests.get(url)
    data = response.json()

    return render_template('index.html', data=data)


@app.route("/contact", methods=['POST'])
def contact():
    if request.method == "POST":
        detailsURL = request.form.get("details")
        empId = int(request.form.get("id"))

        detailsResponse = requests.get(detailsURL)
        details = detailsResponse.json()

        contactURL = 'https://solstice.applauncher.com/external/contacts.json'
        contactResponse = requests.get(contactURL)
        allContacts = contactResponse.json()

        for con in allContacts:
            if con["employeeId"] == empId:
                contact = con

        birthday = datetime.fromtimestamp(
            int(contact['birthdate'])).strftime('%B %d, %Y')

        return render_template('contact.html', details=details,
                               contact=contact, birthday=birthday)


@app.route("/sorry")
def sorry():
    return render_template('sorry.html')


if __name__ == '__main__':
    app.run()
