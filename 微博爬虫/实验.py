import pandas as pd
import requests
from bs4 import BeautifulSoup

url2='https://weibo.com/hot/search'
headers={
'accept':'*/*',
'accept-encoding':'gzip, deflate, br, zstd',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
'client-version':'v2.47.33',
'cookie':'SCF=Av9BWkaCpsCmNvuptA44ZfQAckqKT6VkiKzo7-I_Jo-btXL4bj96PByHMMDCKC9-3FdM5sd6H7uUkGX92RK0-nI.; SUB=_2A25KvRFYDeRhGeFH6FQR8CjMwj2IHXVpsyyQrDV8PUNbmtAbLRPekW9Ne075lxOKgu18wLGjfTSIagVdvOAPCKkf; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh-1YifUB1G7gYGw1w1EPHV5JpX5KzhUgL.FoM4e0q7ehq71K22dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMN1Keceh5ceh.p; ALF=02_1742794248; SINAGLOBAL=2894409805550.067.1740202261659; UOR=,,www.baidu.com; WBPSESS=rw2x7tVBdr5Q2VmEDtsu8N-fk31fl-2h0d2iHnBMnpDCAdwDTkwTMPd-xGbuKMrJHh5K0f2kj_HDjlC9JE_fiNegRVF3eGH5J0xdRMcJ1_fm9E1DxwkzCYaMnQNlLlPka7OdH1l2rUXR-cdQ5AqaPg==; _s_tentry=www.baidu.com; Apache=5180292759917.549.1740292896438; ULV=1740292896439:2:2:1:5180292759917.549.1740292896438:1740202261668',
'priority':'u=1, i',
'referer':'https://weibo.com/hot/search',
'sec-ch-ua':'"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'Windows',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'server-version':'v2025.02.21.1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
'x-requested-with':'XMLHttpRequest',
}
r2=requests.get('https://weibo.com/hot/search',headers = headers)
html = r2.text
soup = BeautifulSoup(html,"html.parser")
search_list=soup.findAll("div",attrs={"class":"HotTopic_num_1H-j8"})
for search in search_list:
    print(search)
