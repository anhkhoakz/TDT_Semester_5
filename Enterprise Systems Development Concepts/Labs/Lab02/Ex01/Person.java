package Ex01;

import java.io.Serializable;
import java.io.Serial;

public class Person implements Serializable {

    @Serial
    private static long serialVersionUID = 1L;
    private String name;
    private int age;
    private String address;

    public Person(String name, int age, String address) {
        this.name = name;
        this.age = age;
        this.address = address;
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public String getAddress() {
        return this.address;
    }

}
