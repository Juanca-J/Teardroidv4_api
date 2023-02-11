from deta import Deta
from os import getenv

deta = Deta("e0owadsa_g6YPrgeZqFJzY2gfE8JeHDvHNvAYvrAa")


def client_db():
    return deta.Base("client")


def notification_db():
    return deta.Base("notification")


def command_db():
    return deta.Base("command")


def auth_db():
    return deta.Base("auth")


async def tear_drive():
    return deta.Drive("teardroid")
