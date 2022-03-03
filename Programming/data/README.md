<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f8ba0a,100:0174b7&height=250&section=header&text=Data&fontSize=80&fontAlign=14&fontAlignY=30&desc=Programing%20Language%20%3A%20%20SQL,%20Python,%20and%20R&descSize=20&descAlign=72&descAlignY=56&&fontColor=fff" />

# Languages
* [SQL](#sql)
* [Python](#python)
* [R](#r)

---
> ## SQL
### Contexts
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
  
  PostgreSQL로 작성하는 것에 익숙하다면, 캐글 Intro to SQL에서는 크게 어려운 부분이 없을 수 있다. (그리고 아직 한참 멀었지만... 사용되는 함수만 다를 뿐 큰 틀은 달라지지 않아서, 용법만 알면 SQL에서 각 언어별 필요한 함수를 보다 빨리 찾을 수 있다는 것을 체감하고 있는 요즘이다. MySQL으로만 공부 중인 나에게도 Intro to SQL은 비교적 쉬웠으니까.) 익숙하지 않았던 Query의 활용에 있어서, 해당 과정에서 예상보다 오래 걸렸던 부분이 WITH AS(temporary 테이블 생성)를 활용한 query 였다.

  SQL에서 서브쿼리(query내 query)를 사용할 때 새로운 테이블이 생성되는데, 이러한 서브 쿼리를 지속해서 사용한다면 메모리 차원에서 문제가 발생할 수 있다. WITH절은 이러한 문제를 해결할 수 있는데, 일시적으로 테이블을 생성할 수 있기 때문이다. 단, WITH 절을 남용했을 때 가용 정도를 넘어가면 느려진다고 한다. 반면, 생성한 WITH 절의 구문을 여러 번 참조하는 쿼리를 작성하는 것은 WITH 절 활용의 좋은 예가 될 수 있다.

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
 4개의 과정이 4시간의 소요될 것이라 적혀, 넉넉히 8시간 정도 걸릴 것으로 예상했었다. 

**Lessons**
- [x] JOINs and UNIONs
- [x] Analytic Functions
- [x] Nested and Repeated Data
- [x] Writing Efficient Queries

TIME_DIFF [^time-fuction] 에서도 LAG를 활용한 문제는...휴...역시 활용을 잘 하려면 아는 게 많아야 한다.(~~나는 바보다.~~) 잘만 활용하면, time-series 분석을 위한 처리(sliding window와 같은)에도 도움이 될 것 같아서 메모를 남긴다.
```postgresql
# LAG - 값 기준 이전 로우 값 반환(<-> LEAD)
LAG([conditions], [order number], [default value]) OVER ([PARTITION BY], [ORDER BY])
```

SchemaFiled의 타입이 'RECORD'인 경우, dictionary 형태로 입력되어 조회 시 유의미한 결과를 출력하려면 특정 값의 키가 무엇인지 파악해야 한다. `table_name.schema[number]`로 입력하면 특정 Schema 만 조회가 가능하다.
```postgresql
sample_commits_table.schema[7]
-- SchemaField('trailer', 'RECORD', 'REPEATED', None, (SchemaField('key', 'STRING', 'NULLABLE', None, (), None), SchemaField('value', 'STRING', 'NULLABLE', None, (), None), SchemaField('email', 'STRING', 'NULLABLE', None, (), None)), None)
```

`UNNEST()`를 활용하는 문제에서 `query=~`으로 주어진 첨부된 이미지를 믿지 말라는 얘기를 꼭 하고 싶다. 그 위의 테이블 조회를 참고하면, 바로 수정해야 할 부분이 보이지만 그래도 보여지는 이미지를 참고해서 뜬 오류 메시지를 확인하면 기분이 유쾌하지 않기 때문이다.

여태까지 Kaggle 이나, Dacon 등에서 제공받은 데이터 외의 데이터를 활용할 때에 데이터 수집에 어려움을 겪었던 이유를 찾았다. 우선 raw 데이터를 찾는 것부터 쉽지 않고, 수집하면서도 정확한 정의가 되지 않았기 때문이다. 왜 필요한지, 왜 필요하지 않은지. 어떠한 데이터를 특정한 분석 목적을 가지고 활용을 하기 위해서는 수집 시 적어도 큰 범주에서의 정의(table, schema)는 이루어져야 하고, 데이터의 양이 방대하다면 사용하는 쿼리는 서브 쿼리 혹은 임시 테이블 생성 등 중/고급의 쿼리를 작성할 줄 알아야 한다는 것이다. (물론 RDBMS를 막 실습하는 입장에서, 이미지나 음성 데이터 분석에 필요하다는 이유로 NoSQL을 활용하기란 어렵다.)

Google BigQuery 가이드나 샘플을 병행해서 읽으며, '`bigquery_sql.py`를 왜 작성했나.'하는 생각이 들었다. 쿼리 스크립트나, BigQuery API로 쿼리 코드 샘플을 읽으며, 이미 되어 있는 내용을 필요할 때마다 간단한 함수로만 작성해서 사용하는 게 낫겠다고 생각했다. 그럼에도 계속해서 해당 파일을 계속해서 보수해야겠다고 판단한 이유는 당장 급하게 확인하고, 편하게 사용할 수 있는 방법(본인 기준)이기 때문이다.


> #### MySQL/Oracle

  MySQL 혹은 Oracle을 공부하거나 실습할 수 있는 플랫폼으로는 Programmers, Elice Coding, Sololearn 등이 있다. 이 중, 앱으론 Sololearn, 웹으론 Programmers 를 주로 사용했었다.

```Python
# Python
import pymysql  # to connect MySQL
import cx_Oracle    # to connect Oracle
```

  Python에 SQL을 활용하기 위해서는 위와 같은 라이브러리를 import 해야 한다. 

---
> ## Python
![Alt text](https://img.shields.io/badge/Python-v3.7%20%7C%20v3.9-blue.svg?&style=flat&logo=Python&logoColor=white&labelColor=abcdef&cacheSeconds=3600$logoWidth=60)

### Steps
* [ETL](#etl)
* [EDA](#eda)
* [FE](#fe)

> #### ETL
- [x] json/xml
- [ ] csv
- [x] urllib/requests
- [x] [BeautifulSoup]/[Selenium]
- [ ] [Playwright]

> #### EDA
- [ ] [Internationalization](https://docs.python.org/3.9/library/i18n.html)
- [ ] [Python Language Service](https://docs.python.org/ko/3.9/library/language.html)
- [ ] [Numpy]
- [ ] [Pandas]
- [ ] [scikit-learn]
- [ ] [OpenCV]

> #### FE
- [ ] [scikit-learn]
<!--
- [ ] [TensorFlow]
- [ ] [PyTorch]
- [ ] [Gensim]
-->

---
> ## R


```python
# R을 python에서 사용할 때
## ipynb
from rpy2.robjects import r
%load_ext rpy2.ipython

%%R
install.packages("data.table")
install.packages("plyr")    #adply, ddply, m*ply, etc.
install.packages("dplyr")
install.packages("sqldf")
install.packages("reshape")
```

---
[^sql-a]: Because of throughput or latency, I supposed the ideal number of datasets is not more than 3.
[^sql_b]: [SQL 언어 전환](https://cloud.google.com/bigquery/docs/reference/standard-sql/enabling-standard-sql?hl=ko#python "Google BigQuery Documents - SQL 언어 전환")
[^sql_c]: [BigQuery 공개 데이터 세트](https://cloud.google.com/bigquery/public-data?hl=ko "Google BigQuery Documents - BigQuery 공개 데이터 세트")
[^time-function]: [Time funtions](https://cloud.google.com/bigquery/docs/reference/standard-sql/time_functions "Google BigQuery Documents - Time funtiions")


<img src="https://capsule-render.vercel.app/api?type=waving&color=0:f8ba0a,100:0174b7&height=200&section=footer&text=Thank%20You&fontSize=50&fontAlignY=70&fontColor=fff"/>
