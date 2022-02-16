# SQL


##  [BigQuery](https://cloud.google.com/bigquery/docs)
구글에서 제공하는 클라우드 제품 중 하나임 BigQuery는 문서도 교육 자료도 많고, 사용 사례 외의 활용에 대해서도 확장 가능성이 높다고 생각됩니다.
하지만 서버나 클라우드에서 데이터를 호출해서 쿼리를 사용하는 게 익숙하지 않다면, 우선 Kaggle Courses를 이용해 공부하는 방법도 있습니다.
Kaggle Course를 통해 공부하니까 Python으로 BigQuery를 사용하는 방법을 실습할 수 있었습니다.

### [Intro to SQL](https://www.kaggle.com/learn/intro-to-sql)
해당 과정은 6개의 과정으로 수료까지 걸리는 시간은 대략 3시간이라 적혀있지만, 응용이나 답을 구하기 위해 구글 문서도 참고하다보니 저의 경우는 9시간 정도 소요되었습니다.
물론 풀이 중 hint나 solution을 제공해주기 때문에, 지름길이 편한 분들은 그냥 답보고 찾는 게 나을 수도 있습니다.

**Lessons**
* Getting Started With SQL and BigQuery
* Select, From & Where
* Group By, Having & Count
* Order By
* As & With
* Joining Data

```python
# bigquery_sql.py

## Case 1: request a dataset(not recommended)
pbq = PubBigQuery("chicago_crime")

### Customized Lesson 1
pbq.check_schema("0.crime")
pbq.check_schema("0.crime", "timestamp")
pbq.check_schema("0.crime", "BOOLEAN")
```

| 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
|![init and checks](https://github.com/AshbeeKim/cs-archive/blob/master/bigquery_py_1.png)|  |  |  |  |  |

<!--
| 4 | 5 | 6 |
|---|---|---|
|  |  |  |
-->

### [Advanced SQL](https://www.kaggle.com/learn/advanced-sql)
4개의 과정임에도 4시간의 소요될 것이라 적혀있어서, 넉넉히 8시간 정도 걸릴 것으로 예상됩니다.

**Lessons**
* JOINs and UNIONs
* Analytic Functions
* Nested and Repeated Data
* Writing Efficient Queries

Intro to SQL을 공부하면서 각각의 문법은 쉬웠으나, 응용이 어렵게 느껴졌습니다. 상세 내용 내일 업로드 하겠습니다.
Sololearn을 통해 공부하 SQL은 Kaggle로 공부한 SQL을 정리한 뒤, 중복되지 않는 범위를 천천히 공유하도록 하겠습니다.
