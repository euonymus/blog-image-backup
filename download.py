import requests, bs4
import urllib.request
import urllib.error

month = '06'
subdomain = 'deutsch'
# directory = 'https://turkey.euonymus.info/wp-content/uploads/2014/'
directory = 'https://' + subdomain + '.euonymus.info/wp-content/uploads/2013/'

def download():
    # res = requests.get('08.html')
    # res.raise_for_status()
    # html_text = res.text

    path = subdomain + '/' + month + '.html'
    f = open(path)
    html_text = f.read()

    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    elems = soup.select('a')
    for elem in elems:
        file_name = elem.get('href')
        image_path = directory + month + '/' + file_name
        print(image_path)
        try:
            req = urllib.request.Request(image_path)
            req.add_header('Referer', 'https://www.bluehost.com/')
            req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; NP06; rv:11.0) like Gecko')

            with urllib.request.urlopen(req) as web_file:
                data = web_file.read()
                with open(subdomain + '/' + month + '/' + file_name, mode='wb') as local_file:
                    local_file.write(data)

        except urllib.error.URLError as e:
            print(e)
if __name__ == "__main__":
    download()


