# MLOps
## Contents
* [Overview](#overview)
* [CI for ML](#ci-for-ml)
* [CD for ML](#cd-for-ml)
* [CT for ML](#ct-for-ml)
* [Study](#study)

## Overview
![Hidden Technical Debt in Machine Learning Systems](https://i0.wp.com/neptune.ai/wp-content/uploads/2022/10/Technical-debt-MLOps.png?ssl=1)

통상적으로 MLOps는 ML을 위한 DevOps라고 생각하면 된다. ML을 위한 DevOps라는 것은 ML을 위한 CI/CD/CT를 의미한다.

* CI: Continuous Integration
* CD: Continuous Delivery/Deployment
* CT: Continuous Training

[Google Cloud | MLOps: 머신러닝의 지속적 배포 및 자동화 파이프라인](https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?hl=ko) 에 따르면 MLOps는 level에 따라 다음과 같이 구분된다.

* Level 0: Manual(수동 프로세스)
* Level 1: Automated(ML Pipeline 자동화)
* Level 2: Continuous(CI/CD 파이프라인 자동화)

그렇다면 ML을 위한 CI/CD/CT는 어떻게 이루어지는가?

## CI for ML
CI for ML은 ML Pipeline을 구축하는 것이다. 즉, 일종의 CI Workflow를 구축하는 것이다. CI Workflow는 다음과 같은 과정을 거친다.
1. Data Collection
2. Data Preprocessing
3. Data Analysis
4. Model Training
5. Model Evaluation(Validation, Testing)

## CD for ML
CD for ML은 CI for ML에서 구축한 ML Pipeline에서 Production에 사용할 모델 서빙하는 것이다. 즉, ML Pipeline에서 Model Deployment 단계를 구축하는 것이다. Model Deployment 단계는 다음과 같은 과정을 거친다.
1. Model Serving
2. Model Inference
3. Model Deployment
4. Model Monitoring

## CT for ML
CT for ML은 CD for ML에서 구축한 ML Pipeline에서 Production에 사용할 모델을 지속적으로 학습시키는 것이다. 즉, ML Pipeline에서 Model Re-Training 단계를 자동화하여 구축하는 것이다. 여기서 고려해야 할 것은 다음과 같다.

* Model Re-Training을 언제 할 것인가?
* Model Re-Training을 어떻게 할 것인가?
* Model Re-Training을 어디서 할 것인가?

이를 위해 다음과 같은 방법을 사용한다.

* Model Re-Training을 언제 할 것인가?
  * Batch Processing
  * Stream Processing
* Model Re-Training을 어떻게 할 것인가?
    * Online Learning
    * Offline Learning
* Model Re-Training을 어디서 할 것인가?
    * Cloud
    * Edge

## Study
### Basic
### CI for ML
### CD for ML
### CT for ML


---
refs
* https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning?hl=ko
* https://neptune.ai/blog/mlops-architecture-guide
* https://www.datacamp.com/blog/10-awesome-resources-for-learning-mlops

[Go to Contents](#contents)