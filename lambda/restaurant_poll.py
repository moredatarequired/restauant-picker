import json
import random

restaurants = [
    "Barney's Gourmet Hamburgers",
    "Curry Up Now",
    "Himalayan Flavours",
    "Holy Basil Pho",
    "Homeroom",
    "Jotmahal",
    "Koryo Sushi",
    "Little Star Pizza",
    "Monster Pho",
    "Namaste Pizza",
    "Ole Ole Burrito Express",
    "Plearn Thai",
    "Proposition Chicken",
    "Royale Rangoon",
    "Sliver Pizzeria",
    "Taqueria La Familia",
    "Taste of the Himalayas",
    "The Star on Grand",
    "Tuk Tuk Thai",
    "Vegan Mob",
    "Zachary's Chicago Pizza",
]


def make_restaurant_poll(num_poll_options=5):
    options = random.sample(restaurants, num_poll_options)

    poll_text = '/poll "@here Please pick tonight\'s restaurant!" '
    return poll_text + " ".join(f'"{s}"' for s in options)


def web_html(body_text):
    return f"<html><head></head><body><p>{body_text}</p></body></html>"


def handler(event, context):
    return {
        "statusCode": 200,
        "body": web_html(make_restaurant_poll()),
        "headers": {
            "Content-Type": "text/html",
        },
    }
