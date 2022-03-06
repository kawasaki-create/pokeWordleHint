import requests
from bs4 import BeautifulSoup


def scraping():
    # ポケモン図鑑のURLを変数に代入
    URL = 'https://yakkun.com/swsh/zukan/'

    # URLの取得
    results = requests.get(URL)
    results.encoding = 'EUC-JP'

    # HTML、XMLの要素をパースする
    data1 = BeautifulSoup(results.text, 'html.parser')

    # クラスを指定し、見出しを取得する
    data2 = data1.find(class_="pokemon_list")

    # それぞれのメニューを抽出
    rows = data2.find_all("a")

    # 配列の値をfor文とprint文で出力、rowsの定義変更
    pokeArray = []
    for row in rows:
        if len(row.getText()) == 5:
            pokeArray.append(row.getText())

    return pokeArray