from flask import Flask,render_template,request
from datetime import datetime
app = Flask(__name__)


@app.route("/my-name/<age>")
def my_name(age):
    address = request.args.get("address")
    return render_template("my-name.html",user_age=age,address=address)

@app.route("/current")
def current():
    return f"Now is {datetime.now()}"

@app.route("/greeting/<name>")
def greet(name):
    age = request.args.get("heigh")
    return render_template("greet.html",user_name=name,heigh="")


products = []
@app.route("/product", methods=["GET","POST"])
def product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        products.append({"name":name, "price":price})
        print(products)
    return render_template("product.html")

if __name__ == "__main__":
    app.run(debug=True)