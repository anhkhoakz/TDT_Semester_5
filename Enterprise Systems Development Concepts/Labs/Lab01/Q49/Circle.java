
public class Circle {
    public static void main(String[] args) {
        Circle c = new Circle(2.0);
        System.out.println(c.getArea());
    }

    private double radius;
    private String color;

    public Circle() {
        this.radius = 1.0;
        this.color = "red";

    }

    public Circle(double radius) {
        this.radius = radius;

    }

    public double getRadius() {
        return this.radius;
    }

    public double getArea() {
        return Math.PI * Math.pow(this.radius, 2);
    }

}
