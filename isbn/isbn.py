#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import requests
try:
    #result  = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784043636037")
    #result  = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784873117782")

    result  = requests.get("https://www.googleapis.com/books/v1/volumes?q=isbn:9784873119861")

    #辞書型変数
    """
    test = { "title":"あああ",
             "price":2000,
             "data":[]
             }
    test["title"]
    """

except:
    print("通信エラー")
else:

    #返却されたJSONを辞書型に変換する。
    data    = result.json()

    #print(data)

    #print(data["items"][0]["volumeInfo"])
    #書籍情報を手に入れる。
    print(data["items"][0]["volumeInfo"]["title"])
    print(data["items"][0]["volumeInfo"]["publishedDate"])
    print(data["items"][0]["volumeInfo"]["authors"])
    print(data["items"][0]["volumeInfo"]["description"])
    print(data["items"][0]["volumeInfo"]["imageLinks"]["thumbnail"])
    print(data["items"][0]["volumeInfo"]["infoLink"])


