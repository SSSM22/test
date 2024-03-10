import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor
import http.client
import json
import math

def hackerrank_ranking(username):
    if(username == 'None'):
        return 0
    try:
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
    except:
        return 0
    algo=parsed_data[1]['practice']['score']
    ds=parsed_data[9]['practice']['score']
    
    return math.floor(algo+ds)


def forcesrate(forcesu):
    if(forcesu == 'None'):
        return 0
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
    if(chefu == 'None'):
        return 0
    url = f"https://www.codechef.com/users/{chefu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(class_="rating-data-section problems-solved")
        if rank_element:
            try:
                rank = str(list(rank_element)[1])
                return int(rank[23:-8])+int(str((list(rank_element)[5]))[14:-8])
            except:
                return 0
        else:
            return 0
    else:
        return 0


def leetrate(leetu):
    if(leetu == 'None'):
        return 0
    url = f"https://leetcode.com/{leetu}"
    response = requests.get(url)
    print(response.status_code)
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
    if(spo == 'None'):
        return 0
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
    if(username == 'None'):
        return 0
    url = f"https://www.interviewbit.com/profile/{username}"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_elements = soup.find_all(class_="profile-daily-goal__goal-details")
        print(rank_elements)
        if rank_elements is not None:
            try:
                rank = int(rank_elements[1].get_text().strip())
                return rank
            except:
                return 0
    else:
        return 0


def geeksforgeeks_ranking(username):
    if(username == 'None'):
        return 0
    url = f"https://auth.geeksforgeeks.org/user/{username}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_elements = soup.find('span',class_="score_card_value").text.strip()
        if rank_elements is not None:
            try:
                
                return rank_elements
            except:
                return 0
    else:
        return 0


def get(usernames: list, func) -> list: # usernames is a list of dictionaries having rollno,usernames and score
    
    start_time = time.time()
    userid = []
    for i in usernames:
        userid.append(i['id']) #appending usernames to userid list

    with ThreadPoolExecutor(max_workers=7) as p:
        res = list(p.map(func, userid)) #res is a list of scores of all the usernames

    c = 0
    for x in res: #iterating through the scores list and adding them to the usernames dictionary
        
        usernames[c]['score'] = x
        c = c+1
    print(f"{(time.time() - start_time):.2f} seconds")

    return usernames

# Profiles for testing purposes

# print(leetrate('sssm_2003'))
# print(coderate("srivandana"))
# print(forcesrate("srivandanatalla"))
# print(spojrate("srivandana"))
#print(geeksforgeeks_ranking('sssm_2003'))
# print(interviewbit_ranking("sssm_2003"))
# print(hackerrank_ranking('sssm_2003'))
