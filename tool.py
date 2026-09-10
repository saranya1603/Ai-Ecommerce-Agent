# tools.py

orders = {
    "ORD1023": {
        "customer": "Saranya",
        "item": "Running Shoes",
        "status": "Out for Delivery",
        "expected": "Today by 7 PM",
        "delivered": False
    },
    "ORD1024": {
        "customer": "Rahul",
        "item": "Smart Watch",
        "status": "Delivered",
        "expected": "Delivered yesterday",
        "delivered": True
    }
}

products = [
    {
        "id": "P101",
        "name": "Running Shoes",
        "category": "Shoes",
        "price": 1999
    },
    {
        "id": "P102",
        "name": "Sports Shoes",
        "category": "Shoes",
        "price": 2499
    },
    {
        "id": "P103",
        "name": "Smart Watch",
        "category": "Electronics",
        "price": 2999
    },
    {
        "id": "P104",
        "name": "Wireless Earbuds",
        "category": "Electronics",
        "price": 1499
    }
]


# Tool 1 - Order Status
def get_order_status(order_id):

    if order_id in orders:
        order = orders[order_id]

        return (
            f"Order {order_id} is {order['status']}. "
            f"Expected: {order['expected']}."
        )

    return "Sorry, I could not find that order."


# Tool 2 - Return Eligibility
def check_return_eligibility(order_id):

    if order_id not in orders:
        return "Order not found."

    order = orders[order_id]

    if order["delivered"]:
        return (
            f"The {order['item']} can be returned "
            f"within 7 days of delivery."
        )

    return "The item can be returned after it is delivered."


# Tool 3 - Product Search
def search_products(keyword):

    results = []

    for product in products:

        if keyword.lower() in product["name"].lower() \
                or keyword.lower() in product["category"].lower():

            results.append(product)

    if len(results) == 0:
        return "No products found."

    answer = "Products found:\n"

    for product in results:

        answer += (
            f"{product['name']} - "
            f"₹{product['price']}\n"
        )

    return answer


# Tool 4 - Recommendations
def get_recommendations(category):

    recommendations = []

    for product in products:

        if product["category"].lower() == category.lower():

            recommendations.append(product)

    if len(recommendations) == 0:
        return "No recommendations available."

    answer = "Recommended products:\n"

    for product in recommendations:

        answer += (
            f"{product['name']} - "
            f"₹{product['price']}\n"
        )

    return answer
