package Ex02;

import java.io.FileInputStream;
import java.io.ObjectInputStream;
import java.io.IOException;

public class Deserial {
    public static void main(String[] args) {
        Car car = null;
        try {
            FileInputStream fileIn = new FileInputStream("car.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);

            car = (Car) in.readObject();

            in.close();
            fileIn.close();
        } catch (IOException i) {
            throw new RuntimeException(i);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

        System.out.println(car.toString());

        Truck truck = null;
        try {
            FileInputStream fileIn = new FileInputStream("truck.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);

            truck = (Truck) in.readObject();

            in.close();
            fileIn.close();
        } catch (IOException i) {
            throw new RuntimeException(i);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

        System.out.println(truck.toString());

        Motorcycle motorcycle = null;
        try {
            FileInputStream fileIn = new FileInputStream("motorcycle.ser");
            ObjectInputStream in = new ObjectInputStream(fileIn);

            motorcycle = (Motorcycle) in.readObject();

            in.close();
            fileIn.close();
        } catch (IOException i) {
            throw new RuntimeException(i);
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }

        System.out.println(motorcycle.toString());

    }
}
