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