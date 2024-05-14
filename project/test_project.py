from project import all_articles, news, answer, first_message
import pytest
from newsapi.newsapi_exception import NewsAPIException

#add credentials to test
# def test_all_articles():
#     assert len(all_articles('tesla', 1)) == 5
#     assert not len(all_articles('fwfds', 1))

def test_all_articles():
    with pytest.raises(NewsAPIException):
        all_articles('tesla', 1)


def test_news():
    with pytest.raises(AttributeError):
        news('daad')

def test_answer():
    with pytest.raises(AttributeError):
        answer('daad')

def test_first_message():
    with pytest.raises(AttributeError):
        first_message('daad')
