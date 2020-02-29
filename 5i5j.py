import requests
from fake_useragent import UserAgent
from lxml import etree


class Zufang():
    def __init__(self):
        self.headers = {
            'User-Agent': str(UserAgent().random)
        }
        self.item = []

    def sent_request(self, page):
        response = requests.get('https://hz.5i5j.com/zufang/n' + str(page), headers=self.headers)
        html = response.content.decode('utf-8')
        self.parse(html)

    def parse(self, html):
        xml = etree.HTML(html)
        nodes = xml.xpath('//ul[@class="pList"]/li')

        for node in nodes:
            info = {}

            # 户型，面积，朝向，楼层，装修，建造时间
            list_1 = node.xpath('./div[2]/div[1]/p[1]/text()')[0].replace(" ", "").split("·")

            # 名称
            info['name'] = node.xpath('.//h3/a/text()')[0].strip()
            # 户型
            info['door_model'] = list_1[0]
            # 面积
            info['area'] = list_1[1].replace('平米', '')
            # 朝向
            info['toward'] = list_1[2]
            # 楼层
            info['floor'] = list_1[3]
            # 装修
            info['renovation'] = list_1[4]
            # 建造时间
            info['build_time'] = list_1[5]
            # 区域
            area_name = node.xpath('./div[2]/div[1]/p[2]/text()')[0].strip()
            info['area_name'] = self.change_area_name(area_name)
            # 小区名
            info['neighbourhood_name'] = node.xpath('./div[2]/div[1]/p[2]/a[1]/text()')[0].strip()
            # 16  人关注 · 近30天带看  0  次  ·  2020-02-20发布
            info['extra'] = node.xpath('./div[2]/div[1]/p[3]/text()')[0].strip().replace(" ", "")
            # 价格
            info['price'] = node.xpath('./div[2]/div[1]/div/p[1]/strong/text()')[0].strip()
            # 出租方式
            info['rent_way'] = node.xpath('./div[2]/div[1]/div/p[2]/text()')[0].strip()
            # 详细信息的url
            info['next_url'] = 'https://hz.5i5j.com' + node.xpath('.//h3/a/@href')[0].strip()

            self.item.append(info)

    def save(self):
        print(self.item)

    def change_area_name(self, area_name):
        if area_name in ['半山田园', '大关', '拱宸桥', '德胜', '湖墅', '三墩', '申花', '万达广场', '和睦', '康桥', '桥西', '塘河']:
            return '拱墅'
        elif area_name in ['宝善', '长庆', '朝晖', '打铁关', '东新', '和平广场', '环北市场', '三塘', '石桥', '天水', '武林', '潮鸣', '德胜', '湖墅',
                           '众安桥']:
            return '下城'
        elif area_name in ['复兴', '鼓楼', '湖滨', '近江', '南星', '清泰', '潮鸣', '众安桥', '四季青', '望江', '吴山', '雄镇楼']:
            return '上城'
        elif area_name in ['奥体', '白马湖', '滨江区政府', '彩虹城', '长河', '浦沿', '西兴']:
            return '滨江'
        elif area_name in ['崇贤', '勾庄', '径山', '老余杭', '良渚', '临平', '瓶窑', '乔司', '仁和', '塘栖', '未来科技城', '良渚文化村', '五常', '闲林',
                           '星桥', '留下', '三墩', '万达广场', '小和山', '中泰']:
            return '余杭'
        elif area_name in ['北干', '城厢', '临浦', '南部卧城', '钱江世纪城', '闻堰', '湘湖', '萧山经济开发区', '萧山市郊', '义桥']:
            return '萧山'
        elif area_name in ['翠苑', '古荡', '黄龙', '九莲', '省府', '文二西路', '文教', '文三西路', '文一西路', '留下', '三墩', '申花', '小和山', '西溪',
                           '学军', '之江', '转塘']:
            return '西湖'
        elif area_name in ['采荷', '丁桥', '艮北新城', '火车东站', '四季青', '笕桥', '景芳', '九堡', '南肖埠', '钱江新城', '三里亭', '闸弄口']:
            return '江干'
        elif area_name in ['富阳', '银湖']:
            return '富阳'
        elif area_name in ['奥特莱斯', '海宁', '许村', '星星港湾']:
            return '海宁'
        elif area_name in ['大江东', '大学城北', '江滨', '金沙湖', '文泽', '沿江']:
            return '钱塘新区'
        else:
            return '其他'

    def main(self):
        for page in range(1, 5):
            self.sent_request(page)
        self.save()


if __name__ == '__main__':
    zufang = Zufang()
    zufang.main()
