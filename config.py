#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7546999478:AAEKDk5AqJ6sLd_v8w8mmqNf4WdU1hKVTC4")
    API_ID = int(os.environ.get("API_ID", "21857983"))
    API_HASH = os.environ.get("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
    AUTH_USERS = os.environ.get("AUTH_USERS", "833465134")
