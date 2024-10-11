// DO NOT USE PACKAGE

import java.io.Serializable;

public class Student implements Serializable {

    private static final long serialVersionUID = 1L;
    private String id, name, gender, major;
    private double gpa;

    public Student() {

    }

    public Student(String id, String name, String gender, double gpa, String major) {
        this.id = id;
        this.name = name;
        this.gender = gender;
        this.major = major;
        this.gpa = gpa;
    }

    public Student(Student s) {
        this.id = s.id;
        this.name = s.name;
        this.gender = s.gender;
        this.major = s.major;
        this.gpa = s.gpa;
    }

    public void copy(Student s) {
        this.id = s.id;
        this.name = s.name;
        this.gender = s.gender;
        this.major = s.major;
        this.gpa = s.gpa;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getMajor() {
        return major;
    }

    public void setMajor(String major) {
        this.major = major;
    }

    public double getGpa() {
        return gpa;
    }

    public void setGpa(double gpa) {
        this.gpa = gpa;
    }

    @Override
    public String toString() {
        return "Student{" + "id=" + id + ", name=" + name + ", gender=" + gender + ", major=" + major + ", gpa=" + gpa
                + '}';
    }

}
