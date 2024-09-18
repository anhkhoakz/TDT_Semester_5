package Q58_Q59;

public class TestMyCircle {
    public static void main(String[] args) {
        MyCircle c1 = new MyCircle(1, 2, 5);
        System.out.println(c1.toString());
        System.out.println(c1.getCenterXY()[0] + " " + c1.getCenterXY()[1]);
        System.out.println("Area is " + c1.getArea());
        System.out.println("Circumference is " + c1.getCircumference());

        MyCircle c2 = new MyCircle(3, 4, 6);
        System.out.println(c2.toString());
        System.out.println(c2.getCenterXY()[0] + " " + c2.getCenterXY()[1]);
        System.out.println("Area is " + c2.getArea());
        System.out.println("Circumference is " + c2.getCircumference());

        System.out.println("Distance between c1 and c2 is " + c1.distance(c2));
    }
}