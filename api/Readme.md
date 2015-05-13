# `GET` `api/articles`

Returns a collection of the 10 most recent articles. Can be specified by court name. 

### Parameters

Parameter | Required / Optional                | Value
---------|--------------------------|-----------
`offset`   |  Optional, default 0   | int
`limit`    |  Optional, default 50  | int
`sortby`   |  Optional, default 'desc'| 'asc', 'desc'
`court`    |  Optional, default null | string

### Return
``` json
{
	"articles" : [
	 	{
	 		"court": string,
	 		"id": integer,
	 		"time": string,
	 		"title": string,
	 		"text": string,
	 		"url": string
	 	},
	 	...
	 	...
	 ],
	 "limit": integer,
	 "offset": integer,
	 "sortby": string,
	 "total": integer 
}
```

### Examples

``` bash
curl http://127.0.0.1:5000/api/articles/?offset=10&limit=5&sortby=asc
```

``` json
{
  "articles": [
    {
      "court": "内蒙古自治区呼伦贝尔市中级人民法院", 
      "id": 7121361, 
      "text": "内蒙古自治区呼伦贝尔市中级人民法院\n民 事 裁 定 书\n（2015）呼民申字第2号\n再审申请人（一审被告）：中国人寿财产保险股份有限公司内蒙古自治区分公司呼伦贝尔市牙克石支公司，住所地内蒙古自治区牙克石市越桔东小区12A号楼1—10门市......", 
      "time": "2015-03-26", 
      "title": "人寿财产保险公司牙克石支公司与张亚军等三人机动车交通事故责任申请再审民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/nmg/nmgzzqhlbeszjrmfy/ms/201503/t20150326_7121361.htm"
    }, 
    {
      "court": "内蒙古自治区呼伦贝尔市中级人民法院", 
      "id": 7121364, 
      "text": "内蒙古自治区呼伦贝尔市中级人民法院\n民 事 裁 定 书\n（2014）呼民申字第53号\n再审申请人（一审被告、二审上诉人）：刘某某，男，蒙古族，个体司机，住内蒙古自治区鄂温克族自治旗。\n被申请人（一审原告、二审被上诉人）：刘某，......", 
      "time": "2015-03-26", 
      "title": "刘某某与刘某抚养费申请再审民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/nmg/nmgzzqhlbeszjrmfy/ms/201503/t20150326_7121364.htm"
    }, 
    {
      "court": "内蒙古自治区呼伦贝尔市中级人民法院", 
      "id": 7121376, 
      "text": "内蒙古自治区呼伦贝尔市中级人民法院\n民 事 裁 定 书\n（2015）呼民申字第9号\n再审申请人（一审被告）：尹德全，男，汉族个体工商户业主，住内蒙古自治区莫力达瓦达斡尔族自治旗。\n被申请人（一审原告）：刘敖，男，达斡尔族，......", 
      "time": "2015-03-26", 
      "title": "尹德全与刘敖、中国华安财产保险公司黑龙江分公司身体权申请再审民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/nmg/nmgzzqhlbeszjrmfy/ms/201503/t20150326_7121376.htm"
    }
  ], 
  "limit": "3", 
  "offset": "10", 
  "sortby": "asc", 
  "total": 29738
}   
```


``` bash
curl http://127.0.0.1:5000/api/articles/?offset=10&limit=3&sortby=asc&court=北京市朝阳区人民法院
```


``` json
{
  "articles": [
    {
      "court": "北京市朝阳区人民法院", 
      "id": 7241899, 
      "text": "北京市朝阳区人民法院\n民 事 判 决 书\n（2014）朝民初字第20907号\n原告上海凯利特实业有限公司北京分公司，住所地北京市朝阳区光华路七号汉威大厦1009单元。\n负责人尹炜，总经理。\n委托代理人李可，北京市永浩律师事务所律师......", 
      "time": "2015-04-02", 
      "title": "上海凯利特实业有限公司北京分公司与北京旺宏装饰设计有限公司承揽合同纠纷一审民事判决书", 
      "url": "http://court.gov.cn/zgcpwsw/bj/bjsdszjrmfy/bjscyqrmfy/ms/201504/t20150402_7241899.htm"
    }, 
    {
      "court": "北京市朝阳区人民法院", 
      "id": 7241900, 
      "text": "北京市朝阳区人民法院\n民 事 判 决 书\n（2015）朝民初字第02660号\n原告上海橡果网络技术发展有限公司，住所地上海市青浦区华新镇嘉松中路1135弄55号A-46，实际经营地北京市朝阳区高井文化产业园8号东亿国际传媒产业园C5号楼2层......", 
      "time": "2015-04-02", 
      "title": "上海橡果网络技术发展有限公司与周琳劳动争议一审民事判决书", 
      "url": "http://court.gov.cn/zgcpwsw/bj/bjsdszjrmfy/bjscyqrmfy/ms/201504/t20150402_7241900.htm"
    }, 
    {
      "court": "北京市朝阳区人民法院", 
      "id": 7241901, 
      "text": "北京市朝阳区人民法院\n民 事 裁 定 书\n（2015）朝民申字第00007号\n再审申请人（一审被告）：上海硕人广告企划有限公司。\n法定代表人：赵勇，总经理。\n委托代理人：史亮，女，1985年8月7日出生，汉族，上海硕人广告企划有限公司行政经理......", 
      "time": "2015-04-02", 
      "title": "上海硕人广告企划有限公司劳动争议申诉、申请民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/bj/bjsdszjrmfy/bjscyqrmfy/ms/201504/t20150402_7241901.htm"
    }
  ], 
  "limit": "3", 
  "offset": "10", 
  "sortby": "asc", 
  "total": 1400
}
```



# `GET` `api/article/:id`

Returns an article specified by article id. 

### Parameters

Parameter | Required / Optional                | Value
---------|--------------------------|-----------
`id`   |  Required   | int

### Return
``` json
{
  "article": {
    "court": string, 
    "id": integer, 
    "text": string, 
    "time": string, 
    "title": string, 
    "url": string
  }
}
```

### Examples
``` bash
curl http://127.0.0.1:5000/api/article/7241893
```

``` json
{
  "article": {
    "court": "北京市朝阳区人民法院", 
    "id": 7241893, 
    "text": "北京市朝阳区人民法院\n民 事 判 决 书\n（2014）朝民初字第21922号\n原告万控集团有限公司，住所地乐清市北白象镇温州大桥工业园区。\n法定代表人木晓东，董事长。\n委托代理人王者洁，女，1966年3月29日出生，万控集团有限公司职员......", 
    "time": "2015-04-02", 
    "title": "万控集团有限公司与北京北开中亚电气科技有限责任公司承揽合同纠纷一审民事判决书", 
    "url": "http://court.gov.cn/zgcpwsw/bj/bjsdszjrmfy/bjscyqrmfy/ms/201504/t20150402_7241893.htm"
  }
}
```





# `GET` `api/courts`

Returns a collection of 10 courts with the largest number of articles.

### Parameters

Parameter | Required / Optional                | Value
---------|--------------------------|-----------
`offset`   |  Optional, default 0   | int
`limit`    |  Optional, default 50  | int
`sortby`   |  Optional, default 'desc'| 'asc', 'desc'
`court`    |  Optional, default null | string

### Return
``` json
{
	"courts" : [
	 	{
	 		"court": string,
	 		"count": integer	 	
	 	},
	 	...
	 	...
	 ],
	 "limit": integer,
	 "offset": integer,
	 "sortby": string
}
```

### Examples

``` bash
curl http://127.0.0.1:5000/api/courts?offset=10&limit=5
```

``` json
{
  "courts": [
    {
      "count": 469, 
      "court": "北京市东城区人民法院"
    }, 
    {
      "count": 445, 
      "court": "山东省莱芜市莱城区人民法院"
    }, 
    {
      "count": 440, 
      "court": "北京市通州区人民法院"
    }, 
    {
      "count": 413, 
      "court": "江苏省宜兴市人民法院"
    }, 
    {
      "count": 401, 
      "court": "福建省厦门市思明区人民法院"
    }
  ], 
  "limit": "5", 
  "offset": "10", 
  "sortby": "desc"
}
```


# `GET` `api/search`

Returns a collection of the 10 most match articles specified by a query.

### Parameters

Parameter | Required / Optional                | Value
---------|--------------------------|-----------
`title`   |  Optional, default null   | string
`text`    |  Optional, default null  | string

Note: You must specify query using either `title` or `text`.

### Return
``` json
{
	"articles" : [
	 	{
	 		"court": string,
	 		"id": integer,
	 		"time": string,
	 		"title": string,
	 		"text": string,
	 		"url": string
	 	},
	 	...
	 	...
	 ]
}
```

### Examples

``` bash
curl http://127.0.0.1:5000/api/search/?title=安徽
```

``` json
{
  "articles": [
    {
      "court": "安徽省合肥市蜀山区人民法院", 
      "id": 7200801, 
      "text": "安徽省合肥市蜀山区人民法院\n民 事 裁 定 书\n（2015）蜀民一初字第00694号\n原告：安徽信旺投资集团有限公司。\n法定代表人：蒋玉祥，该公司董事长。\n委托代理人：蔡国俊，安徽健友律师事务所律师。\n委托代理人......", 
      "time": "2015-04-01", 
      "title": "安徽信旺投资集团有限公司与安徽国美电器有限公司房屋租赁合同纠纷一审民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/ah/ahshfszjrmfy/hfsssqrmfy/ms/201504/t20150401_7200801.htm"
    }, 
    {
      "court": "安徽省合肥市包河区人民法院", 
      "id": 7205529, 
      "text": "安徽省合肥市包河区人民法院\n民 事 裁 定 书\n（2015）包民二初字第00418号\n原告：安徽兄弟物流有限公司。\n法定代表人：尹良波，总经理。\n被告：安徽省佳宝玩具（集团）有限公司。\n法定代表人：徐忠心，总经理。\n被告......", 
      "time": "2015-04-01", 
      "title": "安徽兄弟物流有限公司与安徽省佳宝玩具（集团）有限公司、徐忠心借款合同纠纷一审民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/ah/ahshfszjrmfy/hfsbhqrmfy/ms/201504/t20150401_7205529.htm"
    }, 
    {
      "court": "安徽省寿县人民法院", 
      "id": 7212111, 
      "text": "安徽省寿县人民法院\n民 事 判 决 书\n（2015）寿民二初字第00025号\n原告：安徽砼辉特种建材有限责任公司，住所地安徽省合肥市。\n法定代表人：刘永刚，该公司总经理。\n委托代理人：周志祥，男，1982年5月7日出生，汉族，安徽省六安市人......", 
      "time": "2015-04-01", 
      "title": "安徽砼辉特种建材有限责任公司与安徽省中振建设工程有限公司买卖合同一审判决书", 
      "url": "http://court.gov.cn/zgcpwsw/ah/ahslaszjrmfy/sxrmfy/ms/201504/t20150401_7212111.htm"
    },
    ...
    ...
  ]
}
```

``` bash
curl http://127.0.0.1:5000/api/search/?text=房产
```

``` json
{
  "articles": [
    {
      "court": "安徽省繁昌县人民法院", 
      "id": 7161224, 
      "text": "安徽省繁昌县人民法院\n民 事 判 决 书\n（2014）繁民一初字第01271号\n原告：方麦英，女，汉族，住芜湖市繁昌县。\n被告：芜湖红华房地产有限公司，住所地：繁昌县。\n法定代表人：马芳胜，该公司董事长。\n委托代理人......", 
      "time": "2015-03-28", 
      "title": "方麦英与芜湖红华房地产有限公司房屋买卖合同纠纷一审判决书", 
      "url": "http://court.gov.cn/zgcpwsw/ah/ahswhszjrmfy/fcxrmfy/ms/201503/t20150328_7161224.htm"
    }, 
    {
      "court": "安徽省繁昌县人民法院", 
      "id": 7161224, 
      "text": "安徽省繁昌县人民法院\n民 事 判 决 书\n（2014）繁民一初字第01271号\n原告：方麦英，女，汉族，住芜湖市繁昌县。\n被告：芜湖红华房地产有限公司，住所地：繁昌县。\n法定代表人：马芳胜，该公司董事长。\n委托代理人......", 
      "time": "2015-03-28", 
      "title": "方麦英与芜湖红华房地产有限公司房屋买卖合同纠纷一审判决书", 
      "url": "http://court.gov.cn/zgcpwsw/ah/ahswhszjrmfy/fcxrmfy/ms/201503/t20150328_7161224.htm"
    }, 
    {
      "court": "吉林省高级人民法院", 
      "id": 7232159, 
      "text": "吉林省高级人民法院\n民 事 裁 定 书\n（2014）吉民申字第740号\n再审申请人［一审原告（反诉被告）、二审上诉人］：翟晓波，男，汉族，住长春市。\n被申请人［一审被告（反诉原告）、二审被上诉人］......", 
      "time": "2015-04-02", 
      "title": "翟晓波与吉林省东华房地产开发有限责任公司房地产开发经营合同纠纷再审审查民事裁定书", 
      "url": "http://court.gov.cn/zgcpwsw/jl/ms/201504/t20150402_7232159.htm"
    },
    ...
    ...
  ]
}
```