## Configure Saprk Cluster with Kind

### Kind Create Cluster

How to create a cluster using a script yaml.

```

kind create cluster --name spark-demo --config.yaml

```

Create a namespace in kubernets

```

kubectl create namespace spark-processing

```

Adding a helm repo:

```
$ helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator

```

### Installing Spark Operator

To install the Kubernets Operator for Apache Spark use the helm repositorie with the command:

```
$ helm install spark-series spark-operator/spark-operator --namespace spark-operator --create-namespace --set sparkJobNamespace=spark-processing

```

To validated if the installation is on, test with:

```
kubectl get podes -n spark-operator
```

### Running an Application on Kubenerts

Write a yaml file with the specification about your application and excute with the following code:

```
kubectl apply -f hello-world.yaml
```

You need to change the serviceAccount paramener from yaml model scrit. To get the service account in your workspace do:

```
kubectl get serviceaccount -n spark-processing
```

- 1. Get the Service Account details
Use the following command to get the details of the spark-series-spark service account within the spark-processing namespace:
```
kubectl get serviceaccount spark-series-spark -n spark-processing -o yaml
```

### How To Interact With Logs

```
kubectl describe sparkapplication spark-pi -n spark-processing

 kubectl logs -f users-by-city-driver -n spark-processing
```

### How to Monitoring Spark Cluster With Delight

You basically need to add some config rows to your yaml file. In your yaml file put this code: 

```
 deps:
    jars:
      - "https://oss.sonatype.org/content/repositories/snapshots/co/datamechanics/delight_2.12/latest-SNAPSHOT/delight_2.12-latest-SNAPSHOT.jar"
  sparkConf:
    "spark.delight.accessToken.secret": "token_code"
    "spark.extraListeners": "co.datamechanics.delight.DelightListener"
```

Replace new_token with your delight token. It is necessary to do a singin in Delight page and to create a new token. Delight doesn't work yet with spark version more than 3.2, then we go to build a new image to docker hub. We create a new dockerfile to build the image..

```
docker build -t wesleyjw/spark-series:spark-py-3.2.4 .
```

After build the image we can to do a push to dockerhub.

```
docker push wesleyjw/spark-series:spark-py-3.2.4
```

Deploy the new application:

```
sudo kubectl apply -f scripts/yamls/2_users-by-city_delight.yaml
```

If you need redeploy an application you need to delete the SaprkApplication created when you apply scritp with kubectl. Every time that you need to redeploy an application it is necessary to remove the spark application.

### Integration With AWS

To connect a spark application with a aws bucket (S3), We need to config some jars. Therefore, We need to change the yaml file and put some config rows:

```
sparkConf:
    spark.hadoop.fs.s3a.acess.key: "FIUJEWHFUIWBCBWEUYFGDYEWBCMNVJ"
    spark.hadoop.fs.s3a.secret.key: "IUVY7TVUYHITGUR6TYGFYGguyfrcvdhyguygfuytHYUTYTV"
    spark.hadoop.fs.s3a.impl: "org.apache.hadoop.fs.s3a.S3AFileSystem"
    spark.hadoop.fs.s3a.aws.credentials.provider: "org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider"
    org.apache.hadoop.fs.s3a.path.style.access: "True"
    org.apache.hadoop.fs.s3a.fast.upload: "True"
    org.apache.hadoop.fs.s3a.multipart.size: "104857600"
    org.apache.hadoop.fs.s3a.connection.maximum: "100"
```

We go to change the mainApplicationFile paramenter. Now the main file to run the application is in the S3 bucket on aws, with this change We don't need to put the file script in the image. This metodology is more flexible to change files and redeploy the spark application.

```
mainApplicationFile: "s3a://spok-scripts/users.py"
```

After that and before We apply our application, We need to build an image with spark. We create a Makefile witht the specification to the project.   


```
SPARK_VERSION=3.3.2
PACKAGE=spark-$(SPARK_VERSION)-bin-hadoop3

build:
  # Download the Jars 
	wget -P /tmp https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.2/hadoop-aws-3.3.2.jar
	wget -P /tmp https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.98/aws-java-sdk-bundle-1.12.98.jar


  # Download the spark
	curl https://dlcdn.apache.org/spark/spark-$(SPARK_VERSION)/$(PACKAGE).tgz | tar -xz -C /tmp/

  # Move jars to /tmp/$(PACKAGE)/jars/ directory
	mv /tmp/hadoop-aws-3.3.2.jar /tmp/$(PACKAGE)/jars/
	mv /tmp/aws-java-sdk-bundle-1.12.98.jar /tmp/$(PACKAGE)/jars/

  # Buil the image with the spark bash
	cd /tmp/$(PACKAGE) \
	&& ./bin/docker-image-tool.sh -t latest -p ./kubernetes/dockerfiles/spark/bindings/python/Dockerfile build

	rm -rf /tmp/$(PACKAGE)
```

Now, you need just applied the command make from root directory of the file created.
To push the image to Docker hub, firstly We need to change the tag image to Our image name. Then just do the push. 

```
docker tag spark-py:latest wesleyjw/spark-series:spark-3.3.2_hadoop-3-aws
docker push wesleyjw/spark-series:spark-3.3.2_hadoop-3-aws
```

### Native Orchestration

Running Spark applications on a schedule using a [ScheduledSaprkApplicaiton](https://github.com/GoogleCloudPlatform/spark-on-k8s-operator/blob/master/docs/user-guide.md). To scheduler a spark application, We need to change the YAML file following this step:

- kind: ScheduledSaprkApplicaiton
- spec: 
  - schedule: with parameters of time to run the application 
  - and another configs to cluster.
  - template: With all configurations of your application.


### Airflow Orchestration

To install Apache Airflow on K8s, We can use the helm repo:

```
$ helm install airflow -f helm/airflow/values.yaml helm/airflow -n orchestrator --create-namespace
```

To habilite permission to Airflow submit Spark YAML. 

```
$ kubectl apply -f helm/airflow/config-permission.yaml

```
Map the port of the localhost to the container.

```
$ kubectl port-forward svc/airflow-webserver 8080:8080 --namespace orchestrator

# Login
Usuario: admin
Senha: admin
```

To run the application open your Aiflow page and sart your job.