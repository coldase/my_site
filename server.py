from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def save_contact(mail, sub, text):
	with open("database.txt", "a") as file:
		file.write(f'Email: {mail}\nSubject: {sub}\nText: {text}\n\n')


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
	return render_template(f'{page_name}.html')

@app.route("/getpost", methods=["POST"])
def get_post():
	get_email = request.form["getemail"]	
	get_subject = request.form["getsubject"]	
	get_text = request.form["gettext"]	
	save_contact(get_email, get_subject, get_text)
	return redirect("/contact")
	
if __name__ == "__main__":
	app.run(debug=True)