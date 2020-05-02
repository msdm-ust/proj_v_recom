from flask import Flask,request,render_template,url_for,session,json,jsonify
from page_utils import Pagination
from datetime import datetime
from contentBased4 import get_recommendations,get_random_movies,search_nearest_movies,changeStr,get_index_movies
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        # 随机获得100部电影
        #data = get_random_movies(K = 18)
        data = get_index_movies(K = 18)
        pager_obj = Pagination(request.args.get("page", 1), len(data), request.path, request.args, per_page_count=9)
        index_list = data[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('index2.html',index_list=index_list, html=html)

    else:
        data = request.get_data()  # 得到JSON字符串
        data = json.loads(data)  # 解析为JSON对象
        movieName = data['movieName']
        movieName = changeStr(movieName.strip())  # 去除前后的空格

        if movieName is None or movieName == '':  # 没输入电影名
            print("random recommendation")
            res = get_random_movies(K = 9)   # 随机推荐
        else:
            print(movieName)  # 用户input
            nearMovie = search_nearest_movies(movieName)  # 最接近的电影名
            if nearMovie == '':
                return jsonify({'state':-1,'data':'无推荐结果，请重新输入！'})
            else:
                res = get_recommendations(nearMovie,K = 9)

                record = {'time': datetime.now(),'input':movieName,'nearMovie':nearMovie,'recommend':res}
                # {input:girl, nearMovie: Pink Pig, recommend: res, time: time}
                #print(record)
                filename = 'data/record.json'
                with open(filename, 'a') as file_object:
                    file_object.write(str(record)+'\n')

        return jsonify({'state':0,'data':res})


if __name__ == '__main__':
    app.run()

