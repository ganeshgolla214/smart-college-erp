package com.ganesh.erp;
import org.springframework.boot.CommandLineRunner;import org.springframework.context.annotation.Bean;import org.springframework.context.annotation.Configuration;
@Configuration public class SeedData { @Bean CommandLineRunner seed(StudentRepository r){return a->{if(r.count()==0){r.saveAll(java.util.List.of(new Student("Ananya Rao","ananya@college.local","CSE",3,91.2),new Student("Rahul Kumar","rahul@college.local","ECE",2,84.5),new Student("Priya Shah","priya@college.local","CSE",4,88.0),new Student("Arjun Reddy","arjun@college.local","IT",3,76.4)));}};} }
