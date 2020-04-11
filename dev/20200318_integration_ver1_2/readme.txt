20200318 15:10 By ZHONG Hui:

How to test the system:
1. download the whole file to your computer.
2. click app2.py to run the project.
3. Search movie to get recommendation result, you should type the exactly right movie name.
eg. 'The Avengers'

Done:
1. Simplifiy the way of project runs by removing the unzip and input operations.
2. Re-adjust the movie cover size.

Pending:
1. Add data exploration/visualization part to this program.
2. Add function: If click the name of movies, then turn on the homepage of movie.
(Q:many homepages in the dataset are invalid.)

20200314 12:00 By HUANG Yu:

Instructions:
1. Run "app.py"
2. Follow the printed instruction to input the file path

Functions:
1. The website will show 100 random recommendations first
2. Search the movie name to get some similar recommendations

Done:
1. Canceled the steps to unzip and change path in code manually
2. 3703/4803 movies in the dataset have covers now

Pending:
1. Try to solve the problem of getting cover pictures of the rest movies
2. Add function: If click the name of movies, then turn on the homepage of movie




20200314 09:00 By HUANG Yu:

Instructions:
1. Unzip "picture.zip" in "/static/img"
2. Change the 3 paths in "contentBased2.py" according to the situation
3. Run "app2.py"

Notes:
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
