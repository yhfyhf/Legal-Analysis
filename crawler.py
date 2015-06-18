# encoding: utf-8
import requests
from lxml.html import soupparser
import MySQLdb
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)



def init_db():
    conn = MySQLdb.connect('localhost', 'yhf', '123', 'legal', 3306, charset='utf8')
    return conn, conn.cursor()


def get_urls(index):
    if index == 0:
        url = "http://court.gov.cn/zgcpwsw/mshz"
    else:
        url = "http://court.gov.cn/zgcpwsw/mshz/index_%s.htm" % index
    html = get_html(url)

    soup = soupparser.fromstring(html)
    uls = soup.xpath('//*[@id="bottom_right_con_five_xsaj"]/div/ul')
    urls = []
    for ul in uls:
        url = ul.xpath('li/div/div[2]/a/@href')[0]
        url = "http://court.gov.cn/zgcpwsw/" + url[3:]
        urls.append(url)

    return urls
    # div = soup.xpath("//div[@class='bottom_right_con_five_list']")[0]
    # for ul in div.xpath("ul"):
    #   div = ul.xpath("li/div")[0]
    #   court = div.xpath("div/@style")[0].encode('utf-8').strip()
    #   print court


def get_html(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    return r.text


def parse_html(html):
    soup = soupparser.fromstring(html)
    body = soup.xpath("body")[0]
    div_wenshu = body.xpath("div[@id='wrap']/div[@id='wenshu']")[0]
    inner_table = div_wenshu.xpath("table[1]/tbody[1]/tr[1]/td[1]/div[@id='ws']/table")[0]


    try:
        first_tr, second_tr, third_tr, fourth_tr = inner_table.xpath("tr")

        idx = html.find("<HTML>")
        html = html[idx:]
        soup = soupparser.fromstring(html)
        contents =  soup.xpath("//text()")[:-50]
        contents = [content.encode('utf-8') for content in contents]
        content = "\n".join(contents).strip().encode('utf-8')

    except:
        first_tr, second_tr, third_tr, fourth_tr = inner_table.xpath("tr")[:4]

        idx = html.find("PrintArea")
        last_idx = html.find("td", idx)
        html = html[idx-74:last_idx+3].encode("utf-8")
        soup = soupparser.fromstring(html)
        contents =  soup.xpath("//text()")
        contents = [content.encode('utf-8').strip() for content in contents if len(content.strip()) != 0]
        content = "\n".join(contents).strip().encode('utf-8')

    title = first_tr.xpath("td/div[@id='wsTitle']/text()")[0].encode('utf-8')
    time = second_tr.xpath("td/div[@id='wsTime']/span/text()")[0].encode('utf-8')[-10:]
    court = content.split('\n')[0].encode('utf-8')
    return title, time, court, content


def insert_into_db(cur, conn, id, url, title, time, court, content):
    try:
        sql = 'replace into judgement values (%s, "%s", "%s", "%s", "%s", "%s")' % (id, url, title, time, court, content)
        cur.execute(sql)

    except Exception, e:
        sql = '''
            replace into error values (%s, "%s")
        '''
        cur.execute(sql, (id, str(Exception)+": "+str(e)))
    conn.commit()



if __name__ == '__main__':
    url = "http://court.gov.cn/zgcpwsw/hen/hnsnyszjrmfy/nyswlqrmfy/ms/201503/t20150318_6958292.htm"
    # url = "http://court.gov.cn/zgcpwsw/hen/hnszzszjrmfy/xmsrmfy/ms/201503/t20150319_6964856.htm"
    # url = "http://court.gov.cn/zgcpwsw/ah/ahshsszjrmfy/sxrmfy/ms/201503/t20150319_6971039.htm"
    # r = requests.get("http://court.gov.cn/zgcpwsw/bt/xjscjsbtdseszjrmfy/wlmqkqrmfy/ms/201503/t20150313_6914630.htm")
    # r = requests.get("http://court.gov.cn/zgcpwsw/ah/ahshsszjrmfy/sxrmfy/ms/201503/t20150318_6958316.htm")
    # html = get_html(url)
    # title, time, text = parse_html(html)
    # print title, "\n", time, "\n", text


    # for i in xrange(5):
    #   get_urls(i)

    conn, cur = init_db()

    for i in xrange(1000, 1500):
        urls = get_urls(i)
        print i
        for url in urls:
            url = url[:]
            id = url.split('_')[-1].split('.')[0]
            html = get_html(url)
            title, time, court, content = parse_html(html)

            insert_into_db(cur, conn, id, url, title, time, court, content)
            # print id
            # print id, "\n", url, "\n", title, "\n", time, "\n"#, content
