from urllib.request import urlopen

def readFileURLSting(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)
    return decoded_html

data_str = readFileURLSting("https://www.gutenberg.org/files/11/11-0.txt")
print(data_str)

