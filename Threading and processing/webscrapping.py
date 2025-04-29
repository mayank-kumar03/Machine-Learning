import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://python.langchain.com/docs/introduction/',
    'https://python.langchain.com/docs/tutorials/',
    'https://python.langchain.com/docs/how_to/pydantic_compatibility/'
]

def fetch_content(url):
    response = requests.get(url)  # Corrected variable name
    soup = BeautifulSoup(response.content, 'html.parser')  # Fixed typo in BeautifulSoup
    print(f"Fetched {len(soup.text)} chars from {url}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All pages are fetched")

