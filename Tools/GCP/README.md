# Google Cloud 

`Google Cloud Essentials`를 완료했는데, 숙지가 되지 않은 상태라 복습 겸 계속해서 퀘스트를 수료하기까지 반복해서 작성할 것 같은 내용 정리 목적으로 생성함.

## Contexts
* [Basic](#basic)
* [Set-ups](#set-ups)
* [Cluster](#cluster)
* [Cloud SQL](#cloud-sql)
* [Cloud Storage](#cloud-storage)
* [Awards](#awards)

> ### Basic [^gcloud-cli-overview]
```bash
gcloud auth list
gcloud config list project
# gcloud config list --all ## not recommended
gcloud compute instances create [INSTANCE NAME]
gcloud compute instances list
gcloud components list
```


> ### Set-ups [^regions-and-zones]
```bash
gcloud config get-value compute/zone
gcloud config set compute/zone [ZONE NAME]
gcloud config get-value compute/region
gcloud config set compute/region [REGION NAME]
```
제공되는 서비스 별 파라미터가 매우 많고, `compute/[]`, `storage/[]`에 따라 없는 경우도 존재하기에 에러가 뜬다 싶으면 바로 구글링해서 공식 문서 참고하는 것을 권한다.


> ### Cluster [^standard-cluster-architecture]
```bash
gcloud container clusters create [CLUSTER NAME]
gcloud container clusters get-credentials [CLUSTER NAME]
kubectl create deployment hello-server --image=[IMAGE URL]
kubectl expose deployment hello-server --type=LoadBalancer --port [PORT NO]
# kubectl get service
# gcloud container clusters delete [CLUSTER-NAME]
```
![Standard Cluster Architecture](https://cloud.google.com/kubernetes-engine/images/cluster-architecture.svg "Google Cloud-Standard Cluster Architecture")

> ### Load Balancing [^load-balancing]
![Network Load Balancing example](https://cloud.google.com/load-balancing/images/network-load-balancer.svg "Google Cloud-Network Load Balancing example")
* **TCP/UDP**
* **HTTP(s)**

네트워크 부하 분산을 하는 방법이 TCP/UDP를 활용하는 방법이나, HTTP(s)를 활용하는 방법이 있다는 것은 알겠는데, Quest가 HTTP로 되었던 만큼 TCP로 적용할 시에 추가해야 하는 내용이 무엇인가를 찾느라 오래 걸렸던 [Create and Manage Cloud Resources: Challenge Lab](https://www.cloudskillsboost.google/focuses/10258?parent=catalog). `Challenge Lab`은 마치 특정 회사의 어떠한 업무를 맡았다고 가정하고 문제가 제시되기 때문에 더 어렵게 느껴진다. 분명 궁금한 게 생겨서 간단한 과정을 수료하고 문서를 더 보면서 공부했는데도, 바로 떠올리지 못 하고, 파라미터 하나 추가해서 에러 발생하고 파라미터를 너무 기본적인 내용으로만 채웠다고 실습 과정이 튕겼던 것을 생각하면... "이게 왜 작동하는가? 이게 왜 작동하지 않는가?"로 유명한 짤이 생각나기도 했다. 


> ### Cloud SQL
```shell
# connect to the database
gcloud sql connect $SQL_INSTANCE_NAME --user=root --quiet

# see the default system databases and check [TABLE_NAME]'s tables
mysql> SHOW DATABASES;
mysql> USE $TABLE_NAME;
mysql> SHOW TABLES;

# exit the mysql prompt
mysql> exit
```

주말 내내 카페인 혈관에 꽂으며, XGBoostClassifier를 sql로 작성하는 방법에 대해 고민했으나 제공된 데이터로는 알겠는데 이를 통해 이해한 내용을 바탕으로 다른 도메인의 데이터에 적용시키려는 시도를 했다. 의료 데이터 쪽은 넘사기도 하고, '쓰레기를 넣으면 쓰레기가 나온다.'는 데이터 제 1원칙에 따라, 해당 데이터는 SQL로 적용이 어렵다고 판단했다.(이제부터라도 교통정리를 잘 해야할 것 같은데, 모르겠음..난 아는 게 하나도 없음...ㅎ)

혹시 참고할 자료가 필요한 분들에게 도움이 될 수 있기에, GCP에서 실습이 가능한 링크([Predicting Visitor Purchases with a Classification Model with BigQuery ML](https://www.cloudskillsboost.google/course_sessions/823412/labs/102262))를 제공한다.

> ### Big Query
```shell
# create a example dataset
bq mk $DATASET_NAME

# to create realtime table(empty schema that you will stream into later)
bq mk \
--time_partitioning_field timestamp \
--schema
$SCHEMA_ID:string, $SCHEMA_IDX:integer, latitude:float, longitude:float, \
timestamp:timestamp, $SCHEMA_FEATURE_0:float, $SCHEMA_FEATURE_1:float, $SCHEMA_FEATURE_2:string, \
$SCHEMA_FEATURE_3:integer -t $DATASET_NAME.realtime

```


> ### Cloud Storage
```shell
gsutil mb -p $DEVSHELL_PROJECT_ID \
    -c regional    \
    -l $MY_ZONE    \
    gs://$BUCKET_NAME/

# copy the training images into your bucket
gsutil -m cp -r gs://$TRAIN_BUCKET_NAME/* gs://$BUCKET_NAME/

# copy the template file to your cloud shell instance
gsutil cp gs://$TRAIN_BUCKET_NAME/data.csv .

# update the csv with the files in your project
sed -i -e "s/$ORIGIN_PATH/$BUCKET_NAME/g" ./data.csv

# upload this updated csv file to your bucket
gsutil cp ./data.csv gs://$BUCKET_NAME/
```


> ### AutoML

통상 라벨 별 100 개의 학습데이터셋을 불러오며, custom model을 학습하는 데에는 55분에서 90분 정도가 소요된다. 


> ### Google Cloud Skills Boost [^badges]
* Completion Badge
    * [Google Cloud Essentials](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1743709)
    * [Baseline: Infrastructure](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1757293)
    * [Baseline: Data, ML, AI](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1767263)
    * [Cloud Engineering](https://www.cloudskillsboost.google/quests/66)  :construction: 2/6 :construction:
* Skill badge
    * [Create and Manage Cloud Resources](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1759790)
    * [Perform Foundational Infrastructure Tasks in Google Cloud](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/17593428)
    * [Perform Foundational Data, ML, and AI Tasks in Google Cloud](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1769828)
    * [Engineer Data in Google Cloud](https://www.cloudskillsboost.google/quests/132) :construction:
* Digital badge
    * [Kubernetes in Google Cloud](https://www.cloudskillsboost.google/quests/29)  :construction: 1/5 :construction:
* Course
    * [Google Cloud Fundamentals: Core Infrastructure](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1753227)
    * [Google Cloud Big Data and Machine Learning Fundamentals](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1762243)
    * [Modernizing Data Lakes and Data Warehouses with Google Cloud](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1771612)
    * [Building Resilient Streaming Analytics Systems on Google Cloud](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1778507)
    * [Serverless Data Processing with Dataflow: Foundations](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1769918)
    * [How Google Does Machine Learning](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1771330)
    * [Smart Analytics, Machine Learning, and AI on Google Cloud](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1781392)
    * [Serverless Data Processing with Dataflow: Develop Pipeline](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1787317)
    * [Serverless Data Processing with Dataflow: Operations](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1790320)
    * [Preparing for the Google Cloud Professional Data Engineer Exam](https://www.cloudskillsboost.google/course_templates/72) :construction: 6/8 :construction:
    * [Getting Started With Application Development](https://www.cloudskillsboost.google/course_templates/22) :construction: 5/7 :construction:

계속해서 `Qwiklabs`를 통해 훈련하면서 느낀 것은 리눅스 기본적인 것만 알고서 응용을 잘 하려면 진짜 시도하는 게 중요하다는 점이다. 'multi-region말고 single-region이 latency를 낮출 수 있다.'와 같은 코드 외에 알 수 있는 부분도 시도하면서, 그리고 문서를 더 찾아보면서 알 수 있는 내용이다. 사막의 모래 한 알 정도는 알고 있다고 생각했는데, 미세먼지만도 못한 나의 얕음에 최소한 무엇을 할 수 있는 사람인지를 정의할 목적으로 `Qwiklabs`이나 `Sololearn`을 통해 공부해야겠다.(사실 `Azure`도 구독은 했는데 취업 동향을 보니까 `AWS`나 `GCP`가 많아서, 언젠가 "Hybrid" 관련 컨셉을 공부할 때, 구독을 업그레이드할 듯.)

Lab에서 문제를 풀이할 때에 가급적 CLI로 퓰이하려고 해서, bash파일로 작성은 해뒀는데 공개해도 되는지를 모르겠다. Challenge Lab을 있는 과정을 기준으로, 5번의 skill badge를 수료할 쯤이면 공개 여부를 결정하도록 하겠다.

그리고 나의 이해를 증명할 방법으로 자격증이란 수단을 사용해야 한다면, [Google Cloud Certification](https://cloud.google.com/certification)을 통ß해 보일 계획인데, 우선은 공부에 더 집중해야 할 듯.

[refs: Learning Path](./path.md)


---
[^badges]: Certification 배지가 발급되는 과정이면 develop profile로 바로 연동할텐데(Lab과 커뮤니티 프로필은 다름), Certification 시험 신청 전까지 계속해서 공부할 동기를 잃지 않을 목적으로 공유함.
[^gcloud-cli-overview]: [gcloud CLI overview](https://cloud.google.com/sdk/gcloud)
[^regions-and-zones]: [Regions and zones](https://cloud.google.com/compute/docs/regions-zones)
[^standard-cluster-architecture]: [Standard Cluster Architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
[^load-balancing]: 
    * [External TCP/UDP Network Load Balancing overview](https://cloud.google.com/load-balancing/docs/network)
    * [External HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/https)