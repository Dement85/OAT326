import requests

def test_status_code_200():
    date = "2023-10-10"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  200 <= result < 400

def test_status_code_200():
    date = "2023-02-30"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  400 <= result < 500

def test_status_code_200():
    date = "20232-10-10"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  400 <= result < 500

def test_status_code_200():
    date = "2025-10-10"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  400 <= result < 500

def test_status_code_200():
    date = "2024-01-32"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  400 <= result < 500

def test_status_code_200():
    date = "2023-13-30"
    url = f"https://api.nasa.gov/planetary/apod?api_key=jUsYymkf0vV58o8oJUSsls07GhfVpBW1HmURrBla&date={date}"
    response = requests.request(url=url, method='GET')
    result = response.status_code
    assert  400 <= result < 500