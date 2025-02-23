import pandas as pd
import requests

# 知乎热榜URL
headers = {
'accept':'*/*',
'accept-encoding':'gzip, deflate, zstd',
'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
'cookie':'_xsrf=cpUq2e0mDXwLcTf4qJj6EeDCOsewViCO; _zap=4069a66f-e0cc-42fd-bf82-eb7a50692554; d_c0=ADAS372LjhmPThW7ggAPBm5K0-CjQPhO9Qw=|1731842820; _ga=GA1.2.183582069.1738549475; captcha_session_v2=2|1:0|10:1738549480|18:captcha_session_v2|88:dkd4cTVJQUF1V25GRWZtektpRkJTU1A3aWpyU3hGZkZ0eEErSnQyZFhYSDVERWU5NXBJbzFDN1E3anRxWExPYg==|63c6731fc341fae78f4b59a18d23ff2e4196398dd623219dd1e9ab3d95515d9c; __snaker__id=BeWkzb1iBw9CNABW; gdxidpyhxdE=EwxmjoIjJS6kfXN9N%5C28LDbVvZtGbnr1j%5CNU08YKuwrKsDxL5bl6G9y2KgBxy0M5BI%2B74E6l8PSlWavK6YxS4ytKOqnrZvGLGgi%2BuA50wnNlW9%2FqZwRKrVbPB%2BhgJlEeowTvBrl8JR7hgp6OSfT2mPH7UsjNa8%5CPL2da3XwPxUvTS6%2BP%3A1738550380562; q_c1=94f43ea97aa941088c1e3f3b6baf0d74|1738549503000|1738549503000; __zse_ck=004_25P3lwkKa==CTPaJ6PqtPmGNEVUStevmL/KmLIOv=UhyLELZaodTU=kK61p7speErR35TeJ2=1GKTzGUFBEZIlgCKWm4mM4HtQ5L1cJ3TZYVuuPhe5iCMmzDgmRMMJDE-vxTbXdiQduftgjs94p5zn1jV6Q228Y1d9owXX8EyybffByjGGhoicYocNo5a1Gl2d4H6L087zncAkITfVAYVwTdGHMr1rIOGuaqA486NJRLrHYWztl2sZ+fzozVPifqE; z_c0=2|1:0|10:1739968710|4:z_c0|92:Mi4xZHltZFV3QUFBQUFBTUJMZnZZdU9HUmNBQUFCZ0FsVk5fM2FOYUFBcnNfcGpfQ0toY3Q5MWgwT0JIcXJvenVvY2p3|2b8fd98275ae99711b30a3b6d5eb17a67d103f8efee92fccbef7601659a6f799; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1738549474,1738560675,1739968705,1740052402; HMACCOUNT=98ED63D383EC70DF; tst=h; SESSIONID=SRPpETkoXfAtoz8IrViKcZ08jrwg4Ans3URiGi7GaJg; JOID=V1wTAUso58BL623dQy-jEaxS4VdZereUOas4tCh1gIM7hhLkCEX_cSvvbttFScd6B9crV7orxfhYlqv0WUHW5dc=; osd=V1oUB00o4cdN7W3bRCmlEapV51FZfLCSP6s-sy5zgIU8gBTkDkL5dyvpad1DScF9AdErUb0tw_heka3yWUfR49E=; BEC=5ee33e0856ed13c879689106c041a08d; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1740054218; unlock_ticket=AGDSLmOt1BgXAAAAYAJVTdElt2d9ERI4RI7Y2kcDQH8vme43j0lF_w==',
'priority':'u=1, i',
'referer':'https://www.zhihu.com/hot',
'sec-ch-ua':'"Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'sec-fetch-dest':'empty',
'sec-fetch-mode':'cors',
'sec-fetch-site':'same-origin',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36',
'x-api-version':'3.0.76',
'x-requested-with':'fetch',
'x-zse-93':'101_3_3.0',
'x-zse-96':'2.0_=V8iKL5TnM/PcM3nVmCSDSj3CrZ8DCytiTHvzWRMnB/SlDS4DWaYuBMGMGnPNZ1u',
'x-zst-81':'3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZB0Y0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPFHN0m9pfLhC12gOOADwBsMgqIhrq6qVKeAOqwUXL9cHfhGLBpwt9bcN_eTeTvLeXeTgB5GCK2Ae1gUOGo9p0TCgMwbL_b8LfY9L0ywxMSqwBcQL_XJxCiGxyCqSBjC2L2ckMMRcLtBNB1Bexc8wMZCXmJgNLnqYso6XBh92mQiU_CvSxOqfzf_VqfbOC8Ut_UJNOfBNK-DUMOB3XyhLyQqxCyhXBUCVGYCxyNCc_3UgLiU28hUOyKgoMcT98qUC1oLxBYQxqOJ98xhoLthc8XhtqhbeMc0oBWwLC1XYC',
}
url = 'https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total?limit=50&desktop=true'
# 发送HTTP GET请求
response = requests.get(url=url, headers=headers)
# 查看响应码
print(response.status_code)
#用json接受请求数据
json_data = response.json()
#定义空列表
order_list = [] # 热搜排名
title_list = [] # 热搜标题
desc_list = [] #热搜描述
url_list = [] #热搜链接
hot_value_list = [] #热度值
answer_count_list = [] # 回答数
data_list = json_data['data']
order = 1
for data in data_list:
    # 热搜排名
    order_list.append(order)
    # 热搜标题
    title = data['target']['title_area']['text']
    print(order,'热搜标题：',title)
    title_list.append(title)
    # 热搜描述
    desc_list.append(data['target']['excerpt_area']['text'])
    #热搜链接
    url_list.append(data['target']['link']['url'])
    #热度值
    hot_value_list.append(data['target']['metrics_area']['text'])
    #回答数
    answer_count_list.append(data['feed_specific']['answer_count'])
    order +=1
df = pd.DataFrame(
    {
        '热搜排名': order_list,
        '热搜标题': title_list,
        '热搜链接': url_list,
        '热度值': hot_value_list,
        '回答数': answer_count_list,
        '热搜描述': desc_list,
    }
)
#保存结果到csv文件
df.to_csv('知乎热搜.csv', index=False, encoding='utf_8_sig')
print('爬取结束')