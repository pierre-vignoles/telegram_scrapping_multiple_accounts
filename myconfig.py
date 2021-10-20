from pathlib import Path
from typing import List, Dict, Union

# Variables to change
api_list: List[Dict[str, Union[str, int]]] = [
    {'api_id': your_api_id, 'api_hash': 'your_api_hash', 'username': 'your_username'},
    {'api_id': your_api_id, 'api_hash': 'your_api_hash', 'username': 'your_username'}
]
number_of_adds_per_session: int = 10
split_by: int = 2
number_of_seconds_to_wait_between_every_add: int = 200
number_of_seconds_min_to_wait_between_every_add: int = 20
path_csv: Path = Path("path_you_want_to_save_csv")
bool_send_message: bool = False
number_of_adds_between_every_message: int = 2
link_channel_to_add_members = "https://t.me/..."
link_channel_you_want_to_scrape = "https://t.me/..."


# Do not modify
list_columns: List[str] = ['username', 'id', 'access_hash', 'name']
title_blacklist_csv: str = "blacklist_members.csv"
