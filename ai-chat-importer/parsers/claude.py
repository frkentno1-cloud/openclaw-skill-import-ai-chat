from bs4 import BeautifulSoup


def parse_claude(html):

    soup = BeautifulSoup(html, "html.parser")

    messages = []

    for block in soup.select(".human"):

        messages.append({
            "role": "user",
            "content": block.get_text(strip=True)
        })

    for block in soup.select(".assistant"):

        messages.append({
            "role": "assistant",
            "content": block.get_text(strip=True)
        })

    return {
        "title": "Claude Conversation",
        "messages": messages
    }