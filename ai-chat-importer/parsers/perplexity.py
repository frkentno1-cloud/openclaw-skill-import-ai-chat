from bs4 import BeautifulSoup


def parse_perplexity(html):

    soup = BeautifulSoup(html, "html.parser")

    messages = []

    for block in soup.select(".query"):

        messages.append({
            "role": "user",
            "content": block.get_text(strip=True)
        })

    for block in soup.select(".answer"):

        messages.append({
            "role": "assistant",
            "content": block.get_text(strip=True)
        })

    return {
        "title": "Perplexity Conversation",
        "messages": messages
    }