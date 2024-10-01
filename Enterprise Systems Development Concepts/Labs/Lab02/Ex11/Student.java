package Ex11;

import java.io.Serializable;
import java.io.Serial;

public class Student implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private String email;
    private double[] testScores = new double[3];

    public Student(String name, String email, double[] testScores) {
        this.name = name;
        this.email = email;
        this.testScores = testScores;
    }

    public String getName() {
        return name;
    }

    public String getEmail() {
        return email;
    }

    public double[] getTestScores() {
        return testScores;
    }

    @Override
    public String toString() {
        return "Student[" + getName() + ", " + getEmail() + ", " + getTestScores() + "]";
    }
}