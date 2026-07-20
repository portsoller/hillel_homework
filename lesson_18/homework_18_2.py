import requests

# Part 1
with open('example.jpg', 'rb') as file:
    files = {'image': file}
    response = requests.post('http://127.0.0.1:8080/upload', files=files)
    data = response.json()

# Part 2
image_url = data['image_url'].replace('uploads', 'image')
headers = {'Content-Type': 'text'}
response = requests.get(image_url, headers=headers)
if response.status_code == 200:
    print('Отримано дані:', image_url)
else:
    print('Помилка. Статус-код:', response.status_code)

# Part 3
response = requests.delete(image_url.replace('image', 'delete'))
if response.status_code == 200:
    print('Дані успішно видалено')
else:
    print('Помилка. Статус-код:', response.status_code)