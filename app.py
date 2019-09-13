from flask import Flask, render_template, request
import requests
import json
apikey = "LIVDSRZULELA" # API Key
defaultQ = "exciting" # Default GIF search
lmt = 10 # GIF Limit

app = Flask(__name__, static_url_path='')

@app.route('/')
def index():
    q = request.args.get('search')
    if not q:
        q = defaultQ
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (q, apikey, lmt))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        title = q + " GIFs | Graphics Interchange Format Search"
        return render_template(
            'index.html',
            gifs=gifs["results"],
            title=title
            )
    else:
        return "Request error code: " + r.status_code

if __name__ == '__main__':
    app.run(debug=True)
