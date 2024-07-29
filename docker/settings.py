import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.a = os.getenv('a')
        self.b = os.getenv('b')
        self.c = os.getenv('c')
        self.d = os.getenv('d')
        self.e = os.getenv('e')
        self.f = os.getenv('f')
        self.g = os.getenv('g')

    def get_attribute(self, key):
        return getattr(self, key, None)

settings = Settings()