import os

import yaml


class ConfigReader:
    def __init__(self, config_path=None):
        if config_path is None:
            config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(config_path, "r", encoding="utf-8") as f:
            self.config = yaml.safe_load(f)

    def get_base_url(self):
        return self.config.get("base_url")

    def get_timeout(self):
        return self.config.get("timeout", 10)

    def get_browser_config(self):
        return self.config.get("browser", {})
