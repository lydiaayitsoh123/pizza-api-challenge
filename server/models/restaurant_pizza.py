from server import db
from sqlalchemy import CheckConstraint

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizzas.id'), nullable=False)

    
    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price'),
    )

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'pizza_id': self.pizza_id,
            'restaurant_id': self.restaurant_id,
            'pizza': self.pizza.to_dict(),
            'restaurant': self.restaurant.to_dict()
        }