from flask import Flask, render_template, request
import os
import http.client
import json
import urllib.parse

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', \
    title="姓名判断bot", \
    message="あなたのお名前は？")


@app.route('/', methods=['POST'])
def form():
    field = request.form['field']
    print(len(field))
    if len(field) > 5:
        luck = '大吉'
    else: luck = '凶'
    return render_template('index.html', \
    title="姓名判断bot", \
    message="あなたの運勢は「%s」です！" % luck)


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


    jinkaku = stroke_list[-1] + stroke_list2[0]
    print("あなたの人格は「%d画」です。" % jinkaku)
    if stroke_list[-1] + stroke_list2[0] in [11,15,16,17,18,21,29,31,37,41]:
        print("30～50代前後の運勢を表します。あなたはとても親思いだったり、優しくて責任感の強い性格でしょう。")
    else:
        print("30～50代前後の運勢を表します。可もなく不可もなく，といったところでしょう")


    chikaku = sum(stroke_list2)
    print("あなたの地格は「%d画」です。" % chikaku)
    if sum(stroke_list2) in [7,8,17,18,37,47,48]:
        print("0～30歳までの運勢や生涯の健康を表す部分です。7と8の数字を持つあなたは、病気とほとんど無縁で大病の心配はないでしょう")
    else:
        print("0～30歳までの運勢や生涯の健康を表す部分です。可もなく不可もなく，といったところでしょう")


    gaikaku = stroke_list[0] + stroke_list2[-1]
    print("あなたの外格は「%d画」です。" % gaikaku)
    if stroke_list[0] + stroke_list2[-1] in [13,15,16,17,23,24,29,32]:
        print("対人関係による運勢や自分以外の人からくる運勢を表します。これに恵まれているあなたは、多少の壁にぶつかっても、へこたれないパワーをもつ人と言えるでしょう。")
    else:
        print("対人関係による運勢や自分以外の人からくる運勢を表します。可もなく不可もなく，といったところでしょう")


    soukaku = sum(stroke_list) + sum(stroke_list2)
    print("あなたの総格は「%d画」です。" % soukaku)
    if sum(stroke_list) + sum(stroke_list2) in [15,16,24,31,32,41,45,17,48,61]:
        print("晩年50歳から死ぬまでの運勢と自分の全体を表す大事な部分です。家庭や仕事など、人生を総合的に見た場合のあなたの運勢は最高です！！！。")
    else:
        print("晩年50歳から死ぬまでの運勢と自分の全体を表す大事な部分です。家庭や仕事など、人生を総合的に見た場合のあなたの運勢は，可もなく不可もなく，といったところでしょう")


    return render_template('index.html', \
    title="姓名判断bot", \
    message="あなたの人格は「%d画」です。" % jinkaku, \
    message2="あなたの地格は「%d画」です。" % chikaku, \
    message3="あなたの外格は「%d画」です。" % gaikaku, \
    message4="あなたの総格は「%d画」です。" % soukaku)



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
        return 0
    else:
        return data['kanji']['strokes']['count']


if __name__ == '__main__':
    app.debug = True
    # app.run(host='0.0.0.0', port=os.environ['PORT'])
    app.run(host='0.0.0.0', port=5000)