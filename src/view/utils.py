import PTN
import requests
from bs4 import BeautifulSoup


def imdb_search(name: str) -> bool:
    """
    scrapes IMDb to find if the torrent contains mainstream media which is almost certainly under copyright
    :param name: torrent's name without its suffix
    :return: whatever the media was found in scrape
    """
    try:
        parsed_name = PTN.parse(name)
        query = f"{parsed_name['title']} {parsed_name['year'] if 'year' in parsed_name else ''}"
        url = f"https://www.imdb.com/search/title/?title={'%20'.join(query.split())}"

        response = requests.get(url, headers={'User-Agent': 'Bittorent_python v1.0.0'})
        soup = BeautifulSoup(response.text, 'html.parser')
        links = filter(lambda x: x.startswith('/title/'), map(lambda link: link.get('href'), soup.find_all('a')))
        if list(links):
            return True
    except:
        return False


def convert_seconds(seconds: float) -> str:
    units = [(31556952, 'y'), (2629746, 'm'), (604800, 'w'), (86400, 'd'), (3600, 'h'), (60, 'm'), (1, 's')]
    remaining_seconds = seconds
    result = ''
    displayed_units = 0

    for unit in units:
        value, label = unit
        if remaining_seconds >= value:
            count = int(remaining_seconds / value)
            result += f"{count}{label} "
            remaining_seconds %= value
            displayed_units += 1
            if displayed_units >= 2:
                break

    result = result.strip()
    if len(result) > 7:
        return '\u221e'  # infinity unicode
    return result


def convert_size(size: int) -> str:
    bytes_in_gib = 0.000000000931322574615478515625
    bytes_in_mib = 0.00000095367431640625
    bytes_in_kib = 0.0009765625
    if size * bytes_in_gib < 1:
        if size * bytes_in_mib < 1:
            return f"{round(size * bytes_in_kib, 2)} KiB"
        return f"{round(size * bytes_in_mib, 2)} MiB"
    return f"{round(size * bytes_in_gib, 2)} GiB"


def normalize(value: int, min_value: int, max_value: int):
    return (value - min_value) / (max_value - min_value)


def inverse_normalization(norm_value: float, min_value: int, max_value: int):
    return int((norm_value * (max_value - min_value)) + min_value)
