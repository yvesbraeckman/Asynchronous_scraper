import requests
import click
import asyncio
import aiohttp
import ssl
import certifi
from bs4 import BeautifulSoup
from collections import Counter
from spellchecker import SpellChecker
from urllib.parse import urljoin
from aiohttp import TCPConnector

spell = SpellChecker()

@click.command()
@click.argument('mode', type=click.Choice(['synchroon', 'asynchroon'], case_sensitive=False))
@click.argument('max_diepte', type=int)
@click.argument('url')
def main(mode, max_diepte, url):
    click.echo(f"Je hebt gekozen voor de modus: {mode}")
    click.echo(f"De maximale diepte is ingesteld op: {max_diepte}")
    click.echo(f"De ingevoerde URL is: {url}")

    if mode == 'synchroon':
        click.echo("Werken in synchrone modus...")
        synchronous(url, max_diepte)
    else:
        click.echo("Werken in asynchrone modus...")
        asyncio.run(asynchronous_search(url, max_diepte))

def synchronous(url, max_depth):
    counter = Counter()
    visited = set()
    visit_page(url, counter, visited, max_depth)
    print("Woordfrequenties over alle pagina's:")
    print(counter.most_common(25))


async def asynchronous_search(url, max_depth):
    counter = Counter()
    visited = set()
    ssl_context = ssl.create_default_context(cafile=certifi.where())

    async with aiohttp.ClientSession(connector=TCPConnector(ssl=ssl_context)) as session:
        await async_visit_page(session, url, counter, visited, max_depth)

    print("Woordfrequenties over alle pagina's:")
    print(counter.most_common(25))


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
            visit_page(absolute_url, counter, visited, max_depth, depth + 1)

    except (requests.RequestException, Exception) as e:
        print(f"Fout bij het bezoeken van {url}: {e}")


async def async_visit_page(session, url, counter, visited, max_depth, depth=0):
    if depth > max_depth:
        return

    if url in visited:
        return

    visited.add(url)

    try:
        async with session.get(url, timeout=50) as response:
            if response.status == 200:
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")

                woorden = list(spell.split_words(soup.get_text().lower()))
                counter.update(woorden)

                tasks = []
                for link in soup.find_all('a', href=True):
                    absolute_url = urljoin(url, link['href'])
                    tasks.append(asyncio.create_task(async_visit_page(session, absolute_url, counter, visited, max_depth, depth + 1)))

                await asyncio.gather(*tasks)
    except aiohttp.ClientError as e:
        print(f"Fout bij het bezoeken van {url}: {e}")
    except Exception as e:
        print(f"Fout bij het bezoeken van {url}: {e}")


if __name__ == '__main__':
    main()


