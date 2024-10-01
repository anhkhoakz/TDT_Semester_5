package Ex06;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

public class Serial {
    public static void main(String[] args) {
        Circle circle = new Circle(5.7);
        try {
            FileOutputStream fileOutput = new FileOutputStream("circle.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(circle);

            out.close();
            fileOutput.close();

            System.out.println("Serialized data is saved in circle.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        Rectangle rectangle = new Rectangle(5.2, 7.3);
        try {
            FileOutputStream fileOutput = new FileOutputStream("rectangle.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(rectangle);

            out.close();
            fileOutput.close();

            System.out.println("Serialized data is saved in rectangle.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        Triangle triangle = new Triangle(3.0, 4.0, 5.0);
        try {
            FileOutputStream fileOutput = new FileOutputStream("triangle.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOutput);

            out.writeObject(triangle);

            out.close();
            fileOutput.close();

            System.out.println("Serialized data is saved in triangle.ser");
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
