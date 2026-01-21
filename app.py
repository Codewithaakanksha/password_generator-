from flask import Flask, render_template, request, send_file
import random
import string

app = Flask(__name__)

def generate_password(length, upper, lower, digits, symbols):
    chars = ""
    if upper: chars += string.ascii_uppercase
    if lower: chars += string.ascii_lowercase
    if digits: chars += string.digits
    if symbols: chars += string.punctuation
    if not chars: return "Select at least one option"
    return ''.join(random.choice(chars) for _ in range(length))

@app.route("/", methods=["GET","POST"])
def index():
    password = ""
    if request.method == "POST":
        password = generate_password(
            int(request.form["length"]),
            request.form.get("upper"),
            request.form.get("lower"),
            request.form.get("digits"),
            request.form.get("symbols")
        )
    return render_template("index.html", password=password)

@app.route("/download/<pwd>")
def download(pwd):
    with open("password.txt","w") as f:
        f.write(pwd)
    return send_file("password.txt", as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
