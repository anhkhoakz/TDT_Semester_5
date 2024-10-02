import java.io.Serializable;

public class Person implements Serializable {
    private String surname;
    private int count;
    private double pctwhite;
    private double pctblack;

    public Person(String surname, int count, double pctwhite, double pctblack) {
        this.surname = surname;
        this.count = count;
        this.pctwhite = pctwhite;
        this.pctblack = pctblack;
    }

    public String getSurname() {
        return surname;
    }

    public int getCount() {
        return count;
    }

    public double getPctwhite() {
        return pctwhite;
    }

    public double getPctblack() {
        return pctblack;
    }

    public String toString() {
        return getSurname() + ": count=" + getCount() + ", pctwhite=" + getPctwhite() + ", pctblack=" + getPctblack();
    }
}