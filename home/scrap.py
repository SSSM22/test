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
            rank = rank_element.get_text().strip()[0]
            return int(rank)
        else:
            return "Ranking not found."
    else:
        return "Unable to connect to LeetCode."


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

# test function


def get(dic):
    res = []
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as p:
        res.append(p.submit(leetrate, dic["leet"]))
        res.append(p.submit(coderate, dic['code']))
        res.append(p.submit(forcesrate, dic['forces']))

    for x in res:
        print(x.result())

    # leetrate(dic["leet"])
    # coderate(dic['code'])
    # forcesrate(dic['forces'])

    print(f"{(time.time() - start_time):.2f} seconds")


def main():
    for i in range(2):
        get({"leet": "mesh_05", "code": "mesh_05", "forces": "mesh_05"})


main()
