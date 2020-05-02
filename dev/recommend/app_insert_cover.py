from flask import Flask,request,render_template,url_for,session,json,jsonify
from page_utils import Pagination
#from crawler_douban import Cover
import pandas as pd
app = Flask(__name__)
#df3 = Cover.get_cover_data()
df3 = pd.read_csv('cover_url_data.csv')

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
        # movie1 = {'id':'001','name':df3.original_title[1],'rating':4.6,'tag':'惊悚','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie2 = {'id':'002','name':'Movie2','rating':4.5,'tag':'喜剧','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie3 = {'id': '003', 'name': 'Movie3', 'rating': 3.8,'tag':'剧情','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie4 = {'id': '004', 'name': 'Movie4', 'rating': 2.9,'tag':'灾难','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie5 = {'id': '005', 'name': 'Movie5', 'rating': 3.8,'tag':'科幻','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie6 = {'id': '006', 'name': 'Movie6', 'rating': 2.8,'tag':'悬疑','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie7 = {'id': '007', 'name': 'Movie7', 'rating': 4.6,'tag':'喜剧','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # movie8 = {'id': '008', 'name': 'Movie8', 'rating': 4.4,'tag':'动作','url':'https://ss0.bdstatic.com/94oJfD_bAAcT8t7mm9GUKT-xh_/timg?image&quality=100&size=b4000_4000&sec=1583478382&di=784188562baefbb8cf353a75e22481bb&src=http://image14.m1905.cn/uploadfile/2016/0704/20160704045741804962.jpg'}
        # data = [movie1,movie2,movie3,movie4,movie5,movie6,movie7,movie8]
        data = []
        for i in range(8,16):
            movie = {'id':df3.id[i],'name':df3.original_title[i],'rating':df3.vote_average[i],
            'tag':eval(df3.genres[i])[0]['name'],'url':df3.cover[i]}
            data.append(movie)

        pager_obj = Pagination(request.args.get("page", 1), len(data), request.path, request.args, per_page_count=6)
        index_list = data[pager_obj.start:pager_obj.end]
        html = pager_obj.page_html()
        return render_template('index.html',index_list=index_list, html=html)
    else:
        data = request.get_data()  # 得到JSON字符串
        data = json.loads(data)  # 解析为JSON对象
        movieName = data['movieName']
        print("movieName:",movieName)
        return jsonify(movieName)

if __name__ == '__main__':
    # app.run(DEBUG=True)
    app.run()
