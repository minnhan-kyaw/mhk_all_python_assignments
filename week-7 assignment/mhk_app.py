from flask import Flask, render_template, request, redirect, url_for
import mhk_product_service as service

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for('list_products'))

@app.route("/product_list")
def list_products():
    items = service.get_all_products()
    return render_template("product_list.html", products=items)

@app.route("/product", methods=["GET", "POST"])
def create_product():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        if not name or not price or float(price) < 0:
            return render_template("product.html", error="Invalid input!")
        service.add_product(name, price)
        return redirect(url_for('list_products'))
    return render_template("product.html")

@app.route("/product/edit/<int:index>", methods=["GET", "POST"])
def edit_product(index):
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        service.update_product(index, name, price)
        return redirect(url_for('list_products'))
    
    current = service.get_product_by_index(index)
    return render_template("product_edit.html", current=current, index=index)

@app.route("/product/delete/<int:index>", methods=["POST"])
def delete_product(index):
    service.delete_product(index)
    return redirect(url_for('list_products'))

if __name__ == "__main__":
    app.run(debug=True)

