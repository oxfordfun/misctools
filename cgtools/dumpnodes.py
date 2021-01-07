import requests

if __name__ == "__main__":
    r = requests.get("http://localhost:6000/status").json()
    print('\n'.join(r["nodes"].keys()))
