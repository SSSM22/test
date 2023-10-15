import requests
from bs4 import BeautifulSoup
import time
from concurrent.futures import ThreadPoolExecutor


def forcesrate(forcesu):
    url = f"https://codeforces.com/profile/{forcesu}"
    response = requests.get(url, timeout=0.1)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="_UserActivityFrame_counterValue")
        if rank_element:
            rank = rank_element.get_text().strip()[0]
            return int(rank)
        else:
            return "Ranking not found."
    else:
        return "Unable to connect to Codeforces."


def coderate(chefu):
    url = f"https://www.codechef.com/users/{chefu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(class_="rating-data-section problems-solved")
        if rank_element:
            rank = rank_element.get_text().strip().split()[2]
            return int(rank[1:-2])
        else:
            return "Ranking not found."
    else:
        return "Unable to connect to CodeChef."


def leetrate(leetu):
    url = f"https://leetcode.com/{leetu}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="text-[24px] font-medium text-label-1 dark:text-dark-label-1")
        if rank_element:
            rank = rank_element.get_text().strip()
            return rank
        else:
            return "Ranking not found."
    else:
        return "Unable to connect to LeetCode"


def spojrate(spo):
    url = f'https://www.spoj.com/users/{spo}'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        rank_element = soup.find(
            class_="dl-horizontal profile-info-data profile-info-data-stats"
        )
        print(rank_element)


def get(usernames: dict, func) -> dict:
    result = {}
    start_time = time.time()

    with ThreadPoolExecutor(max_workers=20) as p:
        res = list(p.map(func, usernames.keys()))

    keys = list(usernames.keys())
    c = 0
    for x in res:
        result[keys[c]] = x
        c = c+1
    print(f"{(time.time() - start_time):.2f} seconds")

    return result

# leetrate(leet_id)
# coderate(chef_id)
# forcesrate(forces_id)
