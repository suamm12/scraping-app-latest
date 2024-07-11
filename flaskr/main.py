from flaskr import app
from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form['url']
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    
    data = []
    rankBoxs = soup.find_all("div", attrs={"class": "box overflow-hidden p-0 mt-4"})

    for rankBox in rankBoxs:
        name = rankBox.find("a", attrs={"class": "underline"}).text
        rankNum = rankBox.find("strong", attrs={"class": "ranking-num"}).text
        overView = rankBox.find("h4", attrs={"class": "font-bold pr-12"}).text

        details = {
            "順位": rankNum,
            "名前": name,
            "概要": overView
        }
        data.append(details)
        

    return render_template('index.html', data=data)


if __name__ == '__main__':
    app.run(debug=True)
