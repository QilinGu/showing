__author__ = 'wuwy'

#推送内容的最低评分
rating = 8

#推送内容的最低评分人数
ratings_count = 2000

#捕捉内容的时间间隔 (crontab)
interval = '* * */1 * *'

#服务器邮箱
s_email = 'moka20477@aliyun.com'
s_password = ''

#邮件内容
title = "最新电影信息，{0}部{1}分以上影片"

content = '''
        最新一周的院线电影信息：
        筛选条件：评分{0}以上，评分人数{1}以上
          '''

content_2 = '''
        电影名：{0}
        主演：{1}
        导演：{2}
        国家：{3}
        评分：{4}
        参与人数：{5}
        链接：{6}


'''

#推送目标邮箱
c_email = 'moka20477@gmail.com'

#上映城市
city = 'beijing'