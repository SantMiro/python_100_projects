import requests
import html


def get_data():
    response = requests.get(f'https://opentdb.com/api.php?amount=10&category=31&difficulty=easy&type=boolean')
    response.raise_for_status()
    data = response.json()

    questions = data['results']
    for question in questions:
        question['question'] = html.unescape(question['question'])
    return questions



