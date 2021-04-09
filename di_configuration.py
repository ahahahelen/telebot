import dependency_injector as di
from dependency_injector import containers, providers

class DIConfige(containers.DeclarativeContainer):
    config_ini = providers.Object()

class DIBot(containers.DeclarativeContainer):
    di_bot = providers.Object()

