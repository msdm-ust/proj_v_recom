20200314 09:00 By HUANG Yu:

Instructions:
1. Unzip "picture.zip" in "/static/img"
2. Change the 3 paths in "contentBased2.py" according to the situation
3. Run "app2.py"

Done:
1. Downloaded the cover of some movies to read conveniently from local 
2. Some changes:
- "index2.html": changed img "movie.url" to static
- "contentBased2.py": changed the stable url to local path of cover of each movie
- "app2.py": dependent on "index2.html" and "contentBased2.py"

Pending:
1. Continue to download the cover of the rest movies (since the crawler often be forbidden... need to more tries)
- "success.txt" saved the id of movie that has cover
2. Add function: If click the name of movies, then turn on the homepage of movie

2020年3月11日 21:53 By ZHONG Hui:
已完成：
1. CSS 固定了movie item的div。
2. app.py POST:在输入框input中输入电影名，页面更新推荐结果，暂定K=9，
去除分页nav

待完成：
1. index.html : movie item 中没有加label
2. app.py: POST方法中movieName没有做验证，必须要与
df中的movie name完全一致才能出搜索结果。
3. url写死的，要替换。