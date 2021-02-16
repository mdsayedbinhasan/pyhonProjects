from flask import Flask, render_template, request, url_for
import re

email_regex = re.compile(r'[a-z0-9]+[@]\w+[.]\w{2,3}')
phone_num = re.compile(r'[+][8801][0-9]{1,12}')
url_https_regex = re.compile(r'https?://www\.?\w+\.\w+')
url_regex = re.compile(r'http?:www\.?\w+\.\w+')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['GET', 'POST'])
def process():
    if request.method == 'POST':
        choice = request.form['taskoption']
        if choice == 'email':
            rawtext = request.form['rawtext']
            results = email_regex.findall(rawtext)
            num_of_results = len(results)

        elif choice == 'phone':
            rawtext = request.form['rawtext']
            results = phone_num.findall(rawtext)
            num_of_results = len(results)

        elif choice == 'url_https':
            rawtext = request.form['rawtext']
            results = url_https_regex.findall(rawtext)
            num_of_results = len(results)

        elif choice == 'url':
            rawtext = request.form['rawtext']
            results = url_regex.findall(rawtext)
            num_of_results = len(results)
    return render_template('index.html', results=results, num_of_results=num_of_results)
    

if __name__ == '__main__':
    app.run(debug=True)