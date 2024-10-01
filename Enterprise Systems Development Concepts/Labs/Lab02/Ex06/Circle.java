package Ex06;

import java.io.Serial;
import java.io.Serializable;

public class Circle implements Shape, Serializable {

    @Serial
    private static long serialVersionUID = 1L;
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double calculateArea() {
        return Math.PI * Math.pow(radius, 2);
    }

    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }

    public double getRadius() {
        return radius;
    }

    public String toString() {
        return "Circle [radius=" + getRadius() + ", area=" + calculateArea() + ", perimeter=" + calculatePerimeter()
                + "]";
    }

}
