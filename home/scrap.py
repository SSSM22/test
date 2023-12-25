import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
import http.client
import json
import math

def hackerrank_ranking(username):
    conn = http.client.HTTPSConnection("www.hackerrank.com")
    payload = ""
    headers = {
        'cookie': "hackerrank_mixpanel_token=ff22930b-bc23-4171-bc2b-b88d8feb3fd0; hrc_l_i=F; _hrank_session=798b66069b13021061cd131795c615e6",
        'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
        }
    to_get="/rest/hackers/"+username+"/scores_elo"
    conn.request("GET",to_get , payload, headers)
    res = conn.getresponse()
    data = res.read()
    data=data.decode("utf-8")
    parsed_data = json.loads(data)
    if(len(parsed_data)==1 or len(parsed_data)==0):
        return 0
    algo=parsed_data[1]['practice']['score']
    ds=parsed_data[9]['practice']['score']
    
    return math.floor(algo+ds)


def forcesrate(forcesu):
    url = f"https://codeforces.com/profile/{forcesu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="_UserActivityFrame_counterValue")
        if rank_element:
            try:
                rank = rank_element.get_text().strip()[0]
                return int(rank_element.text[0:-9])
            except:
                return 0
        else:
            return 0
    else:
        return 0


def coderate(chefu):
    url = f"https://www.codechef.com/users/{chefu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(class_="rating-data-section problems-solved")
        if rank_element:
            try:
                rank = str(list(rank_element)[1])
                return int(rank[23:-8])
            except:
                return 0
        else:
            return 0
    else:
        return 0


def leetrate(leetu):
    url = f"https://leetcode.com/{leetu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")
        if rank_element:
            try:
                rank = int(rank_element.get_text().strip())
                return rank
            except:
                return 0

        else:
            return 0
    else:
        return 0


def spojrate(spo):
    url = f'https://www.spoj.com/users/{spo}'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="dl-horizontal profile-info-data profile-info-data-stats"
        )
        try:
            rank = str(list(rank_element)[3])
            return (int(rank[4:len(rank) - 5]))
        except:
            return 0

    return 0

# test function


def interviewbit_ranking(username):
    url = f"https://www.interviewbit.com/profile/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_elements = soup.find_all(class_="txt")
        if rank_elements is not None:
            try:
                rank = int(rank_elements[1].get_text().strip())
                return rank
            except:
                return 0
    else:
        return 0


def geeksforgeeks_ranking(username):
    url = f"https://auth.geeksforgeeks.org/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_elements = soup.find_all(class_="score_card_value")
        if rank_elements is not None:
            try:
                rank = int(rank_elements[1].get_text().strip())
                return rank
            except:
                return 0
    else:
        return 0


def get(usernames: list, func) -> list:
    result = {}
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=7) as p:
        res = list(p.map(func, usernames.keys()))

    keys = list(usernames.keys())
    c = 0
    for x in res:
        result[keys[c]] = x
        c = c+1
    print(f"{(time.time() - start_time):.2f} seconds")

    return result

# Profiles for testing purposes

# print(leetrate('Sithis'))
# print(coderate("everule1"))
# print(forcesrate("tourist"))
# print(spojrate("defrager"))
# print(geeksforgeeks_ranking('anil bera'))
# print(interviewbit_ranking("sssm_2003"))
# print(hackerrank_ranking('sssm_2003'))
