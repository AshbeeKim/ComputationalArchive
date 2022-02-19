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
  구글에서 제공하는 클라우드 제품 중 하나인 BigQuery는 문서도 교육 자료도 많고, 사용 사례 외의 활용에 대해서도 확장 가능성이 높다고 생각된다. 하지만 서버나 클라우드에서 데이터를 호출해서 쿼리를 사용하는 게 익숙하지 않다면, 우선 Kaggle Courses를 이용해 공부하는 방법도 있다. Kaggle Course를 통해 공부하니까, Python으로 BigQuery를 사용하는 방법을 실습할 수 있었다.

##### [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql "Kaggle SQL Course - Intro to SQL")
  해당 과정은 총 6개의 과정으로 수료까지 걸리는 시간은 대략 3시간이라 적혀있지만, 응용이나 답을 구하기 위해 구글 문서도 참고하니까 나의 경우는 9시간 정도 소요되었다. 물론 풀이 중 hint나 solution을 제공해주기 때문에, 지름길이 편한 분들은 그냥 답보고 찾는 게 나을 수도 있다.

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

  BigQuery의 기본 설정 언어 [^sql_b]에 대해 확인한 바로는 표준 SQL과 legacy SQL이라는 두 가지 SQL 언어를 지원한다. Kaggle에서부터 표준 SQL로 사용했기에, bq 명령줄 도구나 REST API에서도 표준 SQL을 사용하고자 한다면 `.bigqueryrc`를 편집하는 방법이 있다.
```bash
[query]
--use_legacy_sql=false

# view 만들 때 사용되는 mk
[mk]
--use_legacy_sql=false
```
legacy SQL이 익숙하다면, Python 클라이언트 라이브러리의 경우 default가 표준 SQL로 되었기에 `bigquery.QueryJobConfig(use_legacy_sql=True)`와 같이 extra configuration을 설정하는 방법을 추천한다. 

##### [Advanced SQL](https://www.kaggle.com/learn/advanced-sql "Kaggle SQL Course - Advanced SQL")
 4개의 과정이 4시간의 소요될 것이라 적혀, 넉넉히 8시간 정도 걸릴 것으로 예상했었다. `bigquery_sql.py`를 수정하던 중, 공개 데이터 세트 [^sql_c] 도 추가적으로 확인해서 예상보다 시간을 더 잡아야 할 것 같다.

**Lessons**
- [x] JOINs and UNIONs
- [ ] Analytic Functions
- [ ] Nested and Repeated Data
- [ ] Writing Efficient Queries


  Google BigQuery 가이드나 샘플을 병행해서 읽으며, "`bigquery_sql.py`를 왜 작성했나." 에 대한 생각이 들었다. 쿼리 스크립트나, BigQuery API로 쿼리 코드 샘플을 읽으며, 이미 되어 있는 내용을 필요할 때마다 간단한 함수로만 작성해서 사용하는 게 낫겠다고 생각했다. 그럼에도 계속해서 해당 파일을 계속해서 보수해야겠다고 판단한 이유는 당장 급하게 확인하고, 편하게 사용할 수 있는 방법(본인 기준)이기 때문이다.


> #### MySQL
Sololearn을 통해 공부했던 SQL은 Kaggle로 공부한 SQL을 정리한 뒤, 중복되지 않는 범위를 천천히 공유하겠다.
참고로 프로그래머스로 MySQL이나 Oracle을 연습하는 방법도 있다.


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
[^sql_b]: [SQL 언어 전환](https://cloud.google.com/bigquery/docs/reference/standard-sql/enabling-standard-sql?hl=ko#python "Google BigQuery Documents - SQL 언어 전환")
[^sql_c]: [BigQuery 공개 데이터 세트](https://cloud.google.com/bigquery/public-data?hl=ko "Google BigQuery Documents - BigQuery 공개 데이터 세트")

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f8ba0a,100:0174b7&height=200&section=footer&text=Thank%20You&fontSize=50&fontAlignY=70&fontColor=fff"/>
