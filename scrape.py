import click
import requests
from bs4 import BeautifulSoup

@click.command()
@click.option("--url","-u",help='your url is')
def main(url):
    res = input(url)
    print(url)
    res = requests.get(url)
    txt = res.text
    status = res.status_code
    print(txt, status)
    soup = BeautifulSoup(res.content, 'html.parser')
    first_h1 = soup.select('h1')[0].text
    all_h1_tags = []
    for element in soup.select('h2'):
        all_h1_tags.append(element.text)
    seventh_p_text = soup.select('p')[6].text

    print(all_h1_tags, seventh_p_text)
    all_links = []


    links = soup.select('a')
    for ahref in links:
        text = ahref.text
        text = text.strip() if text is not None else ''

        href = ahref.get('href')
        href = href.strip() if href is not None else ''
        all_links.append({"href": href, "text": text})

    print(all_links)


if __name__ == "__main__":
    main()

