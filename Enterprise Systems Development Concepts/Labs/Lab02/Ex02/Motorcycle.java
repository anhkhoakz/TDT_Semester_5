package Ex02;

public class Motorcycle extends Vehicle {
    private int cc;

    public Motorcycle(String make, String model, int year, int cc) {
        super(make, model, year);
        this.cc = cc;
    }

    public int getCc() {
        return this.cc;
    }

    @Override
    public String toString() {
        return "Motorcycle [make=" + getMake() + ", model=" + getModel() + ", year=" + getYear() + ", cc=" + cc + "]";
    }

}
