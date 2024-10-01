package Ex06;

import java.io.Serial;
import java.io.Serializable;

public class Triangle implements Shape, Serializable {
    @Serial
    private static long serialVersionUID = 1L;
    private double sideA;
    private double sideB;
    private double sideC;

    public double getSideA() {
        return sideA;
    }

    public double getSideB() {
        return sideB;
    }

    public double getSideC() {
        return sideC;
    }

    public Triangle(double sideA, double sideB, double sideC) {
        this.sideA = sideA;
        this.sideB = sideB;
        this.sideC = sideC;
    }

    public double calculatePerimeter() {
        return sideA + sideB + sideC;
    }

    public double calculateArea() {
        double halfPerimeter = calculatePerimeter() / 2;
        return Math.sqrt(halfPerimeter * (halfPerimeter - sideA) * (halfPerimeter - sideB) * (halfPerimeter - sideC));
    }

    public String toString() {
        return "Triangle [side1=" + getSideA() + ", side2=" + getSideB() + ", side3=" + getSideC() + ", area="
                + calculateArea() + ", perimeter=" + calculatePerimeter() + "]";
    }
}
