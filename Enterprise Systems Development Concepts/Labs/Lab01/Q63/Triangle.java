package Q63;

public class Triangle implements Shape {
    private double base;
    private double height;

    public double getArea() {
        return base * height / 2;
    }

    public String toString() {
        return String.format("Triangle[base=%.2f,height=%.2f,area=%.2f]", base, height, getArea());
    }

}
