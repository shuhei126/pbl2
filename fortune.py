from flask import Flask, render_template, request
import os
import http.client
import json
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
    title="姓名判断 雅の部屋~無料姓名判断~", \
    message="あなたのお名前は？(漢字入力)", \
    message0="(左)姓　　　　　　　　名(右)", \
    message20 = "この運勢はあくまで目安です。皆さん強く生きましょう", \
    message21 = "　　　　　　")


@app.route('/', methods=['POST'])
def form():
    field = request.form['field']
    print(len(field))
    for moji in field:
        print(moji)
        print(kanji(moji))

    stroke_list = []
    for moji in field:
        stroke_list.append(kanji(moji))
    
    print(stroke_list)


    field2 = request.form['field2']
    print(len(field2))
    for moji in field2:
        print(moji)
        print(kanji(moji))


    stroke_list2 = []
    for moji in field2:
        stroke_list2.append(kanji(moji))
    
    print(stroke_list2)

    message_l = []

    jinkaku = stroke_list[-1] + stroke_list2[0]
    #message_l.append("あなたの人格は「%d画」です。" % jinkaku)
    if stroke_list[-1] + stroke_list2[0] in [11,15,16,17,18,21,29,31,37,41]:
        message_l.append("あなたの人格は「%d画」です。" % jinkaku)
        message_l.append("30～50代前後の運勢を表します。あなたはとても親思いだったり、優しくて責任感の強い性格でしょう。")
    else:
        if stroke_list[-1] + stroke_list2[0] == 4:
            message_l.append("G")
            message_l.append(" ")
        else:
            message_l.append("あなたの人格は「%d画」です。" % jinkaku)
            message_l.append("30～50代前後の運勢を表します。可もなく不可もなく，といったところでしょう。")


    chikaku = sum(stroke_list2)
    #message_l.append("あなたの地格は「%d画」です。" % chikaku)
    if sum(stroke_list2) in [7,8,17,18,37,47,48]:
        message_l.append("あなたの地格は「%d画」です。" % chikaku)
        message_l.append("0～30歳までの運勢や生涯の健康を表す部分です。7と8の数字を持つあなたは、病気とほとんど無縁で大病の心配はないでしょう。")
    else:
        if sum(stroke_list2) == 4:
            message_l.append("O")
            message_l.append(" ")
        else:
            message_l.append("あなたの地格は「%d画」です。" % chikaku)
            message_l.append("0～30歳までの運勢や生涯の健康を表す部分です。可もなく不可もなく，といったところでしょう。")
    

    gaikaku = stroke_list[0] + stroke_list2[-1]
    #message_l.append("あなたの外格は「%d画」です。" % gaikaku)
    if stroke_list[0] + stroke_list2[-1] in [13,15,16,17,23,24,29,32]:
        message_l.append("あなたの外格は「%d画」です。" % gaikaku)
        message_l.append("対人関係による運勢や自分以外の人からくる運勢を表します。これに恵まれているあなたは、多少の壁にぶつかっても、へこたれないパワーをもつ人と言えるでしょう。")
    else:
        if stroke_list[0] + stroke_list2[-1] == 4:
            message_l.append("D")
            message_l.append(" ")
        else:
            message_l.append("あなたの外格は「%d画」です。" % gaikaku)
            message_l.append("対人関係による運勢や自分以外の人からくる運勢を表します。可もなく不可もなく，といったところでしょう。")
    

    soukaku = sum(stroke_list) + sum(stroke_list2)
    #message_l.append("あなたの総格は「%d画」です。" % soukaku)
    if sum(stroke_list) + sum(stroke_list2) in [15,16,24,31,32,41,45,17,48,61]:
        message_l.append("あなたの総格は「%d画」です。" % soukaku)
        message_l.append("晩年50歳から死ぬまでの運勢と自分の全体を表す大事な部分です。家庭や仕事など、人生を総合的に見た場合のあなたの運勢は最高です！！！")
    else:
        if sum(stroke_list) + sum(stroke_list2) == 4:
            message_l.append("!")
            message_l.append(" ")
        else:
            message_l.append("あなたの総格は「%d画」です。" % soukaku)
            message_l.append("晩年50歳から死ぬまでの運勢と自分の全体を表す大事な部分です。家庭や仕事など、人生を総合的に見た場合のあなたの運勢は，可もなく不可もなく，といったところでしょう。")
    

    return render_template('index.html', \
    title="姓名判断 雅の部屋~無料姓名判断~", \
    message1 = message_l[0] + message_l[1], \
    message2 = message_l[2] + message_l[3], \
    message3 = message_l[4] + message_l[5], \
    message4 = message_l[6] + message_l[7], \
    message10 = "一般的に凶数とされる数[2 、4、 9、 10、 12、 14、 19、 20、 22、 26、 27、 28、 34、 36、 43、 44、 46、 49、 50、 51、 54、 56 、59、 60、 62、 64、 66、 69、 70、 72、 74、 76、 79、 80]（※9は人格数に限り吉になる）", \
    message15 = "一般的に吉数とされる数[1、3、5、6、7、8、11、13、15、16、17、18、21、23、24、25、29、31、32、33、35、37、38、39、41、45、47、48、52、57、58、61、63、65、67、68、81]", \
    message16 = "姓名には強弱の調和が重要であり,強い数ばかりを選ぶと、逆に凶意を強めることになってしまう場合もあるので注意!!!")



def kanji(moji):
    s = moji
    s_quote = urllib.parse.quote(s)

    conn = http.client.HTTPSConnection("kanjialive-api.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "kanjialive-api.p.rapidapi.com",
        'x-rapidapi-key': "ed0bdc7bb2msh79057c8dcceed61p120748jsn470c6115c7cc"
        }

    conn.request("GET", "/api/public/kanji/" + s_quote , headers=headers)

    res = conn.getresponse()
    data = res.read()

    data = json.loads(data.decode("utf-8"))

    if "error" in data:
        if moji == '佐':
            return 7
        if moji == '鈴':
            return 13
        if moji == '嵐':
            return 12
        if moji == '颯':
            return 14
        if moji == '刈':
            return 4
        if moji == '斗':
            return 4
        if moji == '秀':
            return 7
        if moji == '藤':
            return 18
        if moji == '晟':
            return 10
        if moji == '井':
            return 4
        if moji == '杜':
            return 7
        if moji == '隼':
            return 10
        if moji == '彩':
            return 11
        if moji == '帆':
            return 6
        if moji == '翔':
            return 12
        if moji == '彌':
            return 0
        if moji == '冨':
            return 0
        if moji == '熊':
            return 14
        if moji == '笠':
            return 11
        if moji == '傑':
            return 13
        if moji == '欣':
            return 8
        if moji == '也':
            return 3
        if moji == '伊':
            return 6
        if moji == '邊':
            return 19
        if moji == '斎':
            return 17
        return 0
    else:
        return data['kanji']['strokes']['count']


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=os.environ['PORT'])
    #app.run(host='0.0.0.0', port=5000)