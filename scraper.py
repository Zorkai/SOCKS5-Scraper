from fake_useragent import UserAgent
from requests import get
from re import findall

ua = UserAgent()

def get_proxies(url):
    text = ""
    response = get(url, headers={'User-Agent': ua.random})
    content = response.text.replace("<span> : </span> <em>", ":")
    content = content.replace("</td><td>", ":")
    for proxy, port in findall('((?:\d{1,3}\.){3}\d{1,3}):(\d+)', content):
        text += proxy + ":" + port + "\n"
    print("+", len(text.splitlines()))
    return text

proxies = [
    get_proxies('https://api.proxyscrape.com/?request=getproxies&proxytype=socks5&timeout=10000&country=all'),
    get_proxies('https://proxysource.org/api/proxies/getWorkingProxies?apiToken=17580e4438910c287cef15dca10b7912a26&latencyMax=15000&latencyMin=0&outputMode=plaintext&uptimeMax=100&uptimeMin=30'),
    "\n".join(
    get_proxies(
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
    ).splitlines()[2:]),
    get_proxies('https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt'),
    "\n".join(
    get_proxies(
        "https://www.freeproxychecker.com/result/socks5_proxies.txt"
    ).splitlines()[7:]),
    get_proxies('https://multiproxy.org/txt_all/proxy.txt'),
    get_proxies('http://rootjazz.com/proxies/proxies.txt'),
    get_proxies('http://ab57.ru/downloads/proxyold.txt'),
    get_proxies('https://www.proxy-list.download/api/v1/get?type=socks5'),
    get_proxies('https://www.proxyscan.io/download?type=socks5'),
    get_proxies('http://proxydb.net/?protocol=socks5'),
    get_proxies('https://kabak.top/socks5'),
    get_proxies('https://hidemy.name/en/proxy-list/?type=5#list'),
    get_proxies('https://www.socks-proxy.net/'),
    get_proxies('https://www.my-proxy.com/free-socks-5-proxy.html')
    ]

open("output.txt", "w").write('\n'.join(proxies))
