# **Dynamic-parsing-IP**

> 间隔一段时间会判断一次ip变化情况 仅适用于阿里云购买的域名

## 项目说明

* main.py 程序入口
* get_ip.py 获取当前的公网IP
* parser.py 为云解析添加或更新记录

* config.json 配置文件
  * conn_args
    * accessKeyId 阿里云中设置的 [AcessKey](https://usercenter.console.aliyun.com/#/manage/ak)
    * accessSecret 与上面对应的 Secret
    * delay 设置每次解析ip的时间间隔
  * record_args
    * domainName 设置域名
    * RRKeyWord 设置主机记录

