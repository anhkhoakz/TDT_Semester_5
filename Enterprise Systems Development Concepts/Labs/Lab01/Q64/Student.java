package Q64;

public class Student extends Person {

    public static void main(String[] args) {
        Student s = new Student("Madison Maldonado", "753, rue Christophe Collet",
                "Software Engineering", 2012, 12345);
        System.out.println(s);
    }

    private String program;
    private int year;
    private double fee;

    public Student(String name, String address, String program, int year, double fee) {
        super(name, address);
        this.program = program;
        this.year = year;
        this.fee = fee;
    }

    public String getProgram() {
        return this.program;
    }

    public void setProgram(String value) {
        this.program = value;
    }

    public int getYear() {
        return this.year;
    }

    public void setYear(int value) {
        this.year = value;
    }

    public double getFee() {
        return this.fee;
    }

    public void setFee(double value) {
        this.fee = value;
    }

    public String toString() {
        return String.format("Student[%s,program=%s,year=%d,fee=%.2f]", super.toString(), this.program, this.year,
                this.fee);
    }

}
