from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def write_message():
    if request.method == 'POST':
        message = request.form.get('message')
        if message:
            with open('messages.txt', 'a') as file:
                file.write(message + '\n')
            return 'Message written to file: ' + message
        else:
            return 'Message is empty'
    return render_template('index2.html')

if __name__ == '__main__':
    app.run(debug=False)
