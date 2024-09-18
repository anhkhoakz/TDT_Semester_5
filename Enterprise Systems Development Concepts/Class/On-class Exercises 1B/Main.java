public class Main {
    public static void main(String[] args) {
        Shape circle = new Circle(2);
        Shape rectangle = new Rectangle(3, 5);
        System.out.println(circle.area());
        System.out.println(rectangle.area());
    }
}
