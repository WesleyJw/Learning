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

