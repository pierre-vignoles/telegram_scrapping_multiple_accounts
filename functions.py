from telethon.client.telegramclient import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.types import InputPeerUser, Channel
from telethon.errors.rpcerrorlist import PeerFloodError, UserPrivacyRestrictedError, UserNotMutualContactError, \
    UserChannelsTooMuchError, ChannelPrivateError
from telethon.tl.types import UserStatusRecently
from telethon.helpers import TotalList

import re
import csv
import traceback
import time
from random import randint
import random
from pathlib import Path
from typing import List, Dict, Union, Tuple

from myconfig import *

from colorama import init, Fore

init()
rs = Fore.RESET
lg = Fore.LIGHTGREEN_EX
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
colors = [cy, w, r]


def logo():
    logo_str: List[str] = ["""`` ``  `` ``  `  `` ``  `` `..-::////::-..` ``  `` ``  `  ``  `  `` ``""",
"""  `  `` ``  `` ``  `` ``.:+oosossssssssoooo+:.`` ``  `` ``  `  ``  `"""  ,
"""`` ``  `` ``  `  ````./oossssssssssssssssssssoo:.` `   `  ``  `  `  ``""",
"""``  `  `   `  `` ``.+osssssssssssssssssssssssssso+.``  `  `   `  `` ` """,
"""  `  ``  `  `` ```/osssssssssssssssssssssssssssssso/``` ``  `  ``  `  """,
"""`` ``  `  ``  ``.+sssssssssssssssssssssssssssssssssso.``  `` ``  `` ``""",
"""  `  ``  `  `` .ossssssssssssssssssssssssso++ossssssso. ``  `  ``  `  """,
"""``  `  `  `` ``+ssssssssssssssssssssso+/:-```/sssssssso`  `` ``  `  ``""",
"""  `  `   `  ``:ssssssssssssssssoo+/:.````   `osssssssss:``  `  ``  `  """,
"""  `  `   ` ```osssssssssssoo+/-.``  ``.``   :sssssssssso``` `  `  ``  """,
"""`` ``  `` `` `ossssssso+/-.`     ``..`      +sssssssssss` `` ``  `  ``""",
"""  `  `` ``  ``ossssssso-.``   ``...`       .ssssssssssso``  `` ``  `  """,
"""``  `  `` `` `osssssssssoo+/:....`         /ssssssssssso` ``  `  `  ``""",
""" `  ``  `  ``:ssssssssssssso:.-.`        `ossssssssssss:``  `  ``  `  """,
"""``  `  ``  `  `+sssssssssssss+---:/-`     :ssssssssssso`  `   `  `  ` """,
""" ``    `      `.osssssssssssss/:+osso/.` `osssssssssso.    `        ` """,
"""  `  ``  `  `` `.ossssssssssssoosssssso+/+ssssssssss+.`  `  `  ``  `  """,
"""`` ``  `  ``  ` ``/osssssssssssssssssssssssssssssso/`  `  ``  `  `` ``""",
"""  `  ``  `  `` `` `.+osssssssssssssssssssssssssso+.  `` ``  `  ``  `  """,
"""``  `  `  ``  `  `` `./oossssssssssssssssssssoo/.` ``  `  ``  `  `` ``""",
"""  `  `` ``  `   `  `` ``.:+oooossssssssooso+:.`` ``  `` ``  `  ``  `  """,
"""```  ``         `  `  `` ````--::////::--```````     ````` `          """]
    for idx, char in enumerate(logo_str):
        if idx <= (len(logo_str) / 3) :
            colors_list = colors[0]
        elif idx <= (len(logo_str) / 3)*2 :
            colors_list = colors[1]
        else:
            colors_list = colors[2]

        print(f'{colors_list}{char}{rs}')
    print(f'{r}Telegram Scraper{rs}\n')
    print(f'{lg}Version: {rs}1.0 | {lg}Author: {rs}Pierre{rs}\n')


def define_title_file(target_group_title: str, own_group_or_blacklist: bool, username: str) -> str:
    title_file: str = target_group_title
    title_file = title_file.replace(" ", "_").lower()
    title_file = "".join(re.findall("[a-zA-Z_]", title_file))
    title_file = title_file[:-1] if title_file[-1] == "_" else title_file
    if own_group_or_blacklist == False:
        title_file = title_file + "_" + username
    title_file = str(title_file) + ".csv"
    return title_file


async def join_group(client: TelegramClient) -> Tuple[Channel, Channel]:
    try:
        your_group = await client.get_entity(link_channel_to_add_members)
        await client(JoinChannelRequest(your_group))
        print("\n\n Group {} joined ".format(your_group.title))
    except ChannelPrivateError:
        print("\n\n Group {} can't be joined with this account because ChannelPrivateError".format(group_scrape.title))
    try:
        group_scrape = await client.get_entity(link_channel_you_want_to_scrape)
        await client(JoinChannelRequest(group_scrape))
        print("\n\n Group {} joined ".format(group_scrape.title))
    except ChannelPrivateError:
        print("\n\n Group {} can't be joined with this account because ChannelPrivateError".format(group_scrape.title))
    return your_group, group_scrape


async def scrapping_members_of_a_group(own_group: bool, target_group: Channel, client: TelegramClient, username: str) -> \
Tuple[
    List[Dict[str, Union[str, int]]], str]:
    title_file: str = define_title_file(target_group.title, own_group, username)
    my_file: Path = Path(path_csv / title_file)
    if not my_file.is_file():
        all_participants = await scrap_members_on_a_group(target_group, client)
        title_file = await write_csv_members(all_participants, target_group, own_group, username)
        users_on_your_group = await read_csv_members(title_file, own_group)
    else:
        users_on_your_group = await read_csv_members(title_file, own_group)
    return users_on_your_group, title_file


async def scrap_members_on_a_group(target_group: Channel, client: TelegramClient) -> TotalList:
    print('Loading members...')
    all_participants = await client.get_participants(target_group, aggressive=True)
    return all_participants


async def write_csv_members(all_participants: TotalList, target_group: Channel, own_group: bool, username) -> str:
    title_file = define_title_file(target_group.title, own_group, username)

    with open(path_csv / title_file, "w", encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        writer.writerow(list_columns)
        for user in all_participants:
            if str(user.status) not in (str(UserStatusRecently())):
                continue
            else:
                if user.username:
                    username = user.username
                else:
                    username = ""
                if user.first_name:
                    first_name = user.first_name
                else:
                    first_name = ""
                if user.last_name:
                    last_name = user.last_name
                else:
                    last_name = ""
                name = (first_name + ' ' + last_name).strip()
                writer.writerow([username, user.id, user.access_hash, name])
    print('Members scraped successfully.')
    return title_file


async def add_member_csv(user: Dict[str, Union[str, int]], title_file):
    title_file = path_csv / title_file

    with open(title_file, 'a+', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")

        if user['username']:
            username = user['username']
        else:
            username = ""
        if user['name']:
            name = user['name']
        else:
            name = ""
        writer.writerow([username, user['id'], user['access_hash'], name])
    print("Member : " + str(user['id']) + " added to the csv")


async def write_csv_blacklist(user: Dict[str, Union[str, int]], reason_blacklist: str, title_file=False):
    if title_file == False:
        title_file = title_blacklist_csv
        my_file = Path(path_csv / title_file)
    else:
        title_file = "blacklist_" + title_file
        title_file = path_csv / title_file
        my_file = Path(title_file)

    if my_file.is_file():
        file_exist = True
    else:
        file_exist = False

    with open(my_file, 'a+', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=";", lineterminator="\n")
        if file_exist == False:
            writer.writerow(list_columns + ['reason_blacklist'])

        if user['username']:
            username = user['username']
        else:
            username = ""
        if user['name']:
            name = user['name']
        else:
            name = ""
        writer.writerow([username, user['id'], user['access_hash'], name, reason_blacklist])
    print("Member : " + str(user['id']) + " added to the blacklist csv")


async def read_csv_members(input_file: str, only_id: bool) -> List[Union[Dict[str, Union[str, int]], int]]:
    users: List[Union[Dict[str, Union[str, int]], int]] = []
    my_file: Path = Path(path_csv / input_file)
    if my_file.is_file():
        with open(str(my_file), encoding='UTF-8') as f:
            rows = csv.reader(f, delimiter=";", lineterminator="\n")
            next(rows, None)
            if only_id == False:
                for row in rows:
                    user = {'username': row[0]}
                    try:
                        user['id'] = int(row[1])
                        user['access_hash'] = int(row[2])
                        user['name'] = row[3]
                    except IndexError:
                        print('users without id or access_hash')
                    users.append(user)
            else:
                for row in rows:
                    try:
                        users.append(int(row[1]))
                    except IndexError:
                        print('users without id')

    else:
        users = []
    return users


def random_choice_username(username: str) -> str:
    random_username = random.choice(api_list)['username']
    if random_username == username:
        random_username = random_choice_username(username)
    return random_username


async def function_send_message(client: TelegramClient, username: str):
    list_words = ['apple', 'banana', 'cherry', 'dates', 'etc', 'have', 'I', 'You', 'good', 'morning', 'what', ]
    sentence = []
    random_number_message = randint(2, 10)
    random_username = random_choice_username(username)
    for i in range(0, random_number_message):
        sentence.append(random.choice(list_words))
    sentence = " ".join(sentence)
    entity = await client.get_entity(random_username)
    await client.send_message(entity=entity, message=sentence)
    print("message sent")


async def add_members_to_group(client: TelegramClient, username: str):
    global value
    print("\nSESSION : {}\n".format(username))
    your_group, target_group = await join_group(client)
    users_on_your_group, title_file_of_your_own_group = await scrapping_members_of_a_group(True, your_group, client,
                                                                                           username)
    users_in_the_other_group, title_file_of_the_other_group = await scrapping_members_of_a_group(False, target_group,
                                                                                                 client, username)
    users_blacklist = await read_csv_members("blacklist_" + str(define_title_file(target_group.title, True, username)),
                                             True)
    users_blacklist_2 = await read_csv_members(title_blacklist_csv, True)
    users_you_want_to_add = [user for user in users_in_the_other_group if
                             user['id'] not in (users_on_your_group + users_blacklist + users_blacklist_2)]

    random.shuffle(users_you_want_to_add)

    for idx, user in enumerate(users_you_want_to_add):
        if idx >= (number_of_adds_per_session / split_by):
            break
        else:
            try:
                user_to_add = InputPeerUser(user['id'], user['access_hash'])
                if idx == 0:
                    await client(InviteToChannelRequest(your_group, [user_to_add]))
                    print("\nAdd : " + str(user['id']))
                    print(str(idx + 1) + "/" + str(len(users_you_want_to_add)))
                    await add_member_csv(user, title_file_of_your_own_group)
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add))
                    time.sleep(number_of_seconds_to_wait_between_every_add)
                else:
                    value = randint(number_of_seconds_min_to_wait_between_every_add,
                                    number_of_seconds_to_wait_between_every_add)
                    print("\nWait {} sec..".format(value))
                    time.sleep(value)
                    await client(InviteToChannelRequest(your_group, [user_to_add]))
                    print("Add : " + str(user['id']))
                    print(str(idx + 1) + "/" + str(len(users_you_want_to_add)))
                    await add_member_csv(user, title_file_of_your_own_group)
                    if idx % number_of_adds_between_every_message == 0:
                        if bool_send_message == True:
                            await function_send_message(client, username)
                        #print("\nWait {} sec..".format(number_of_seconds_to_wait_between_every_add * 2))
                        #time.sleep(number_of_seconds_to_wait_between_every_add * 2)
                    else:
                        print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add - value))
                        time.sleep(number_of_seconds_to_wait_between_every_add - value)

            except PeerFloodError as e:
                print("\nGetting Flood Error from telegram. Switch session...")
                break
            except UserPrivacyRestrictedError:
                print("The user's privacy settings do not allow you to do this. Skipping.")
                await write_csv_blacklist(user, 'UserPrivacyRestrictedError', title_file=False)
                if idx == 0:
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add))
                    time.sleep(number_of_seconds_to_wait_between_every_add)
                else:
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add - value))
                    time.sleep(number_of_seconds_to_wait_between_every_add - value)
            except UserNotMutualContactError:
                print("The user has already leave the group and he is not in your contact")
                await write_csv_blacklist(user, 'UserNotMutualContactError', title_file=title_file)
                if idx == 0:
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add))
                    time.sleep(number_of_seconds_to_wait_between_every_add)
                else:
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add - value))
                    time.sleep(number_of_seconds_to_wait_between_every_add - value)
            except UserChannelsTooMuchError:
                print("The user is already in too many channels")
                await write_csv_blacklist(user, 'UserChannelsTooMuchError', title_file=False)
                if idx == 0:
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add))
                    time.sleep(number_of_seconds_to_wait_between_every_add)
                else:
                    print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add - value))
                    time.sleep(number_of_seconds_to_wait_between_every_add - value)
            except KeyboardInterrupt:
                print(f'{error}{r} ---- Adding Terminated ----')
                exit_window()
            except:
                traceback.print_exc()
                print("Unexpected Error")
                print("Wait {} sec..".format(number_of_seconds_to_wait_between_every_add))
                time.sleep(number_of_seconds_to_wait_between_every_add)

    print("\n\nSwitch sessions")
