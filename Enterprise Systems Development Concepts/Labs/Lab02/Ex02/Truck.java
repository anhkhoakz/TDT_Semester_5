package Ex02;

import java.io.Serial;

public class Truck extends Vehicle {

    @Serial
    private static long serialVersionUID = 1L;

    private int weight;

    public Truck(String make, String model, int year, int weight) {
        super(make, model, year);
        this.weight = weight;
    }

    public int getWeight() {
        return this.weight;
    }

    @Override
    public String toString() {
        return "Truck [make=" + getMake() + ", model=" + getModel() + ", year=" + getYear() + ", weight=" + weight
                + "]";
    }
}
