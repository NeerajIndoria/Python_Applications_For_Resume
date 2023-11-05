import requests

# URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple"

# """
parameters = {
    "amount": 20,
    "category": 9,
    "difficulty": "easy",
    "type": "multiple",
}
# """
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
# response = requests.get(url=URL)
question_data = response.json()["results"]
