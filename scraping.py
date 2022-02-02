import requests
from bs4 import BeautifulSoup


def scraping():
    # くら寿司メニューのURLを変数に代入
    URL = 'https://www.kurasushi.co.jp/menu/?area=area0'

    # URLの取得
    results = requests.get(URL)

    # HTML、XMLの要素をパースする
    data1 = BeautifulSoup(results.text, 'html.parser')

    # クラスを指定し、見出しを取得する
    data2 = data1.find(id="menu02")
    data3 = data1.find(id="menu03")
    data4 = data1.find(id="menu04")
    data7 = data1.find(id="menu07")
    data8 = data1.find(id="menu08")

    # それぞれのメニューを抽出
    rows = data2.find_all("h4")

    # 配列の値をfor文とprint文で出力、rowsの定義変更
    rows2 = []
    for row in rows:
        print(row.getText())
        rows2.append(row.getText())
    print('-------------------')

    rows = data3.find_all("h4")
    rows3 = []
    for row in rows:
        print(row.getText())
        rows3.append(row.getText())
    print('-------------------')

    rows = data4.find_all("h4")
    rows4 = []
    for row in rows:
        print(row.getText())
        rows4.append(row.getText())
    print('-------------------')

    rows = data7.find_all("h4")
    rows7 = []
    for row in rows:
        print(row.getText())
        rows7.append(row.getText())
    print('-------------------')

    rows = data8.find_all("h4")
    rows8 = []
    for row in rows:
        print(row.getText())
        rows8.append(row.getText())
    print('-------------------')

    sumRows = rows2 + rows3 + rows4 + rows7 + rows8

    #予定：正規表現を外す

    return sumRows
    