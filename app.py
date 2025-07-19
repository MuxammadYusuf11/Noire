from flask import Flask, render_template, request, redirect, url_for, session
app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Для сессий (можешь заменить)

# Пример товаров (словарь: id → данные)
products = {
    1: {'name': 'Черная футболка', 'price': 20},
    2: {'name': 'Темные джинсы', 'price': 50},
    3: {'name': 'Кожаная куртка', 'price': 150},
}

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[product_id] = cart.get(product_id, 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    total = sum(products[pid]['price'] * qty for pid, qty in cart.items())
    return render_template('cart.html', cart=cart, products=products, total=total)

@app.route('/clear_cart')
def clear_cart():
    session.pop('cart', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
