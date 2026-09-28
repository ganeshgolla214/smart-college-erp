package com.ganesh.erp;
import jakarta.persistence.*;
@Entity @Table(name="students") public class Student { @Id @GeneratedValue(strategy=GenerationType.IDENTITY) public Long id; @Column(nullable=false) public String name; @Column(unique=true,nullable=false) public String email; public String department; public int year; public double attendance; public Student(){} public Student(String n,String e,String d,int y,double a){name=n;email=e;department=d;year=y;attendance=a;} }
