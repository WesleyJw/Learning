SPARK_VERSION=3.3.4
PACKAGE=spark-$(SPARK_VERSION)-bin-hadoop3

build:
	wget -P /tmp https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
	wget -P /tmp https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.98/aws-java-sdk-bundle-1.12.98.jar

	curl https://dlcdn.apache.org/spark/spark-$(SPARK_VERSION)/$(PACKAGE).tgz | tar -xz -C /tmp/

	mv /tmp/hadoop-aws-3.3.4.jar /tmp/$(PACKAGE)/jars/
	mv /tmp/aws-java-sdk-bundle-1.12.98.jar /tmp/$(PACKAGE)/jars/

	cd /tmp/$(PACKAGE) \
	&& ./bin/docker-image-tool.sh -t latest -p ./kubernetes/dockerfiles/spark/bindings/python/Dockerfile build

	rm -rf /tmp/$(PACKAGE)

# docker tag spark-py:latest wesleyjw/spark-series:spark-3.3.2_hadoop-3-aws
# docker push wesleyjw/spark-series:spark-3.3.2_hadoop-3-aws