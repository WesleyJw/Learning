# Repo to Study

## Spark on Kubernetes

### PySpark scripts

PySpark Files:
- users.py: A simple PySpark script to create a data frame from a dictionary and save in S3 bucket on AWS.
- 1_users_by_city.py: A simple PySpark script to create a data frame from a dictionary and show in command prompt.

Yaml's Files:
- 1_users_by_city.yaml: A script to create a PySpark spark application on Kubernetes with spark operator.k8s from an image pre config.
- 2_users_by_city_delight.yaml: A script to create a PySpark spark application on Kubernetes with spark operator.k8s from an image created and personalized hosted in my Docker Hub account. This YAML was configured to run a Delight setup to get cluster resources and metrics.
- 3_aws_integration.yaml: A script to create a PySpark spark application on Kubernetes with spark operator.k8s from an image created and personalized hosted in my Docker Hub account. This application was configured to connect to AWS bucket to read and write files. In this application, We change the main application file to read files dynamically from a S3 bucket and run in spark app.
- kind.yaml: To create a Kubernetes cluster with four nodes.

Make files:
- A make file was created to download jars to configure a spark app and to build the image with specific configuration. Then the image was push to my docker hub.
