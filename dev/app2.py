from flask import Flask,request,render_template,url_for,session,json,jsonify
from page_utils import Pagination
from contentBased2 import get_recommendations,get_random_movies
app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        # 随机获得100部电影
        data = get_random_movies(100)
        pager_obj = Pagination(request.args.get("page", 1), len(data), request.path, request.args, per_page_count=6)
        index_list = data[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('index2.html',index_list=index_list, html=html)

    else:
        data = request.get_data()  # 得到JSON字符串
        data = json.loads(data)  # 解析为JSON对象
        movieName = data['movieName']
        #movieName = 'The Avengers'
        res = get_recommendations(movieName,K = 9)
        print(res)
        return jsonify(res)


if __name__ == '__main__':
    #app.run(DEBUG=True)
    app.run()

