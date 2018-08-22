from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        username = request.form['username']
        with open('message.txt', 'a') as f:
            f.write(username + '\n')
            print(username)
        message = request.form['message']
        with open('message.txt', 'a') as f:
            f.write(message + '\n')
            print(message)
    return render_template('board.html')

@app.route('/', methods = ['POST'])
def signin():
    username = request.form['username']
    message = request.form['message']
    return render_template('signin-ok.html', username = username)


if __name__ == '__main__':
    app.run(debug=True)

