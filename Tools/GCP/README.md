# Google Cloud 

`Google Cloud Essentials`를 완료했는데, 숙지가 되지 않은 상태라 복습 겸 계속해서 퀘스트를 수료하기까지 반복해서 작성할 것 같은 내용 정리 목적으로 생성함.

## Contexts
* [Basic](#basic)
* [Set-ups](#set-ups)
* [Cluster](#cluster)


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


---
[^gcloud-cli-overview]: [gcloud CLI overview](https://cloud.google.com/sdk/gcloud)
[^regions-and-zones]: [Regions and zones](https://cloud.google.com/compute/docs/regions-zones)
[^standard-cluster-architecture]: [Standard Cluster Architecture](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
[^load-balancing]: 
    * [External TCP/UDP Network Load Balancing overview](https://cloud.google.com/load-balancing/docs/network)
    * [External HTTP(S) Load Balancing overview](https://cloud.google.com/load-balancing/docs/https)