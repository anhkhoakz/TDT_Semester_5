public class Employee {
    public static void main(String[] args) {
        Employee e = new Employee(1, "Vickie", "Johnson", 862);
        System.out.println(e.getID());
        System.out.println(e.getFirstName());
        System.out.println(e.getLastName());
        System.out.println(e.getName());
        System.out.println(e.getSalary());
        System.out.println(e.getAnualSalary());
        System.out.println(e.raiseSalary(10));
        System.out.println(e.toString());
    }

    private int id;
    private String firstName;
    private String lastName;
    private int salary;

    public Employee(int id, String firstName, String lastName, int salary) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.salary = salary;
    }

    public int getID() {
        return this.id;
    }

    public String getFirstName() {
        return this.firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public String getName() {
        return this.firstName + " " + this.lastName;
    }

    public int getSalary() {
        return this.salary;
    }

    public int getAnualSalary() {
        return this.salary * 12;
    }

    public int raiseSalary(int percent) {
        return this.salary + (this.salary * percent / 100);
    }

    public String toString() {
        return "Employee[id=" + id + ",name=" + getName() + ",salary=" + salary + "]";
    }
}
