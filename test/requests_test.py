import requests

files = {'file': open('test.txt', 'rb')}
headers = {
            "Content-Type": "multipart/form-data;charset=UTF-8"
          }
r = requests.post("http://httpbin.org/post",files=files,headers=headers)
print(r.text)


#设置超时时间,timeout 仅对连接过程有效
r = requests.get('http://github.com', timeout=1)

#设置访问代理
proxies = {
           "http": "http://10.10.1.10:3128",
           "https": "http://10.10.1.100:4444",
          }
r = requests.get('http://github.com', proxies=proxies)


r = requests.post('https://www.baidu.com/')      # post请求
r = requests.put('https://www.baidu.com/')       # put请求
r = requests.delete('https://www.baidu.com/')    # delete请求
r = requests.options('https://www.baidu.com/')   # options请求




r.url                             #打印输出URL
r.headers                         #以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
r.status_code                     #返回连接状态，200正常。
r.text                            #默认以unicode形式返回网页内容，也就是网页源码的字符串。
r.content                         #以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩。
r.json()                          #json数据转成字典并将其返回。
r.encoding                        #获取当前的编码
r.encoding = 'GBK'               #自定义编码,r.text返回的数据类型，写在r.text之前。
r.raise_for_status()              #失败请求抛出异常返回






