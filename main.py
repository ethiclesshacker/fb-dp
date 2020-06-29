import requests
from flask import *
from bs4 import BeautifulSoup
import urllib.parse

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    imgLink = ""
    

    if(request.method == "POST"):
        print(request.form)
        URL = request.form["link"]
        page = requests.get(URL)
        if(page.status_code == 200):
            html = page.text
            soup = BeautifulSoup(html, "html.parser")
            meta = soup.find('meta', {'property': 'og:image'})
            imgLink = meta['content']

            imgLink = urllib.parse.unquote(imgLink).encode(
                'latin1').decode('unicode_escape')

    return render_template("index.html", imgLink=imgLink)


if __name__ == "__main__":
    app.run(debug=True)
