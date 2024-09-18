package Q64;

public class Staff extends Person {
    public static void main(String[] args) {
        Staff s = new Staff("Madison Maldonado", "753, rue Christophe Collet", "Software Engineering", 12345);
        System.out.println(s);
    }

    private String school;
    private double pay;

    public Staff(String name, String address, String school, double pay) {
        super(name, address);
        this.school = school;
        this.pay = pay;
    }

    public String getSchool() {
        return this.school;
    }

    public void setSchool(String value) {
        this.school = value;
    }

    public double getPay() {
        return this.pay;
    }

    public void setPay(double value) {
        this.pay = value;
    }

    public String toString() {
        return String.format("Staff[%s,school=%s,pay=%.2f]", super.toString(),
                this.school, this.pay);
    }

}
