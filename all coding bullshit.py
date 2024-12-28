import ollama
from ollama import generate

def new_func():
    ollama.generate(model='openchat', prompt='why is games fun?')

new_func()
