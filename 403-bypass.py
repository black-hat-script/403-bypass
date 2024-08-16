import requests
from bs4 import BeautifulSoup
import re
import urllib.parse as urlparse
from termcolor import colored

# Banner function
def generate_banner():
    header = colored(' ***************403 BYPASS****************', 'blue', 'on_grey', ['bold'])
    print(header)
    header = colored(' github: https://github.com/black-hat-script', 'red', 'on_grey', ['bold'])
    print(header)
    header += colored('facebook: https://www.facebook.com/profile.php?id=Rakesh%20Sarkar', 'red', 'on_grey', ['bold'])
    script_msg = colored(' ************BLACK-HAT-SCRIPT*************', 'green', 'on_grey', ['bold', 'blink'])
    print(script_msg)

if __name__ == '__main__':
    generate_banner()


# Extract links function
def extract_links(url, num_links):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        all_anchors = soup.find_all('a')
        extracted_links = []
        for anchor in all_anchors:
            href = anchor.get('href')
            if href:
                href = urlparse.urlsplit(href).scheme + "://" + urlparse.urlsplit(href).netloc + urlparse.urlsplit(href).path
                if re.match(r'^(?:http|ftp)s?://', href) and href not in extracted_links:
                    extracted_links.append(href)

        # Return the first 'num_links' links
        return extracted_links[:num_links]
    else:
        print("Failed to extract links. Status code:", response.status_code)
        return []

url = input(colored("Enter the URL: ", 'yellow'))
num_links = int(input(colored("Enter the number of links to extract: ", 'yellow')))
extracted_links = extract_links(url, num_links)
print(colored(f"Number of extracted links: {len(extracted_links)}", 'green'))
for index, link in enumerate(extracted_links):
    print(colored(f"{index+1}. {link}", 'cyan'))