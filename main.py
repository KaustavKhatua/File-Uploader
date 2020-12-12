from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(uploaded_file.filename)

        # files = request.files.getlist('files[]')
        # for file in files:
        #     if file.filename != '':
        #         file.save(file.filename)

        return redirect('/')
    else:
        return render_template('main.html')

if __name__ == '__main__':
    app.run(debug = True, host= '192.168.0.101')