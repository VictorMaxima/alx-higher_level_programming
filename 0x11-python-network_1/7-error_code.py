#!/usr/bin/python3
"""
  sends a request to the url, displays the body of the response.
"""
import requests
from sys import argv


def main(argv):
    """
    Method that manage urllib.error.HTTPError exceptions,
    print: Error code: followed by the HTTP status code
    """
    url = argv[1]
    r = requests.get(url)
    if r.status_code == requests.codes.ok:
        print(r.text)
    else:
        print("Error code: {}".format(r.status_code))


if __name__ == "__main__":
    main(argv)