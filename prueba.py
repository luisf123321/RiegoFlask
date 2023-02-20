import requests


def run():
    response = requests.get('http://192.168.3.102:5000/')
    print(type(response))
    print(response)


if __name__ == "__main__":
    run()
