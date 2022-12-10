from pydantic import BaseSettings
import os
import yaml
from pathlib import Path

basedir = Path(__file__).parent.resolve()
env = os.getenv("ENV", "dev")
config_yaml_path = Path(basedir / f"{env}-config.yaml")
print(f"using config: {config_yaml_path}")


class Config(BaseSettings):
    SQLALCHEMY_DATABASE_URI: str
    SECRET_KEY: str
    LOG_LEVEL: str


config_dict = yaml.safe_load(config_yaml_path.read_text(encoding="utf-8"))
settings = Config(**config_dict)

