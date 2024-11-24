import requests

def add_post():
    title = input("titel: ")
    views = int(input("views: "))
    data = {"title": title, "views": views}
    r = requests.post("http://localhost:3000/posts", json=data)

def add_comment():
    try:
        post_id = input('Voor welke post wil je een comment toevoegen? (Voer het post-ID in) ')
        text = input('Voer de tekst van de comment in: ')
        r = requests.get(f"http://localhost:3000/posts/{post_id}")
        r.raise_for_status()
        if r.status_code == 404:
            print("Post met dit ID bestaat niet.")
            return

        new_comment = {
            "text": text,
            "postId": post_id
        }
        response = requests.post(f"http://localhost:3000/comments", json=new_comment)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Er is een fout opgetreden: {e}")


if __name__ == "__main__":
    while True:
        print("wat wil je doen?")
        print("1. Een nieuwe post maken")
        print("2. Een comment toevoegen aan een bestaande post")
        print("3. Stoppen")
        keuze = int(input("keuze: "))

        if keuze == 1:
            add_post()
        elif keuze == 2:
            add_comment()
        else:
            break