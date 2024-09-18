package Q63;

public class Rectangle implements Shape {
    private double length;
    private double width;

    public double getArea() {
        return length * width;
    }

    public String toString() {
        return String.format("Rectangle[length=%.2f,width=%.2f,area%.2f]", length, width, getArea());
    }
}
