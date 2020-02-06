#!/usr/bin/python
# -*- coding: utf-8 -*-


#Splunk Custom Alert Action for Telegram 

import os
import sys
import re
import subprocess
import json
import csv
import gzip
import requests
import urllib
import datetime

URL = "https://api.telegram.org"

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def send_message(text):
    url = URL + "{}".format(text)
    get_url(url)

def log(msg):
    f = open(os.path.join(os.environ["SPLUNK_HOME"],  "var", "log", "splunk", "alert_telegram.log"), "a")
    print >> f, str(datetime.datetime.now().isoformat()), msg
    f.close()

#Check args
def main():
    #os.environ['LD_LIBRARY_PATH'] = os.getcwd()
    #get json ouptut from splunk modular alert - See alert_actions.conf.spec
    payload = json.loads(sys.stdin.read())
    config = payload.get('configuration', dict())
    #host = payload.get('host') 
    splunkServer = payload.get('server_host')
    splunkURI = payload.get('server_uri')
    splunkApp = payload.get('app')
    splunkSearch = payload.get('search_name')
    resultsLink = payload.get('results_link')
    #result = payload.get('result')
    botID = config.get('botID')
    message = config.get('message')
    severity = config.get('severity')
    chat = config.get('chat')
    message = "<b>****SPLUNK ALERT MESSAGE***</b>\n<b>Splunk Search</b>: {0} \n<b>SEVERITY</b>: {1} \n<b>MESSAGE</b>: {2} \n<b>Results Link</b>: {3}".format(splunkSearch, severity, message, resultsLink)

    #Format the paramaters and pass them to send_message
    params = urllib.urlencode({'text': message,
                               'chat_id': chat,
                               'parse_mode': "HTML",
                               'disable_web_page_preview': "1"})
    link = "/bot{0}/sendMessage?{1}".format(botID, params)

            #UNCOMMENT DEBUG
    log("[DEBUG] - Telegram Alert Starting")

    try:
        log("[DEBUG] - Sending Alert Message")
        send_message(link) 
        log("[DEBUG] - Alert Message Sent")
    except:
        log("[ERROR] - Telegram Alert Failed, check splunkd.log for more details.")
        sys.stderr.write('[Telegram] failed to run CURL command\n')
        sys.stderr.write('[Telegram] {0}\n'.format(message))
if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] != "--execute":
        print >> sys.stderr, "FATAL Unsupported execution mode (expected --execute flag)"
        sys.exit()

    main()
