from flask import Flask, render_template, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
    page_title = "Homepage"

    cities = ["Wien", "Prag", "Bratislava", "London"]

    return render_template("index.html", page_title=page_title, cities=cities)


@app.route("/impressum")
def impressum():
    return render_template("impressum.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "Get":
        user_name = request.cookies.get("user_name")
        return render_template("success.html", name= user_name)
    else:

    contact_name = request.form.get("contact-name")
    contact_email = request.form.get("contact-email")
    contact_text = request.form.get("contact-message")

    print(contact_name)
    print(contact_email)
    print(contact_text)

    response = make_response(render_template(render_template("success.html", name="contact-name", mail="contact-email",user_text="contact-message")))

    return response


if __name__ == "__main__":
    #app.debug = False
    app.run()
