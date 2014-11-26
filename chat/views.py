import itertools

import asyncio

from django.conf import settings
from django.shortcuts import render

from c10ktools.http import websocket


global_subscribers = set()


def echo(request):
    return render(request, 'chat/chatpage.html')


@websocket
def echo_ws(ws):
    print("Watcher connected")
    global_subscribers.add(ws)
    # Block until the client goes away
    while True:
        message = yield from ws.recv()
        if message is None:
            break
        for subscriber in global_subscribers:
            if subscriber.open:
                yield from subscriber.send(str(message))

        # yield from ws.send(message)
        print(message)
    global_subscribers.remove(ws)
    print("Watcher disconnected")


