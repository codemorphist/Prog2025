import json
import requests
import xml.etree.ElementTree as ET


def get_html(url: str) -> str:
    responce = requests.get(url)
    return responce.text


def wordcount(text: str) -> dict[str, int]:
    # for delim in ".,?!\"'/\\`":
    #     text = text.replace(delim, "")

    # text = text.lower()
    words = text.split()

    counts = {}

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
         
    return counts


def generate_wordcount_json(counts: dict[str, int]) -> str:
    counts_json = []

    for word, count in counts.items():
        counts_json.append({
            "word": word,
            "count": count,
        })

    return json.dumps(counts_json)


def generate_wordcount_xml(counts: dict[str, int]) -> str:
    root = ET.Element("words")

    for word, count in counts.items():
        word_elem = ET.SubElement(root, "word", {"count": str(count)})
        word_elem.text = word

    xml = ET.tostring(root).decode() 
    return xml


if __name__ == "__main__":
    url = input("Input url: ")
    html = get_html(url) 
    counts = wordcount(html)
    print(generate_wordcount_xml(counts))
