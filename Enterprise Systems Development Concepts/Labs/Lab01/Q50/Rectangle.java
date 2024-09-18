public class Rectangle {
    public static void main(String[] args) {
        Rectangle r = new Rectangle(2.0f, 3.0f);
        System.out.println(r.getLength());
        System.out.println(r.getWidth());
        System.out.println(r.getArea());
        System.out.println(r.getPerimeter());
        System.out.println(r.toString());
    }

    private float length = 1.0f;
    private float width = 1.0f;

    public Rectangle() {

    }

    public Rectangle(float length, float width) {
        this.length = length;
        this.width = width;
    }

    public float getLength() {
        return this.length;
    }

    public void setLength(float value) {
        this.length = value;
    }

    public float getWidth() {
        return this.width;
    }

    public void setWidth(float value) {
        this.width = value;
    }

    public double getArea() {
        return this.length * this.width;
    }

    public double getPerimeter() {
        return 2 * (this.length + this.width);
    }

    public String toString() {
        return "Rectangle[length=" + length + ",width=" + width + "]";
    }
}