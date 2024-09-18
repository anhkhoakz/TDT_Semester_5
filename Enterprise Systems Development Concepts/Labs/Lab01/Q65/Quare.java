package Q65;

public class Quare extends Rectangle {
    public static void main(String[] args) {
        Quare q = new Quare(3.0);
        System.out.println(q);
        System.out.println(q.getArea());
        System.out.println(q.getPerimeter());
    }

    public Quare() {
    }

    public Quare(double side) {
        super(side, side);
    }

    public Quare(double side, String color, boolean filled) {
        super(side, side, color, filled);
    }

    public double getSide() {
        return this.width;
    }

    public void setSide(double side) {
        this.width = side;
        this.length = side;
    }

    public void setWidth(double side) {
        this.width = side;
        this.length = side;
    }

    public void setLength(double side) {
        this.width = side;
        this.length = side;
    }

    public String toString() {
        return String.format("Quare[side=%.2f]", this.width);
    }

}
