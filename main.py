import requests
import click
from bs4 import BeautifulSoup
from collections import Counter
from spellchecker import SpellChecker
from urllib.parse import urljoin

spell = SpellChecker()

@click.group()
def cli():
    pass

def visit_page(url, counter, visited, max_depth, depth=0):
    if depth > max_depth:
        return

    if url in visited:
        return

    visited.add(url)

    try:
        r = requests.get(url, timeout=5)
        soup = BeautifulSoup(r.text, "html.parser")

        woorden = list(spell.split_words(soup.get_text().lower()))
        counter.update(woorden)

        for link in soup.find_all('a', href=True):
            absolute_url = urljoin(url, link['href'])
            visit_page(absolute_url, counter, visited, depth + 1, max_depth)

    except (requests.RequestException, Exception) as e:
        print(f"Fout bij het bezoeken van {url}: {e}")


@cli.command()
@click.argument("url")
@click.argument("max_depth")
def syncronous(url, max_depth):
    counter = Counter()
    visited = set()

    visit_page(url, counter, visited, max_depth)

    print("Woordfrequenties over alle pagina's:")
    print(counter)


@cli.command()
@click.argument("url")
@click.argument("max_depth")
def asynchronous(url, max_depth):
    raise NotImplementedError("code moet nog geschreven worden")

if __name__ == "__main__":
    cli()
