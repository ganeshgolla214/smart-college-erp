package com.ganesh.erp;
import jakarta.persistence.*;
@Entity @Table(name="students") public class Student{@Id @GeneratedValue(strategy=GenerationType.IDENTITY) public Long id;public String name;@Column(unique=true)public String email;public String department;public int year;public double attendance;}