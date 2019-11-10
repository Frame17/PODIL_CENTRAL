FROM openjdk:11-jre-slim
ADD build/libs/server-1.0-SNAPSHOT.jar topic-simple.jar
ENTRYPOINT ["/bin/bash", "-c", "java -jar /topic-simple.jar"]
