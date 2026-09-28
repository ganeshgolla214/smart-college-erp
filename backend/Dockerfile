FROM eclipse-temurin:21-jdk-alpine
WORKDIR /app
COPY pom.xml .
RUN apk add --no-cache maven && mvn dependency:go-offline -q
COPY src ./src
RUN mvn package -DskipTests -q
EXPOSE 8080
ENTRYPOINT ["java","-jar","target/college-erp-1.0.0.jar"]
