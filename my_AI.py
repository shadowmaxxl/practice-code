from ollama import chat 
from ollama import ChatResponse
from ollama import generate

ollama.generate(model='openchat', prompt='why coding so hard?')