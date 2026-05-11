
from flask import Flask,render_template,request,redirect
from datetime import datetime
app = Flask(__name__)


@app.route("/my-name/<age>")
def my_name(age):
    address = request.args.get("address")
    return render_template("my-name.html",user_age=age,address=address)

@app.route("/current")
def current():
    return f"Now is {datetime.now()}"

@app.route("/")
def mypage():
    return redirect("/product")

@app.route("/greeting/<name>")
def greet(name):
    h_value = request.args.get("height")
    return render_template("greet.html",user_name=name,height=h_value)

products = []

@app.route("/product",methods=["GET","POST"])
def create_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        products.append({"name": name, "price": price})
        print(products)
        return redirect("/product_list")

    return render_template("product.html")

@app.route("/product_list")
def list_products():
    return render_template("product_list.html", product_list=products)

@app.route("/product/<index>",methods=["POST"])
def delete_product(index):
    if index != "" and index.isdigit():
        index = int(index)
    else:
        index = 0

    if index >= 0 and index < len(products):
        products.pop(index)
    return redirect("/product_list")


@app.route("/product/edit/<index>",methods=["GET","POST"])
def edit_product(index):
    if index != "" and index.isdigit():
        index = int(index)
    else:
        index = 0

    current = products[index]
    if request.method == "GET":
        return render_template("product_edit.html", current=current, index = index)
    else:
        current['name']= request.form.get("name")
        current['price'] = request.form.get("price")

        products[index] = current
        return redirect("/product_list")


if __name__ == "__main__":
    app.run(debug=True)