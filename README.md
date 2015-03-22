# 定期推送优秀热映电影

  经常遇到发现了好电影，刚刚准备订票，却发现电影已经下线了，后悔不已。。
  所以开发了一个这样的应用。
  
## 功能
  可配置指定间隔时间执行抓取`豆瓣电影`首页内容，筛选符合要求的影片（`最低评分`，`最低评分人数`），并将相关信息推送至制定邮箱中。


## 如何使用
  * 按需求配置 `config` 文件
  
    ```
      #推送内容的最低评分
      rating
      
      #推送内容的最低评分人数
      ratings_count
      
      #捕捉内容的时间间隔 (crontab)
      interval
      
      #服务器邮箱
      s_email 
      s_password
      
      #邮件内容
      title 
      
      content
      
      content_2
      
      #推送目标邮箱
      c_email
      
      #上映城市
      city
    ```
  * 在系统中添加计划任务，定期执行start.py
  
## 待开发
  * 在配置文件中配置计划任务，间隔时间等。
