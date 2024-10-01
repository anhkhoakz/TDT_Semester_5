package Ex10;

import java.io.Serial;
import java.io.Serializable;

public class Address implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;
    private String street;
    private String city;
    private int zipCode;

    public Address(String street, String city, int zipCode) {
        this.street = street;
        this.city = city;
        this.zipCode = zipCode;
    }

    public String getStreet() {
        return this.street;
    }

    public String getCity() {
        return this.city;
    }

    public int getZipCode() {
        return this.zipCode;
    }

    public String toString() {
        return "Address [street=" + getStreet() + ", city=" + getCity() + ", zipCode=" + getZipCode() + "]";
    }
}
