#!__*__coding:utf-8__*__
import os
import sys
import sub_naver_search_blog as naver_blog
import sub_naver_search_news as naver_news


class crawler:
    def do_blog(self):
        """
        네이버 블로그에서 해당 키워드를 검색합니다.
        """
        keyword = input("검색 키워드를 입력해 주십시오:")
        naver_blog.search_blog_main(keyword)

    def do_news(self):
        """
        네이버 뉴스에서 해당 키워드를 검색합니다.
        """
        keyword = input("검색 키워드를 입력해 주십시오:")
        naver_news.search_news_main(keyword)

# 모듈이 아니라 자기 자신을 실행할 경우 동작 C 언어의 main 느낌
if __name__ == "__main__":

    print("모듈이지만 스스로 동작, 유닛(모듈 테스트)")
    test = crawler()
    test.do_blog()
    test.do_news()
    print("종료")
