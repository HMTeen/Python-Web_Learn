
import requests
res = requests.get("http://www.chinaunicom.com.cn/api/article/NewsByIndex/2/2021/11/news")
data_list = res.json()
print(data_list)