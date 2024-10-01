package Ex06;

import java.io.Serial;
import java.io.Serializable;

public class Rectangle implements Shape, Serializable {

    @Serial
    private static long serialVersionUID = 1L;
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double calculateArea() {
        return width * height;
    }

    public double calculatePerimeter() {
        return 2 * (width + height);
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public String toString() {
        return "Rectangle [width=" + getWidth() + ", height=" + getHeight() + ", area=" + calculateArea()
                + ", perimeter="
                + calculatePerimeter() + "]";
    }
}
