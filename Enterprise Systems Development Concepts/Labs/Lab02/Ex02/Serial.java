package Ex02;

import java.io.FileOutputStream;
import java.io.ObjectOutputStream;
import java.io.IOException;

public class Serial {
    public static void main(String[] args) {

        Car car = new Car("Toyota", "Camry", 2022, 4);
        try {
            FileOutputStream fileOut = new FileOutputStream("car.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(car);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in car.ser");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        Truck truck = new Truck("Toyota", "Hilux", 2022, 4000);
        try {
            FileOutputStream fileOut = new FileOutputStream("truck.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(truck);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in truck.ser");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        Motorcycle motorcycle = new Motorcycle("Honda", "Wave", 2022, 110);
        try {
            FileOutputStream fileOut = new FileOutputStream("motorcycle.ser");
            ObjectOutputStream out = new ObjectOutputStream(fileOut);
            out.writeObject(motorcycle);
            out.close();
            fileOut.close();
            System.out.println("Serialized data is saved in motorcycle.ser");
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }
}
