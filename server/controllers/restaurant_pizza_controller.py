from flask import Blueprint, request, jsonify
from server.app import db
from server.models.restaurant_pizza import RestaurantPizza
from server.models.pizza import Pizza
from server.models.restaurant import Restaurant

restaurant_pizza_bp = Blueprint('restaurant_pizzas', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    rp = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
    db.session.add(rp)
    db.session.commit()

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)

    return jsonify({
        "id": rp.id,
        "price": rp.price,
        "pizza_id": rp.pizza_id,
        "restaurant_id": rp.restaurant_id,
        "pizza": {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients},
        "restaurant": {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address}
    })
