import unittest
from ccgpspider.urlencode import get_url


class UrlencodeTestCase(unittest.TestCase):
    """
    测试urlencode.py
    """

    def test_get_url(self):
        """
        测试get_url函数
        """
        url = "https://www.mysite.com/"
        parameters = {
            "sortField": "人工智能",
            "pageIndex": 3,
            "pageSize": 20,
        }
        result = get_url(url, parameters)
        correct_result = "https://www.mysite.com/?sortField=%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD&pageIndex=3&pageSize=20"
        self.assertEqual(result, correct_result)
