#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial

# 各自適当なデバイスファイルに修正してください。
printer = serial.Serial('/dev/tty.SM1-21-SerialPortDevB', 115200)

from tweepy.streaming import StreamListener, Stream
from tweepy.auth import OAuthHandler
from tweepy.api import API
from datetime import timedelta

def get_oauth():
  consumer_key = ''
  consumer_secret = ''
  access_key = ''
  access_secret = ''
  auth = OAuthHandler(consumer_key, consumer_secret)
  auth.set_access_token(access_key, access_secret)
  return auth
  
class StreamListener(StreamListener):
  def on_status(self, status):
    status.created_at += timedelta(hours=9)
    for hashtag in status.entities['hashtags']:
      printer.write(u"{text}".format(text=status.text).encode('shift-jis', 'replace') + '\n')
      printer.write(u"{name}({screen})\n{time}\n".format(
        name=status.author.name, screen=status.author.screen_name,
        time=status.created_at).encode('shift-jis', 'replace'))
      printer.write('-' * 32 + '\n')
      
if __name__ == '__main__':
  printer.write('\x1c\x26') # Enable Full-Widthe
  printer.write('\x1c\x43\x01') # Enable Shift JIS
  auth = get_oauth()
  stream = Stream(auth, StreamListener(), secure=True)
  stream.filter(track=['#kosenconf'])
