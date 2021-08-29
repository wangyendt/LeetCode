#!/usr/bin/env python  
# -*- coding:utf-8 _*-
""" 
@author: wangye(Wayne) 
@license: Apache Licence 
@file: search_contest_result.py
@time: 2021/08/29
@contact: wang121ye@hotmail.com
@site:  
@software: PyCharm 

# code is far away from bugs.
"""

import requests
import urllib.parse
import pprint
import json


def find(country_, contest_type_, week_no_, name_):
    if country_ == '1':
        url_base = 'leetcode.com'
        region = 'global'
    elif country_ == '2':
        url_base = 'leetcode-cn.com'
        region = 'local'
    else:
        return ''
    if contest_type_ == '1':
        contest = f'weekly-contest-{week_no_}'
    elif contest_type_ == '2':
        contest = f'biweekly-contest-{week_no_}'
    else:
        return ''
    url = f'https://{url_base}/contest/api/ranking/{contest}/?'
    headers = {
        'cookie': 'gr_user_id=a92c7a68-17b5-4027-9525-9b2b3b62b6ea; _ga=GA1.2.2027613635.1555847093; grwng_uid=36692f18-9c9e-4b86-97bc-67b31d310f82; _uab_collina=155594416479372913637839; a2873925c34ecbd2_gr_last_sent_cs1=wangyehope; __auc=af7dfe3f16d32fe596a06bdade0; aliyungf_tc=c6579c2b242c25cdf89caf73d3e66332dff036c92737213bb081d8ca5a43b969; NEW_PROBLEMLIST_PAGE=1; __appToken__=; _gid=GA1.2.187012209.1630205309; a2873925c34ecbd2_gr_session_id=f31cf193-5ba6-461a-916d-ad8961b3ef24; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=f31cf193-5ba6-461a-916d-ad8961b3ef24; a2873925c34ecbd2_gr_session_id_f31cf193-5ba6-461a-916d-ad8961b3ef24=true; __asc=1c6e9b4f17b900ee45dc189982e; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1630209500,1630209505,1630209524,1630209533; csrftoken=m6BnyUduGVEbl4tpJ733WxTu3QigVViGdDb58pjQthQkWAUB6t6vaGSBu6GEfpZF; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1630210412; a2873925c34ecbd2_gr_cs1=wangyehope; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJfYXV0aF91c2VyX2lkIjoiNDk1NjA1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiYWxsYXV0aC5hY2NvdW50LmF1dGhfYmFja2VuZHMuQXV0aGVudGljYXRpb25CYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYTFkNGVjNTZjM2NjMDlkYTRiM2FhNzdiNTk4NmJlOTcwNDBmZWEyMDA2MmM0MjdlYjQxNTQyNTU3OTM1Zjc2YiIsImlkIjo0OTU2MDUsImVtYWlsIjoiOTA1MzE3NzQyQHFxLmNvbSIsInVzZXJuYW1lIjoid2FuZ3llaG9wZSIsInVzZXJfc2x1ZyI6Indhbmd5ZWhvcGUiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy93YW5neWVob3BlL2F2YXRhcl8xNjIzNTA2MTQ1LnBuZyIsInBob25lX3ZlcmlmaWVkIjp0cnVlLCJfdGltZXN0YW1wIjoxNjMwMjA5Njg3LjQ0MTc2OTEsImV4cGlyZWRfdGltZV8iOjE2MzI3NjkyMDAsImxhdGVzdF90aW1lc3RhbXBfIjoxNjMwMjEwNDMwfQ.bGK7V76yX9-esPrbLJI2Jwgf5aGpkODvichJ3YEc2qM; _gat_gtag_UA_131851415_1=1',
        'content-type': 'application/json',
    }
    page = 45
    while True:
        url_ = url + urllib.parse.urlencode({'pagination': page, 'region': region})
        print(url_)
        while res := requests.get(url_, headers):
            if res.status_code == 200:
                break
        txt = json.loads(res.text)
        if not txt['total_rank']:
            break
        for item in txt['total_rank']:
            if name_ in item['username']:
                return item
        page += 1


def ask(question, answers=None):
    while True:
        ret = input(question)
        if not answers or ret and ret in answers:
            return ret


def main():
    country = ask('Global(1) or China(2)?', ('1', '2'))
    contest_type = ask('Contest(1) or Biweekly Contest(2)?', ('1', '2',))
    week_no = ask('The week number is:')
    name = ask('The user\'s name is:')
    pprint.pprint(find(country, contest_type, week_no, name))
    # pprint.pprint(find('1', '256', 'xhc'))
    # pprint.pprint(find('1', '256', 'jia-zhou-e'))


if __name__ == '__main__':
    main()
