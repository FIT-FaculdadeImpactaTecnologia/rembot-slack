#!usr/bin/env python
#-*- coding: utf-8 -*-

import commands
import initializer

def handle_command(command, channel):
    print "Interpretando comandos..."
    client = initializer.initclient()
    invalid_command = "Comando inválido, tente novamente!"
    if len(command.split()) > 1:
        values = command.split('@')
        command = values[0].strip()
        params = values[1].split()
        print params
        client.api_call('chat.postMessage', channel=channel, text=getattr(commands, command)(params), as_user=True)
    else:
        if hasattr(commands, command):
            print "Executando comando..."
            client.api_call('chat.postMessage', channel=channel, text=getattr(commands, command)(), as_user=True)
        else:
            print "Comando inválido..."
            client.api_call('chat.postMessage', channel=channel, text=invalid_command, as_user=True)
