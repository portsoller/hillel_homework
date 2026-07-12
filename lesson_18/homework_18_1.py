import requests

BASE_URL = "https://images-api.nasa.gov"

search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",  # пошуковий запит
    "media_type": "image",  # тільки зображення
    "page_size": 20  # щоб було з чого вибрати
}

response = requests.get(search_url, params=search_params)
if response.status_code == 200:
    data = response.json()
    items = data.get('collection', {}).get('items', [])
    for index, item in enumerate(items[:2], start=1):
        nasa_id = item.get('data')[0].get('nasa_id')
        filename = f'mars_photo{index}.jpg'
        asset_url = f"{BASE_URL}/asset/{nasa_id}"
        response2 = requests.get(asset_url)
        url_details = response2.json().get('collection').get('items')[0].get('href')
        image_data = requests.get(url_details)
        with open(filename, 'wb') as file:
            file.write(image_data.content)

else:
    print('Помилка запиту:', response.status_code)
