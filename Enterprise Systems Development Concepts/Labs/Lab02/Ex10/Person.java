package Ex10;

import java.io.Serial;
import java.io.Serializable;

public class Person implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private Address address;

    public Person(String name, Address address) {
        this.name = name;
        this.address = address;
    }

    public String getName() {
        return this.name;
    }

    public Address getAddress() {
        return this.address;
    }

    public String toString() {
        return "Person [name=" + getName() + ", " + getAddress() + "]";
    }

}
