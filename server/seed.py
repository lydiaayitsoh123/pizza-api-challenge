from server.app import db, create_app
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Mario's Pizza", address="123 Cheese St")
    r2 = Restaurant(name="Luigi's Pizza", address="456 Tomato Ave")
    db.session.add_all([r1, r2])

    p1 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
    p2 = Pizza(name="Veggie", ingredients="Dough, Tomato Sauce, Cheese, Peppers, Olives")
    db.session.add_all([p1, p2])

    rp1 = RestaurantPizza(price=10, restaurant=r1, pizza=p1)
    rp2 = RestaurantPizza(price=12, restaurant=r1, pizza=p2)
    db.session.add_all([rp1, rp2])

    db.session.commit()
