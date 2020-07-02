import string
import random

def random_string(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def convert(url):
    if(url[-1]=='/'):
        url=url[:-1]
    if url.startswith('http://www.'):
        return 'http://' + url[len('http://www.'):]
    if url.startswith('www.'):
        return 'http://' + url[len('www.'):]
    if url.startswith('https://www.'):
        return 'http://' + url[len('https://www.'):]
    if not url.startswith('http://') and not url.startswith('https://'):
        return 'http://' + url
    return url