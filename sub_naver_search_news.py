#!__*__coding:utf-8__*__
# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import pandas as pd
import html
import sub_naver_search_news_main_content as naver_news

# 보통 공개 API 를 사용할 때 각각 고유 키를 발급을 해줌
CLIENT_ID = "L6nXKqU10Xr1MZ2G6KOl"
CLIENT_SECRET = "GCSWcVuovx"

NUMBER_OF_SEARCH = 100

# openAPI로 네이버 뉴스 가져오기
def search_news_from_naver(keyword, start_idx, display=10): #맛집, 100
    global CLIENT_ID, CLIENT_SECRET
    encText = urllib.parse.quote(keyword)
    url = "https://openapi.naver.com/v1/search/news?query=" + encText # json 결과
    url = url + "&start=" + str(start_idx)
    url = url + "&display=" + str(display)

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        return result
    else:
        print("Error Code:" + rescode)


# openAPI로 네이버 뉴스 가져오기 메인
def search_news_main(keyword):
    global NUMBER_OF_SEARCH

    df = pd.DataFrame({}, columns=["title", "link", "originallink", "description", "pubDate"])
    for start_idx in range(1, NUMBER_OF_SEARCH, 100):
        result = search_news_from_naver(keyword, start_idx)
        result2 = json.loads(result, encoding="utf-8")
        for one_item in result2["items"]:
            print(naver_news.get_title(one_item["title"]))

            r2 = {
                "title": naver_news.get_title(one_item["title"]),
                "link": html.unescape(one_item["link"]),
                "originallink": html.unescape(one_item["originallink"]),
                "description": naver_news.get_title(one_item["description"]),
                "pubDate": one_item["pubDate"],
            }

            df = df.append(r2, ignore_index=True)

    output_filename = keyword + "_뉴스검색결과_with내용.xlsx"
    df.to_excel(output_filename)

if __name__ == "__main__":
    search_news_main("방탄소년단")