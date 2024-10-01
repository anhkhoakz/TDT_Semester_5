package Ex04;

import java.io.Serializable;
import java.io.Serial;

public class Student implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private String id;
    private double[] testScores = new double[3];

    public Student(String name, String id, double[] testScores) {
        this.name = name;
        this.id = id;
        this.testScores = testScores;
    }

    public String getName() {
        return name;
    }

    public String getId() {
        return id;
    }

    public double[] getTestScores() {
        return testScores;
    }

    public String toString() {
        return "Student[" + getName() + ", " + getId() + ", " + getTestScores() + "]";
    }
}
