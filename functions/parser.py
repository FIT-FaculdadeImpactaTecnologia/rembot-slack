#!usr/bin/env python
#-*- coding: utf-8 -*-

from config import settings

AT_BOT = "<@" + settings.SLACK_BOT_ID + "> /"

def parse_slack_output(rtm_output):
    output_list = rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), output['channel']
    return None, None