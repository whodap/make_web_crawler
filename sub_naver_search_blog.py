#!__*__coding:utf-8__*__
# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import os
import sys
import urllib.request
import json
import pandas as pd
import html
import sub_naver_search_blog_main_content as naver_main

CLIENT_ID = "000"
CLIENT_SECRET = "000"

NUMBER_OF_SEARCH = 100

# openAPI로 네이버 블로그 가져오기
def search_blog_from_naver(keyword, start_idx, display=100): #맛집, 100\

    global CLIENT_ID, CLIENT_SECRET
    encText = urllib.parse.quote(keyword) # 인코딩
    url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
    url = url + "&start=" + str(start_idx) # 페이징
    url = url + "&display=" + str(display) # 한페이지에 몇개
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", CLIENT_ID)
    request.add_header("X-Naver-Client-Secret", CLIENT_SECRET)
    response = urllib.request.urlopen(request) # 실제 요청
    rescode = response.getcode() # 응답 코드 
    if (rescode == 200):
        response_body = response.read() # 데이터를 읽어온다(바디로부터)
        result = response_body.decode('utf-8')
        return result
    else:
        print("Error Code:" + rescode)


# openAPI로 네이버 블로그 가져오기 메인
def search_blog_main(keyword):
    global NUMBER_OF_SEARCH

    df = pd.DataFrame({}, columns=["title", "link", "description", "bloggername", "bloggerlink", "postdate"])

    for start_idx in range(1, NUMBER_OF_SEARCH, 100):
        result = search_blog_from_naver(keyword, start_idx)
        result2 = json.loads(result, encoding="utf-8")
        # { "items" : "123" }
        for one_item in result2["items"]:
            print(naver_main.get_title(one_item["title"]))

            my_url = html.unescape(one_item["link"])
            if my_url.find("blog.naver.com") >= 0:
                c = naver_main.get_main_content(my_url)
                c = naver_main.remove_extra_text(c)
            else:
                c = ""

            r2 = {
                "title": naver_main.get_title(one_item["title"]),
                "link": html.unescape(one_item["link"]),
                "description": naver_main.get_title(one_item["description"]),
                "bloggername": one_item["bloggername"],
                "bloggerlink": one_item["bloggerlink"],
                "postdate": one_item["postdate"],
                "full_content": c
            }
            df = df.append(r2, ignore_index=True)

    output_filename = keyword + "_블로그검색결과.xlsx"
    df.to_excel(output_filename)


if __name__ == "__main__":
    search_blog_main("방탄소년단")
