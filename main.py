from flask import Flask, render_template

ismapp = Flask(__name__)

@ismapp.route('/')
def root():
    return render_template('root.html')

if __name__ == "__main__":
    ismapp.run(debug=True)