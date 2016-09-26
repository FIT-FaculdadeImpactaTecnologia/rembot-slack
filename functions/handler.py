#!usr/bin/env python
#-*- coding: utf-8 -*-

import commands
import initializer

def handle_command(command, channel):
    client = initializer.initclient()
    invalid_command = "Comando inválido, tente novamente!"
    if len(command.split()) > 1:
        values = command.split()
        command = values[0]
        param = values[1]
        client.api_call('chat.postMessage', channel=channel, text=getattr(commands, command)(param), as_user=True)
    if hasattr(commands, command):
        client.api_call('chat.postMessage', channel=channel, text=getattr(commands, command)(), as_user=True)
    else:
        client.api_call('chat.postMessage', channel=channel, text=invalid_command, as_user=True)
