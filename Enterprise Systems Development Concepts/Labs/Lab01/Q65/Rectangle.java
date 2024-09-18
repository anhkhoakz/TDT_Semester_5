package Q65;

public class Rectangle extends Shape {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(1.0, 2.0);
        System.out.println(r);
        System.out.println(r.getArea());
        System.out.println(r.getPerimeter());
    }

    protected double width;
    protected double length;

    public Rectangle() {
    }

    public Rectangle(double width, double length) {
        this.width = width;
        this.length = length;
    }

    public Rectangle(double width, double length, String color, boolean filled) {
        super(color, filled);
        this.width = width;
        this.length = length;
    }

    public double getWidth() {
        return this.width;
    }

    public void setWidth(double width) {
        this.width = width;
    }

    public double getLength() {
        return this.length;
    }

    public void setLength(double length) {
        this.length = length;
    }

    public double getArea() {
        return this.width * this.length;
    }

    public double getPerimeter() {
        return 2 * (this.width + this.length);
    }

    public String toString() {
        return String.format("Rectangle[width=%.2f,length=%.2f]", this.width, this.length);
    }
}
