import tomli


class Config(object):
    def __init__(self, name, iterable=(), **kwargs):
        with open('./backend/config/config.toml', mode='rb') as file:
            config = tomli.load(file)
            try:
                self.__dict__.update(config[name], **kwargs)
            except Exception:
                raise BaseException(f'configuration not found ({name})')
