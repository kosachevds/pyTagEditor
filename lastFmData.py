﻿import pylast

API_KEY = '70578b40668e460c6282ee394e448586'
API_SECRET = 'd105089ed009bbd740176b4e00ffd261'
URL = 'ws.audioscrobbler.com'
USERNAME = 'kosds'
password_hash = pylast.md5('12481632!')

network = pylast.LastFMNetwork(API_KEY, API_SECRET, USERNAME, password_hash)
