'''
    Created By: Shivam Ralli
    Date: 17/05/2020
    Github.com/sralli
'''

import datetime, json, time
from selenium import webdriver
from messages import randomize_messages
from database import Init_df, Update
from webdriver import Initialze_Script
from ast import literal_eval

names, already_sent, nicknames = Init_df().Birthday_Today()
idx=0

try:
   alrady_sent = [literal_eval(i) for i in already_sent]
except:
    pass


for name, sent in zip(names, already_sent):
    try:
        message_block_value = randomize_messages(literal_eval(sent))
    except:
        message_block_value = randomize_messages(sent)
    message = message_block_value()
    Initialze_Script().send_message(name= name, message = f"Hi {nicknames[idx]}, {message[1]}")
    Update(message[0], idx)
    idx+=1



