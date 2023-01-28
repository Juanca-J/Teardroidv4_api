from deta import Deta
from os import getenv

deta = Deta("e088wg5t_kfqwuU5c2rADLnqxxzUWZ1ahNFUrLqk9")


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
