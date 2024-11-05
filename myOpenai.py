import os, json
import openai
from openai import OpenAI
from decouple import config
openai.api_key = config("OPENAI_API_KEY")
# openai.organization="org-BPfWYdVCzqZ3ad5b5N6Ov4as"

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)

prompt = "Convert the movie '{movie}' into emojis."
examples = [
{ "input": "Titanic", "output": "🛳️🌊❤️🧊🎶🔥🚢💔👫💑" },
{ "input": "The Matrix", "output": "🕶️💊💥👾🔮🌃👨🏻‍💻🔁🔓💪" }
]
movie = "Toy Story"
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt.format(movie=examples[0]
    ["input"])},
    {"role": "assistant", "content": examples[0]["output"]},
    {"role": "user", "content": prompt.format(movie=examples[1]
    ["input"])},
    {"role": "assistant", "content": examples[1]["output"]},
    {"role": "user", "content": prompt.format(movie=movie)},
    ]
)
print(response.choices[0].message)