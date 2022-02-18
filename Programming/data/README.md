<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f8ba0a,100:0174b7&height=250&section=header&text=Data&fontSize=80&fontAlign=14&fontAlignY=30&desc=Programing%20Language%20%3A%20%20SQL,%20Python,%20and%20R&descSize=20&descAlign=72&descAlignY=56&&fontColor=fff" />

# Languages
* [SQL](#sql)
* [Python](#python)
* [R](#r)

---
> ## SQL
### Contents
* [BigQuery](#bigquery)
* [MySQL](#mysql)

> #### [BigQuery](https://cloud.google.com/bigquery/docs "Google BigQuery Documents")
구글에서 제공하는 클라우드 제품 중 하나임 BigQuery는 문서도 교육 자료도 많고, 사용 사례 외의 활용에 대해서도 확장 가능성이 높다고 생각됩니다.
하지만 서버나 클라우드에서 데이터를 호출해서 쿼리를 사용하는 게 익숙하지 않다면, 우선 Kaggle Courses를 이용해 공부하는 방법도 있습니다.
Kaggle Course를 통해 공부하니까 Python으로 BigQuery를 사용하는 방법을 실습할 수 있었습니다.

##### [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql "Kaggle SQL Course - Intro to SQL")
해당 과정은 6개의 과정으로 수료까지 걸리는 시간은 대략 3시간이라 적혀있지만, 응용이나 답을 구하기 위해 구글 문서도 참고하다보니 저의 경우는 9시간 정도 소요되었습니다.
물론 풀이 중 hint나 solution을 제공해주기 때문에, 지름길이 편한 분들은 그냥 답보고 찾는 게 나을 수도 있습니다.

**Lessons**
- [x] Getting Started With SQL and BigQuery
- [x] Select, From & Where
- [x] Group By, Having & Count
- [x] Order By
- [x] As & With
- [x] Joining Data

**Customized Lesson 1**
```python
# bigquery_sql.py

## Case 1: request a dataset(not recommended)
pbq = PubBigQuery("chicago_crime")

pbq.check_schema("0.crime")
pbq.check_schema("0.crime", "timestamp")
pbq.check_schema("0.crime", "BOOLEAN")
```

**Customized Lesson 2 & 3** [^sql-a]
```python
# bigquery_sql.py

qr_1 = QueryResult("openaq")

qr_1.check_schema('1.global_air_quality', 'string')
qr_1.request_query_result("""
SELECT country
FROM `bigquery-public-data.openaq.global_air_quality`
WHERE unit = 'ppm'
""")

## Case 2: request several datasets(len(args)<= 3)
qr_2 = QueryResult("openaq", "hacker_news", option=True)

qr_2.check_table()
qr_2.check_schema('2.full', "INTEGER")
qr_2.show_table('2.comments')

print(qr_2.request_query_result("""
SELECT parent, COUNT(1) AS NumPosts
FROM `bigquery-public-data.hacker_news.comments`
GROUP BY parent
HAVING COUNT(1) > 10
""").head())
```

| 1                                                                                                               | 2                                                                                                              | 3                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|
| ![Alt text](https://github.com/AshbeeKim/cs-archive/blob/master/src/images/bigquery_py_1.png "init and checks") | ![Alt text](https://github.com/AshbeeKim/cs-archive/blob/master/src/images/bigquery_py_2.png "check and edit") | ![Alt text](https://github.com/AshbeeKim/cs-archive/blob/master/src/images/bigquery_py_3.png "print out to markdown") |

| 4 | 5 | 6 |
|---|---|---|
|  |  |  |

##### [Advanced SQL](https://www.kaggle.com/learn/advanced-sql "Kaggle SQL Course - Advanced SQL")
4개의 과정임에도 4시간의 소요될 것이라 적혀있어서, 넉넉히 8시간 정도 걸릴 것으로 예상됩니다.

**Lessons**
- [x] JOINs and UNIONs
- [ ] Analytic Functions
- [ ] Nested and Repeated Data
- [ ] Writing Efficient Queries

> #### MySQL
Sololearn을 통해 공부했던 SQL은 Kaggle로 공부한 SQL을 정리한 뒤, 중복되지 않는 범위를 천천히 공유하도록 하겠습니다.
프로그래머스로 MySQL이나 Oracle을 연습하는 방법도 있다는 것을 알려드립니다.


---
> ## Python
![Alt text](https://img.shields.io/badge/Python-v3.7%20%7C%20v3.9-blue.svg?&style=flat&logo=Python&logoColor=white&labelColor=abcdef&cacheSeconds=3600$logoWidth=60)

### Steps
* [Basic](#basic)
* [EDA](#eda)
* [FE](#fe)

> #### Basic
- [x] [logger](https://github.com/AshbeeKim/cs-archive/wiki/Python-logger)

> #### EDA
- [ ] re

> #### FE

---
> ## R


---
[^sql-a]: Because of throughput or latency, I supposed the ideal number of datasets is not more than 3.


<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f8ba0a,100:0174b7&height=200&section=footer&text=Thank%20You&fontSize=50&fontAlignY=70&fontColor=fff"/>
