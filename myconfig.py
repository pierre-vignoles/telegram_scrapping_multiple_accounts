from pathlib import Path
from typing import List, Dict, Union

# Variable to change
api_list: List[Dict[str, Union[str, int]]] = [
    {'api_id': 8759294, 'api_hash': 'd591adc00cebda110561f5ce1e808d35', 'username': 'Lucas_2555'},
    {'api_id': 8014027, 'api_hash': 'ccbf8418fd3368655d1daf3f98f5b69c', 'username': 'Xavier_2555'}
]
number_of_adds_per_session: int = 10
split_by: int = 2
number_of_seconds_to_wait_between_every_add: int = 1800
number_of_seconds_min_to_wait_between_every_add: int = 300
path_csv: Path = Path("C:/Users/pierr/PycharmProjects/telegram_scrapping/csv")
bool_send_message: bool = True
number_of_adds_between_every_message: int = 2
link_channel_to_add_members = "https://t.me/Saviez_vous_que_gr"
link_channel_you_want_to_scrape = "https://t.me/cryptotradersdiscussion"

# Do not modify
list_columns: List[str] = ['username', 'id', 'access_hash', 'name']
title_blacklist_csv: str = "blacklist_members.csv"
