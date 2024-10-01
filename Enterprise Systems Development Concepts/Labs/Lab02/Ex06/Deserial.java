package Ex06;

import java.io.FileInputStream;
import java.io.ObjectInputStream;

public class Deserial {
    public static void main(String[] args) {
        Circle circle = null;

        try {
            FileInputStream fileInput = new FileInputStream("circle.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            circle = (Circle) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + circle);

        Rectangle rectangle = null;
        try {
            FileInputStream fileInput = new FileInputStream("rectangle.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            rectangle = (Rectangle) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + rectangle);

        Triangle triangle = null;
        try {
            FileInputStream fileInput = new FileInputStream("triangle.ser");
            ObjectInputStream in = new ObjectInputStream(fileInput);

            triangle = (Triangle) in.readObject();

            in.close();
            fileInput.close();
        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        System.out.println("Deserialized data: " + triangle);
    }
}
