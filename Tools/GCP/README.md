# Google Cloud 

`Google Cloud Essentials`를 완료했는데, 숙지가 되지 않은 상태라 복습 겸 계속해서 퀘스트를 수료하기까지 반복해서 작성할 것 같은 내용 정리 목적으로 생성함.

## Contexts
* [Basic](#basic)
* [Set-ups](#set-ups)
* [Cluster](#cluster)
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


가급적 CLI로 퓰이하려고 해서, bash파일로 작성은 해뒀는데 공개해도 되는지를 몰라서 Challenge Lab을 있는 과정을 기준으로, 5번의 skill badge를 수료할 쯤이면 공개 여부를 결정하도록 하겠다

> ### Google Cloud Skills Boost [^badges]
* Completion Badge
    * [Google Cloud Essentials](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1743709)
    * [Baseline: Infrastructure](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1757293)
    * [Cloud Engineering](https://www.cloudskillsboost.google/quests/66)  :construction: 2/6 :construction:
* Skill badge
    * [Create and Manage Cloud Resources](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1759790)
    * [Perform Foundational Infrastructure Tasks in Google Cloud](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/17593428)
    * [Engineer Data in Google Cloud](https://www.cloudskillsboost.google/quests/132) :construction:
* Digital badge
    * [Kubernetes in Google Cloud](https://www.cloudskillsboost.google/quests/29)  :construction: 1/5 :construction:
* Course
    * [Google Cloud Fundamentals: Core Infrastructure](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1753227)
    * [Google Cloud Big Data and Machine Learning Fundamentals](https://www.cloudskillsboost.google/course_templates/3) :construction: 4/7 :construction:
    * [Getting Started With Application Development](https://www.cloudskillsboost.google/course_templates/22) :construction: 3/7 :construction:

---
[^badges]: Certification 배지가 발급되는 과정이면 develop profile로 바로 연동할텐데(Lab과 커뮤니티 프로필은 다름), Certification 시험 신청 전까지 계속해서 공부할 동기를 잃지 않을 목적으로 공유함.
[^gcloud-cli-overview]: [gcloud CLI overview](https://cloud.google.com/sdk/gcloud)
[^regions-and-zones]: [Regions and zones](https://cloud.google.com/compute/docs/regions-zones)
[^standard-cluster-architecture]: [Standard Cluster Architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
[^load-balancing]: 
    * [External TCP/UDP Network Load Balancing overview](https://cloud.google.com/load-balancing/docs/network)
    * [External HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/https)