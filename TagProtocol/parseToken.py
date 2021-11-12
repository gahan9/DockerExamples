# Web Scrapper to parse token id, name, grade, from https://tagscan.info/tokenID/<token-id>/0/10

import os
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup

BASE_URL = "https://tagscan.info/tokenID"
MAX_TOKEN_ID = 20500  # TODO: Parse max value from https://tagprotocol.com/


# TODO: Add a function to resume parsing of token

CSV_HEADER = ["tokenID", "hashTag", "Earned Tag", "Current Grade", "Avg Grade", "Current Rank", "Avg Rank", "Index Pages", "1 Day", "2 Day", "3 Day"]

def url_to_bs(url):
    page = requests.get(url)
    return BeautifulSoup(page.content, "html.parser")

def get_tabular_data(page):
    """Parse tabular data from the page

    @param page: BeautifulSoup object which contains the tabular data in div and text under tag `span`

    @return: list of `n` strings contains data parsed from table [as such 4 values]
    """
    return [i.find('span').text for i in page.find_all("div")]


def parse_token(token_id):
    """Parse record information for given token ID

    @param token_id: token ID to parse webpage for

    @return: list of values for csv header
    """
    url = f"{BASE_URL}/{token_id}/0/10"
    soup = url_to_bs(url)
    hash_tag = soup.find("div", class_="tokenID").find("span").text[1:]
    earnings, performance, social_media_idx_count = soup.find_all("div", class_="datatablecont")
    earned_tag = earnings.find_all("div")[0].find("span").text.split()[0]
    current_grade, average_grade, current_rank, average_rank = get_tabular_data(performance)
    current_idx, one_day, two_day, three_day = [i.split()[0] for i in get_tabular_data(social_media_idx_count)]
    return [token_id, hash_tag, earned_tag, current_grade, average_grade, current_rank, average_rank, current_idx, one_day, two_day, three_day]

def parse_tokens(max_tokens=MAX_TOKEN_ID, csv_file="result.csv"):
    """
    Parse all tokens from 1 to max_tokens
    """
    if not csv_file:
        print("Exiting function...there's no means to keep running if you are not storing parsed data!!!")
        return False
    next_token_idx = 1
    if csv_file:
        if os.path.exists(csv_file):
            last_row = open(csv_file, "r").readlines()[-1]
            last_token_id = int(last_row.split(";")[0])
            next_token_idx = last_token_id + 1

    for token_id in range(next_token_idx, max_tokens+1):
        if token_id in (next_token_idx, max_tokens) or token_id % 100 == 0:  # show progress status on every 200th parsed record
            print(f"[Parser:T{datetime.now().strftime('%H-%M-%S')}]Parsing token {token_id}/{max_tokens}")
        try:
            csv_row = parse_token(token_id)
        except AttributeError:
            print(f"Token {token_id}....trying again")
            time.sleep(2)
            csv_row = parse_token(token_id)

        with open(csv_file, "a+") as f:
            if next_token_idx == 1 and next_token_idx == token_id:
                f.write("; ".join(CSV_HEADER) + "\n")
            f.write("; ".join([str(i) for i in csv_row]) + "\n")


if __name__ == "__main__":
    timestamp = datetime.utcnow().strftime("%Y-%m-%d")  # Since site result updated on 00 UTC date is kept from utc time.
    csv_file_name = f"tag_protocol_{timestamp}.csv"
    parse_tokens(max_tokens=MAX_TOKEN_ID, csv_file=csv_file_name)
