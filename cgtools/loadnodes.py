import requests, sys

if __name__ == "__main__":
    for line in sys.stdin:
        url = f"http://localhost:6000/add_node/{line.strip()}"
        requests.get(url)
