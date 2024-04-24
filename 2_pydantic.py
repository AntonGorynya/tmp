from datetime import datetime
from pydantic import BaseModel, validator, BaseSettings, ConfigDict

from string import digits
from environs import Env
import json


DIGITS = frozenset(digits)


class SubModel(BaseModel):
    v1: str
    v2: str
    v3: int


class Settings(BaseSettings):
    class Config:
        env_nested_delimiter = '__'

    auth_key: str
    api_key: str
    sub_model: SubModel
    sub_model2: SubModel | None


class Settings_from_env(BaseSettings):
    auth_key: str
    api_key: str


class Tag(BaseModel):
    id: int
    text: str


# Написать вложенную схему валидации данных, получить ошибки валидации
class Goods(BaseModel):
    id: int
    name: str
    price: float


class Order(BaseModel):
    id: int
    created_at: datetime | None
    goods: list[Goods]

    @validator('goods')
    def goods_in_not_empty(cls, goods):
        if goods:
            return goods
        raise ValueError('list of goods is empty')


class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None
    orders: list[Order]
    tags: list[Tag] | None

    @validator('name')
    def name_without_digits(cls, name):
        if not set(name) & DIGITS:
            return name
        raise ValueError('Digits in name')


external_data = {
    'id': '123',
    'name': 'Anton',
    'signup_ts': '2019-06-01 12:22',
    'orders': [
        {
            'id': 1,
            'goods': [
                {
                    'id': 1,
                    'name': 'Potato',
                    'price': 1.0
                 }
            ]
        },
    ],
}
user = User(**external_data)

# Экспортировать данные в формат JSON с помощью Pydantic
print(user.json())

# Прочитать данные из JSON с помощью Pydantic
user2 = User.parse_raw(json.dumps(external_data))
print(user2)

# Написать вложенную схему валидации переменных окружения (настройки приложения), получить ошибки валидации

# чтение из .env
settings_env = Settings_from_env(_env_file='.env', _env_file_encoding='utf-8')
print(settings_env)

# из переменных окружения
env = Env()
env.read_env()
settings = Settings()
print(settings)
