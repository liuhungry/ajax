from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template('ajax.html')

@app.route('/testdownload', methods=['GET'])
def testdownload():

    # f = open('C:\\Users\\ME\\Desktop\\test\\python-spyder\\Flask\\word.txt','r')
    f = open('C:\\Users\\ME\Desktop\\test\\python\\Flask\\ajax\\word.txt','r')
    s = f.read()
    print(s)
    f.close()
    return str(s)


if __name__ == "__main__":
    app.run(host='192.168.10.104',port='5000',debug=True)


