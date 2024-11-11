import re

url = input("URL: ").strip()

if matches := re.search(r"x.com/(.+)$", url):
    username = matches.group(1)

print(f"hello, {username}")
