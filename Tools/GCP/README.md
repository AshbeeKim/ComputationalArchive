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



> ### Badges [^badges]
* Quest
    * [Google Cloud Essentials](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1743709)
    * [Create and Manage Cloud Resources](https://www.cloudskillsboost.google/quests/120) :construction: 5/6 :construction:
    * [Baseline: Infrastructure](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1757293)
    * [Perform Foundational Infrastructure Tasks in Google Cloud](https://www.cloudskillsboost.google/quests/118) :construction: 5/6 :construction:
    * [Cloud Engineering](https://www.cloudskillsboost.google/quests/66)  :construction: 2/6 :construction:
    * [Kubernetes in Google Cloud](https://www.cloudskillsboost.google/quests/29)  :construction: 1/5 :construction:
    * [Engineer Data in Google Cloud](https://www.cloudskillsboost.google/quests/132)
* Course
    * [Google Cloud Fundamentals: Core Infrastructure](https://www.cloudskillsboost.google/public_profiles/97e8f540-bf60-4f75-9a8e-025c1cc95a24/badges/1753227)
    * [Getting Started With Application Development](https://www.cloudskillsboost.google/course_templates/22) :construction:
    * [Google Cloud Big Data and Machine Learning Fundamentals](https://www.cloudskillsboost.google/course_templates/3) :construction:

---
[^badges]: Certification 배지가 발급되는 과정이면 develop profile로 바로 연동할텐데(Lab과 커뮤니티 프로필은 다름), Certification 시험 신청 전까지 계속해서 공부할 동기를 잃지 않을 목적으로 공유함.
[^gcloud-cli-overview]: [gcloud CLI overview](https://cloud.google.com/sdk/gcloud)
[^regions-and-zones]: [Regions and zones](https://cloud.google.com/compute/docs/regions-zones)
[^standard-cluster-architecture]: [Standard Cluster Architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
[^load-balancing]: 
    * [External TCP/UDP Network Load Balancing overview](https://cloud.google.com/load-balancing/docs/network)
    * [External HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/https)