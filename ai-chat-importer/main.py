import json
import sys
from playwright.sync_api import sync_playwright

from parsers.gemini import parse_gemini
from parsers.chatgpt import parse_chatgpt
from parsers.claude import parse_claude
from parsers.perplexity import parse_perplexity


def detect_platform(url):

    if "gemini" in url:
        return "gemini"

    if "chatgpt" in url or "openai" in url:
        return "chatgpt"

    if "claude" in url:
        return "claude"

    if "perplexity" in url:
        return "perplexity"

    return "unknown"


def fetch_html(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url, timeout=60000)

        page.wait_for_timeout(4000)

        html = page.content()

        browser.close()

        return html


def main():

    input_data = json.loads(sys.stdin.read())

    url = input_data["url"]

    platform = detect_platform(url)

    html = fetch_html(url)

    if platform == "gemini":
        result = parse_gemini(html)

    elif platform == "chatgpt":
        result = parse_chatgpt(html)

    elif platform == "claude":
        result = parse_claude(html)

    elif platform == "perplexity":
        result = parse_perplexity(html)

    else:
        result = {
            "title": "",
            "messages": []
        }

    result["platform"] = platform

    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()