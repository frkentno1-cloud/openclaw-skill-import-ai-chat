from bs4 import BeautifulSoup


def parse_gemini(html):

    soup = BeautifulSoup(html, "html.parser")

    messages = []

    for block in soup.select('[data-message-author-role="user"]'):

        messages.append({
            "role": "user",
            "content": block.get_text(strip=True)
        })

    for block in soup.select('[data-message-author-role="assistant"]'):

        messages.append({
            "role": "assistant",
            "content": block.get_text(strip=True)
        })

    return {
        "title": "Gemini Conversation",
        "messages": messages
    }