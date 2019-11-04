"""
招标网爬虫主模块
功能：
整合四个子功能模块
"""
from .mode.sqlmanager import SQLManager
from .spider import Spider
from .mparser import parser_run
from .myemail import mail_to_user
import time


def zbprint(args):
    print("[ ZBSPIDER: ] " + args)


class ZBSpider(object):
    """
    主程序类
    """

    def __init__(self, config):
        self.config = config
        self.sql = SQLManager(self.config.DATABASE)
        self.spider = Spider(self.config.URL, **self.config.SPIDER)
        zbprint("程序初始化")

    def run(self):
        # 查询最后一个数据
        last_one_title = self.sql.get_last_one_title()
        zbprint("已提取数据")
        # 建立results列表
        results = []
        page = 1
        while True:
            #if page == 505:
            #    zbprint("该标的存在问题，换一个查询标的")
            #    last_one_title = self.sql.get_last_one_title("1")
            #    page = 1
            # 检查数据是否在列表中存在
            if last_one_title in results:
                # 若存在： 按顺序分割列表，将顺序后的数据存入数据库
                zbprint("在第%d页中存在已经提取的数据" % (page))
                # print("存在")
                # print(results)
                index = results.index(last_one_title)
                results = results[:(index - 1)]
                # print(results)
                break
            else:
                # 若不存在提取不存在的网页进行分析，然后在查找下一页
                zbprint("在第%d页中不存在已经提取的数据" % (page))
                # print("不存在%d" % (page))
                # 爬取网页
                html_doc = self.spider.get(page)
                # 分析网页，获得结果
                results += parser_run(html_doc)
                # print(results)
                page = page + 1
                time.sleep(120)
        mail_to_user(self.config.EMAIL, results)
        zbprint("提取的数据已发送到相关邮箱")
        # 若不存在： 获取下一页数据,补全列表，直到存在
        for result in reversed(results):
            # print(result)
            self.sql.insert(result)
        zbprint("数据存储完毕")
        # 关闭数据库
        self.sql.close()
        zbprint("程序已完成，关闭。")
