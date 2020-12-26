from flask import Flask, make_response, request
import requests

app = Flask(__name__)

SEARCH = 'http://openlibrary.org/search.json'
COVERS = 'http://covers.openlibrary.org/b/id/'

def cover_image(title):
    r = requests.get(SEARCH, params={'q': title})
    response = r.json()
    if response['num_found'] < 1:
        return ''

    for doc in response['docs']:
        if 'cover_i' not in doc:
            continue
        cover = doc['cover_i']
        return f'{COVERS}{cover}-L.jpg'

    return ''


@app.route('/')
def index():
    if 'q' in request.args:
        img_url = cover_image(request.args.get('q'))
        if not img_url:
            return ''

        data = requests.get(img_url)
        resp = make_response(data.content)
        resp.headers.set('Content-Type', 'image/jpeg')
        return resp

    return ''
