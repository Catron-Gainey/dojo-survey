from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'root'

@app.route('/')
def main_page():
    return render_template('main_page.html') 

@app.route('/process', methods=['POST'])
def process_form():
    print(request.form)
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['favorite'] = request.form['favorite']
    session['message'] = request.form['message']    
    return redirect('/show')

@app.route('/show')
def show_data_page():
    return render_template('data_page.html')



if __name__ == "__main__":
    app.run(debug=True)