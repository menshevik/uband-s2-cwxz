from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/<string:student_number>/index')
def show_index(student_number):
	if student_number == "A10552" or student_number == "A10294":
		return render_template(str(student_number) + '/index.html')
	else:
		return "Page not found"

if __name__ == '__main__':
    app.run(debug = True)