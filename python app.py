from flask import Flask, request, render_template
import datetime
import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
try:
    cursor.execute('create table message (id integar primary key, username varchar(64), message text)')
except Exception as e:
    print('数据表已存在')

app = Flask(__name__)


@app.route('/', methods=['GET'])
def sign():
    return render_template('board.html')


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
    username = request.form['username']
    message = request.form['message']
    #check_same_thread这个设置为False，即可允许sqlite被多个线程同时访问 （未修改实现）
    if(username and message):
        cursor.execute('insert into message (username, message) values (?, ?)', [username, message])
        conn.commit()

    return render_template('sign.html',username=username, message=message)

#应该还有一个实现把数据库链接网页输出的函数，也没能实现



if __name__ == '__main__':
    app.run(debug=True)
