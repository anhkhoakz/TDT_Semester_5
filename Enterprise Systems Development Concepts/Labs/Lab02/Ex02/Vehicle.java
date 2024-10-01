package Ex02;

import java.io.Serializable;
import java.io.Serial;

/**
 * Vehicle
 */
public class Vehicle implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String make;
    private String model;
    private int year;

    public Vehicle(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public String getMake() {
        return this.make;
    }

    public String getModel() {
        return this.model;
    }

    public int getYear() {
        return this.year;
    }

    @Override
    public String toString() {
        return "Vehicle [make=" + make + ", model=" + model + ", year=" + year + "]";
    }
}
