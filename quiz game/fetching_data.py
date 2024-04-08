import requests

CATEGORIES = {
    "GeneralKnowledge": 9,
    "Science": 17,
    "History": 23,
}


def fetch_questions(category, number):
    response = requests.get(f"https://opentdb.com/api.php?"
                            f"category={CATEGORIES[category]}&"
                            f"amount={number}&"
                            f"type=multiple",
                            )
    return response.json()["results"]
