# agent.py

import re

from tools import (
    get_order_status,
    check_return_eligibility,
    search_products,
    get_recommendations
)

from memory import (
    add_memory,
    get_memory
)


def agent_response(user_message):

    message = user_message.lower()

    # Find order ID
    order_match = re.search(r"ord\d+", message)

    order_id = None

    if order_match:
        order_id = order_match.group().upper()


    # ORDER STATUS
    if "status" in message or \
       "where is my order" in message or \
       "track" in message:

        if order_id:

            response = get_order_status(order_id)

        else:

            response = "Please provide your order ID."

        add_memory(user_message, response)

        return response


    # RETURN
    if "return" in message:

        if order_id:

            response = check_return_eligibility(order_id)

        else:

            response = "Please provide your order ID."

        add_memory(user_message, response)

        return response


    # PRODUCT SEARCH
    if "shoe" in message:

        response = search_products("Shoes")

        add_memory(user_message, response)

        return response


    if "watch" in message:

        response = search_products("Electronics")

        add_memory(user_message, response)

        return response


    if "earbuds" in message:

        response = search_products("Earbuds")

        add_memory(user_message, response)

        return response


    # RECOMMENDATION
    if "recommend" in message or \
       "suggest" in message:

        if "shoe" in message:

            response = get_recommendations("Shoes")

        elif "electronic" in message or \
             "watch" in message:

            response = get_recommendations("Electronics")

        else:

            response = "What type of product would you like?"

        add_memory(user_message, response)

        return response


    # FAQ
    if "shipping" in message:

        response = (
            "Standard shipping usually takes "
            "3 to 5 business days."
        )

        add_memory(user_message, response)

        return response


    if "payment" in message:

        response = (
            "We support online payment methods "
            "such as UPI, cards and net banking."
        )

        add_memory(user_message, response)

        return response


    # MEMORY
    if "previous" in message or \
       "earlier" in message or \
       "remember" in message:

        return get_memory()


    response = (
        "I'm your E-Commerce Support Agent. "
        "I can help with order tracking, "
        "returns, products and recommendations."
    )

    add_memory(user_message, response)

    return response
