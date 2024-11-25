from bs4 import BeautifulSoup

def main():
    html_pad = input("Geef het pad naar het HTML-bestand op: ")

    with open(html_pad, 'r', encoding='utf-8') as html_file:
        inhoud = html_file.read()
        soup = BeautifulSoup(inhoud, 'html.parser')
        jpg_links = [img['src'] for img in soup.find_all('img') if 'src' in img.attrs and img['src'].lower().endswith('.jpg')]
        for link in jpg_links:
            print(link)


if __name__ == "__main__":
    main()
