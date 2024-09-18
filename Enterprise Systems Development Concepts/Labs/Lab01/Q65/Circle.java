package Q65;

public class Circle extends Shape {
    public static void main(String[] args) {
        Circle c = new Circle(1.0);
        System.out.println(c);
        System.out.println(c.getArea());
        System.out.println(c.getPerimeter());
    }

    protected double radius;

    public Circle() {
    }

    public Circle(double radius) {
        this.radius = radius;
    }

    public Circle(double radius, String color, boolean filled) {
        super(color, filled);
        this.radius = radius;
    }

    public double getRadius() {
        return this.radius;
    }

    public void setRadius(double radius) {
        this.radius = radius;
    }

    public double getArea() {
        return Math.PI * Math.pow(this.radius, 2);
    }

    public double getPerimeter() {
        return 2 * Math.PI * this.radius;
    }

    public String toString() {
        return String.format("Circle[radius=%.2f]", this.radius);
    }

}
