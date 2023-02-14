from flask import Flask,render_template,app
app=Flask(__name__)

@app.route('/')
def Hello_World():
    print('Hello World From GitHub')
    first='Ganesh'
    last='Ingle'
    return render_template('hello.html',first_name=first,last_name=last)


if __name__=='__main__':
    app.run(host='65.0.105.14',port=5000)
    