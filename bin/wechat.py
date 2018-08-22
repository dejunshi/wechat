from wxpy import *
import time
import re
import os

def set_bot(groupname):
    bot = Bot(cache_path=True)
    company_group = bot.groups().search(groupname)[0]
    return company_group

def send_msg(someone,msg):
    someone.send(msg)

def news_data():
    msg_path1 = os.path.dirname(os.path.dirname(__file__))
    msg_path2 = "%s\\conf\\allocation.cfg" %(msg_path1)
    f1 = open(msg_path2,'r',encoding="utf-8")
    msg_data = f1.read()
    news_data = re.findall (r"news=(.*)",msg_data)
    f1.close()
    news = news_data[0]
    return news

def group_data():
    group_path1 = os.path.dirname(os.path.dirname(__file__))
    group_path2 = "%s\\conf\\allocation.cfg" %(group_path1)
    f2 = open(group_path2,'r',encoding="utf-8")
    g_data = f2.read()
    group_data = re.findall (r"group=(.*)",g_data)
    f2.close()
    group_d = group_data[0]
    group = group_d.split(',')
    return group

def time():
    time_path1 = os.path.dirname(os.path.dirname(__file__))
    time_path2 = "%s\\conf\\allocation.cfg" %(time_path1)
    f3 = open(time_path2,'r',encoding="utf-8")
    time_data = f3.read()
    t_data = re.findall (r"time=(.*)",time_data)
    f3.close()
    time = t_data[0]
    return time

def run():
    normal_msg = news_data()
    group = group_data()
    t = int(time())
    while True:
        for i in group:
            company_group=set_bot(i)
            send_msg(company_group,normal_msg)
    time.sleep(t)
    print("sleep....",current_time)

if __name__ == '__main__':
    run()