#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
File: get_data.py
Author: cwk
Date: 3/29/18
"""

import time
import requests
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


city_list = {'深圳', '西安', '北京', '上海'}
job_list = {'c', 'c++', 'python', 'java', '数据挖掘'}
file_name_base = '%s_%s.csv'
base_url = 'https://www.lagou.com/jobs/%s.html'
sql_conn = MySQLdb.connect(host='localhost', user='root', db='test', passwd='h', charset='utf8')
sql_curs = sql_conn.cursor()
sql_insert = """
             INSERT INTO ad_info (companyName, positionfullName, positionName, city, positionAdvantage, salarymin, salarymax, workYear, request_url, stime, etime)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, '2018-03-29 00:00:00', '2018-06-30 23:59:59')
"""


def lagou(page, position, city):
    """

    :param page:
    :param position:
    :return:
    """

    headers = {
        'Referer': 'https://www.lagou.com/jobs/list_'+position+'?city=' + city + '&cl=false&fromSearch=true&labelWords=&suginput=',
        'Origin': 'https://www.lagou.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Cookie': 'JSESSIONID=ABAAABAAAGFABEFE8A2337F3BAF09DBCC0A8594ED74C6C0; user_trace_token=20180122215242-849e2a04-ff7b-11e7-a5c6-5254005c3644; LGUID=20180122215242-849e3549-ff7b-11e7-a5c6-5254005c3644; index_location_city=%E5%8C%97%E4%BA%AC; _gat=1; TG-TRACK-CODE=index_navigation; _gid=GA1.2.1188502030.1516629163; _ga=GA1.2.667506246.1516629163; LGSID=20180122215242-849e3278-ff7b-11e7-a5c6-5254005c3644; LGRID=20180122230310-5c6292b3-ff85-11e7-a5d5-5254005c3644; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516629163,1516629182; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1516633389; SEARCH_ID=8d3793ec834f4b0e8e680572b83eb968'
    }
    dates = {
        'first': 'true',
        'pn': page,
        'kd': position
    }
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=' + city + '&needAddtionalResult=false&isSchoolJob=0'
    resp = requests.post(url, data=dates, headers=headers)
    print(resp.content.decode('utf-8'))
    result = resp.json()['content']['positionResult']['result']
    # file_name = file_name_base % (city, position)
    # fw = open(file_name, 'w')
    # for ob in result:
    #     out_str = ''
    #     companyFullName = ob['companyFullName']
    #     out_str = companyFullName + ','
    #     positionName = ob['positionName']
    #     out_str += (positionName + ',')
    #     city = ob['city']
    #     out_str += (city + ',')
    #     positionAdvantage = ob['positionAdvantage']
    #     out_str += (positionAdvantage + ',')
    #     salary = ob['salary']
    #     out_str += (salary + ',')
    #     workYear = ob['workYear']
    #     out_str += (workYear + ',')
    #     companyLabelList = '@'.join(ob['companyLabelList'])
    #     out_str += (companyLabelList + ',')
    #     positionId = ob['positionId']
    #     request_url = base_url % positionId
    #     out_str += (request_url + '\n')
    #     print out_str
    #     fw.write(out_str)
    # fw.close()


def main():
    for city in city_list:
        for job in job_list:
            print city, job
            lagou(1, job, city)
            time.sleep(1)


if __name__ == '__main__':
    main()
