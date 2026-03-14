from bs4 import BeautifulSoup


def parse_chatgpt(html):

    soup = BeautifulSoup(html, "html.parser")

    messages = []

    for user in soup.select(".user-message"):

        messages.append({
            "role": "user",
            "content": user.get_text(strip=True)
        })

    for ai in soup.select(".assistant-message"):

        messages.append({
            "role": "assistant",
            "content": ai.get_text(strip=True)
        })

    return {
        "title": "ChatGPT Conversation",
        "messages": messages
    }