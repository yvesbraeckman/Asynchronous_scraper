from bs4 import BeautifulSoup


def main():
    locatie = input("Geef locatie evan HTML file: ")
    with open(locatie) as f:
        html = f.read()
        soup = BeautifulSoup(html ,"html.parser")
        print(soup.get_text())


if __name__ == "__main__":
    main()