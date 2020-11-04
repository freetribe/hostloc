import requests
import time #不延时可以去掉
import re
import os

username = os.environ["USERNAME"]  # 论坛账户
password = os.environ["PASSWORD"]  # 论坛密码
login_url = 'https://www.hostloc.com/member.php?mod=logging&action=login&loginsubmit=yes&infloat=yes&lssubmit=yes&inajax=1'  # post登录接口
request = requests.post(login_url, {"username": username, 'password': password})  # 登录一次，获取request
cookie = request.cookies  # 获取request里的cookie
user_info = requests.get('https://www.hostloc.com/home.php?mod=spacecp&ac=credit', cookies=cookie).text  # 获取用户积分中心
Current_money = re.search(r'金钱: </em>(\d+).+?</li>', user_info).group(1)  # 积分中心使用re获取金钱
print("用户%s,你的金钱为%s" % (username, Current_money))  # 打印初始积分

for i in range(20359, 20370):
    request1 = requests.get('https://www.hostloc.com/space-uid-%s.html' % i, cookies=cookie)  # 访问循环id用户空间
    print(re.search(r'<title>(.+?)全球主机交流论坛', request1.text).group(1))  # 获取访问的空间标题
    time.sleep(4)
    new_money = requests.get('https://www.hostloc.com/home.php?mod=spacecp&ac=credit', cookies=cookie).text  # 重新获取个人积分中心
    new_money = re.search(r'金钱: </em>(\d+).+?</li>', new_money).group(1)  # 获取金钱
    print("金钱为%s" % new_money)  # 打印金钱
