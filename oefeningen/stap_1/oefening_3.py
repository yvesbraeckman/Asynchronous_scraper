import requests

base_url = "http://localhost:3000"

def lookup():
    id = int(input("welke post wil je zien: "))
    post = requests.get(f"{base_url}/posts", params={"id":id})
    post = post.json()[0]

    comments = requests.get(f"{base_url}/comments", params={"postId": id})
    comments = comments.json()

    print(f"{post['title']} (views: {post['views']} views)")
    for i in range(len(comments)):
        comment = comments[i]
        print(f"- {comment['text']}")


if __name__ == "__main__":
    lookup()