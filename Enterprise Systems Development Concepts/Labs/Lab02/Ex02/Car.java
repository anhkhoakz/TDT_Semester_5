package Ex02;

import java.io.Serial;

public class Car extends Vehicle {

    @Serial
    private static long serialVersionUID = 1L;

    private int doors;

    public Car(String make, String model, int year, int doors) {
        super(make, model, year);
        this.doors = doors;
    }

    public int getDoors() {
        return this.doors;
    }

    public String toString() {
        return "Car [make=" + getMake() + ", model=" + getModel() + ", year=" + getYear() + ", doors=" + doors + "]";
    }
}
