from flask import Flask, render_template, request
import requests
import json
apikey = "LIVDSRZULELA" # API Key
lmt = 10 # GIF Limit

app = Flask(__name__)

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract the query term from url using request.args.get()

    # TODO: Make 'params' dictionary containing:
    # a) the query term, 'q'
    # b) your API key, 'key'
    # c) how many GIFs to return, 'limit'

    # TODO: Make an API call to Tenor using the 'requests' library. For
    # reference on how to use Tenor, see:
    # https://tenor.com/gifapi/documentation

    # TODO: Use the '.json()' function to get the JSON of the returned response
    # object

    # TODO: Using dictionary notation, get the 'results' field of the JSON,
    # which contains the GIFs as a list

    # TODO: Render the 'index.html' template, passing the list of gifs as a
    # named parameter called 'gifs'


    # set the apikey and limit

    q = request.args.get('search')
    r = requests.get(
        "https://api.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (q, apikey, lmt))

    if r.status_code == 200:
        gifs = json.loads(r.content)
        return render_template(
            'index.html',
            gifs=gifs["results"]
            )
    else:
        return "Request error code: " + r.status_code

if __name__ == '__main__':
    app.run(debug=True)
