# 必要モジュールインポート
from flask import Flask, render_template, request, redirect
from numpy import result_type, void
from sqlalchemy import null
import scraping
import re

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/scraping', methods=["POST"])
def run_scraping():

    pokename1 = request.form['pokename1']
    pokename2 = request.form['pokename2']
    pokename3 = request.form['pokename3']
    pokename4 = request.form['pokename4']
    pokename5 = request.form['pokename5']

    all5 = scraping.scraping()

    result = []
    if pokename1 == "":
        result.append('名前を入力してください')
    else:
        for i in all5:
            if pokename1 in i:
                if pokename2 in i:
                    if pokename3 in i:
                        if pokename4 in i:
                            if pokename5 in i:
                                result.append(i)
                else:
                    if result == "":
                        return('そのポケモンはいません')
                    


    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run()