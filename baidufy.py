import requests
import random
import hashlib
# hashlib是MD5的哈希算法


# 定义一个翻译的主函数，该函数接收main中的参数，并作为后续的字符串对象，该对象名称不要与main中定义的对象名称一样，重复名称不是好选择
def trans(q, from_lang, to_lang):
    url = "http://api.fanyi.baidu.com/api/trans/vip/translate"
    appid = "你的APPID"
    appkey = "你的APPKEY"
    salt = random.randint(5, 200)
    # 根据规定的顺序组合得到字符串,顺序一定要正确
    sign_str = appid+q+str(salt)+appkey
    # 调用hash方法对字符串进行hash
    sign = hashlib.md5(sign_str.encode()).hexdigest()

    # 对需要翻译的文本进行encode处理
    q = q.encode(encoding="utf-8", errors="编码错误")

    # 使用params参数组合URL中需要传递的参数
    params = {"q": q, "from": from_lang, "to": to_lang, "appid": appid, "salt": salt, "sign": sign}
    r = requests.get(url=url, params=params)
    result = r.json()  # r对象调用json方法赋值给result，result是一个字典对象

    # print("翻译语言是%s(英语)，翻译结果是%s(简体中文)" % (result['from'],result['to']))
    print("翻译语言: %s(自动识别)" % result['from'])
    print("翻译语言: %s(简体中文)" % result['to'])
    # 从字典对象中根据键名取值，根据示例看该值是一个列表，且在第一位，取完之后又是一个字典，继续根据键名取值就得到了想要的内容
    print("翻译原文: " + result["trans_result"][0]["src"])
    print("翻译结果: " + result["trans_result"][0]["dst"])


if __name__ == '__main__':
    # query = input(str("请输入想要翻译的句子："))
    query = "I can't do it anymore, because I love this too much"
    f_lang = "auto"
    t_lang = "zh"
    # 调用trans()函数传递以上参数进去
    trans(query, f_lang, t_lang)
    print("-----"*10)
    print("程序运行完成，感谢使用")