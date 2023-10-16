import argparse
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

def track_resources(url, headers=None):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(f"Request to {url} was successful!")

            print("Response Headers:")
            for key, value in response.headers.items():
                print(f"{key}: {value}")

            soup = BeautifulSoup(response.text, 'html.parser')

            for tag in soup.find_all(['img', 'script', 'link']):
                if tag.has_attr('src'):
                    resource_url = tag['src']
                elif tag.has_attr('href'):
                    resource_url = tag['href']
                else:
                    continue

                resource_domain = urlparse(resource_url).netloc

                print(f"Resource URL: {resource_url}")
                print(f"Resource Domain: {resource_domain}")
                print("---")
        else:
            print(f"Request to {url} failed with status code {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Track resources from a URL with custom headers.")
    parser.add_argument("-u", "--url", required=True, help="URL to track resources")
    parser.add_argument("-heads", "--headers", help="Custom headers as a comma-separated list")

    args = parser.parse_args()

    url_to_track = args.url
    custom_headers = args.headers

    headers = {}
    if custom_headers:
        for header in custom_headers.split(','):
            key, value = header.strip().split('=')
            headers[key] = value

    track_resources(url_to_track, headers)
