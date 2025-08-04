# Simple in-memory storage for restaurant orders
RESTAURANT_MENU = {
    "burger": {"name": "Cheeseburger", "price": 6.99,
               "description": "Juicy beef patty with cheese, lettuce, and tomato on a fresh bun", "quantity": 1},
    "pizza": {"name": "Margherita Pizza", "price": 11.50,
              "description": "Classic pizza with fresh mozzarella, basil, and tomato sauce", "quantity": 1},
    "fries": {"name": "French Fries", "price": 2.99,
              "description": "Crispy golden fries with a touch of salt", "quantity": 1},
    "salad": {"name": "Caesar Salad", "price": 5.75,
              "description": "Fresh romaine lettuce with Caesar dressing and croutons", "quantity": 1},
    "soda": {"name": "Soft Drink", "price": 1.50,
             "description": "Choice of cola, lemon-lime, or orange soda", "quantity": 1},
    "wings": {"name": "Chicken Wings", "price": 8.99,
              "description": "Spicy or BBQ wings served with ranch dip", "quantity": 6},
    "pasta": {"name": "Penne Alfredo", "price": 10.25,
              "description": "Creamy Alfredo sauce over penne pasta", "quantity": 1},
    "sandwich": {"name": "Club Sandwich", "price": 7.99,
                 "description": "Triple-decker sandwich with turkey, bacon, lettuce, and tomato", "quantity": 1},
    "icecream": {"name": "Vanilla Ice Cream", "price": 3.25,
                 "description": "Two scoops of classic vanilla ice cream", "quantity": 1},
    "coffee": {"name": "Hot Coffee", "price": 2.50,
               "description": "Freshly brewed black coffee", "quantity": 1}
}

ORDERS_DB = {"orders": {}, "next_id": 1}


def get_menu_item_info(item_name):
    item = RESTAURANT_MENU.get(item_name.lower())
    if item:
        return {
            "name": item["name"],
            "description": item["description"],
            "price": item["price"],
            "quantity": item["quantity"]
        }
    return {"error": f"Item '{item_name}' not found in the menu."}


def place_order(customer_name, item_name):
    item = RESTAURANT_MENU.get(item_name.lower())
    if not item:
        return {"error": f"Item '{item_name}' not available."}

    order_id = ORDERS_DB["next_id"]
    ORDERS_DB["next_id"] += 1

    order = {
        "id": order_id,
        "customer": customer_name,
        "item": item["name"],
        "quantity": item["quantity"],
        "total": item["price"],
        "status": "pending"
    }
    ORDERS_DB["orders"][order_id] = order

    return {
        "order_id": order_id,
        "message": f"Order {order_id} placed: {item['quantity']} {item['name']} for ${item['price']:.2f}",
        "total": item["price"],
        "quantity": item["quantity"]
    }


def lookup_order(order_id):
    order = ORDERS_DB["orders"].get(int(order_id))
    if order:
        return {
            "order_id": order_id,
            "customer": order["customer"],
            "item": order["item"],
            "quantity": order["quantity"],
            "total": order["total"],
            "status": order["status"]
        }
    return {"error": f"Order {order_id} not found."}


FUNCTION_MAP = {
    'get_menu_item_info': get_menu_item_info,
    'place_order': place_order,
    'lookup_order': lookup_order
}
