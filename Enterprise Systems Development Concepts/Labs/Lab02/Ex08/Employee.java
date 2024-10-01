package Ex08;

import java.io.Serial;
import java.io.Serializable;

public class Employee implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private double salary;
    private transient String password;

    public String getName() {
        return name;
    }

    public double getSalary() {
        return salary;
    }

    public String getPassword() {
        return password;
    }

    public Employee(String name, double salary, String password) {
        this.name = name;
        this.salary = salary;
        this.password = password;
    }

    public String toString() {
        return "Employee [name=" + getName() + ", salary=" + getSalary() + ", password=" + getPassword() + "]";
    }
}
