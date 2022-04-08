from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<rows>/<columns>/<color1>/<color2>')
def load_checkerboard(rows, columns, color1, color2):
    return render_template('index.html', rows=int(rows), columns=int(columns), color1=color1, color2=color2)

@app.errorhandler(404)
def no_response(error):
    return f"Sorry! To play, please enter your URL like the following: /rows/columns/color1/color2"

if __name__ == "__main__":
    app.run(debug=True)