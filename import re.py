import re

texts = [
    "FROM <alas@gmail.com>",
    "to anna <anana@banana.com>",
    "fromer, toer <shakala@boomboom>",
    "lala <alala.com>"
]

# Pattern to match <some text with @ in it>
pattern = r"<[^<>]*@[^<>]*>"

import re

texts = [
    "FROM <alas@gmail.com>",
    "to anna <anana@banana.com>",
    "fromer, toer <shakala@boomboom>",
    "lala <alala.com>"
]

# Pattern to match <some text with @ in it>
pattern = r"<[^<>]*@[^<>]*>"

for text in texts:
    match_ = re.search(pattern, text)
    if match_:
        email = match_.group(0)
        print(f"Found: {email}")