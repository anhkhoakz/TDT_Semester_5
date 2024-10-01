package Ex11;

import java.io.Serializable;
import java.io.Serial;

public class Student3 implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private int age;
    private double[] testScores = new double[3];

    public Student3(String name, int age, double[] testScores) {
        this.name = name;
        this.age = age;
        this.testScores = testScores;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    public double[] getTestScores() {
        return testScores;
    }

    public String toString() {
        return "Student[" + getName() + ", " + getAge() + ", " + getTestScores() + "]";
    }
}
