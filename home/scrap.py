import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor


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
