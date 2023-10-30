import pytest
from main import *


# Teste para a função "Hello"
def teste_hello():
    assert hello() == "Hello World!"
