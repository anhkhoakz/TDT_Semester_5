public class Date {
    public static void main(String[] args) {
        Date d = new Date(2021, 12, 31);
        System.out.println(d.getYear());
        System.out.println(d.getMonth());
        System.out.println(d.getDay());
        System.out.println(d.toString());
        System.out.println(d.setDate(2022, 1, 1));
        System.out.println(d.toString());
    }

    private int day;
    private int month;
    private int year;

    public Date(int day, int month, int year) {
        this.day = day;
        this.month = month;
        this.year = year;
    }

    public int getDay() {
        return this.day;
    }

    public int getMonth() {
        return this.month;
    }

    public int getYear() {
        return this.year;
    }

    public void setDay(int value) {
        this.day = value;
    }

    public void setMonth(int value) {
        this.month = value;
    }

    public void setYear(int value) {
        this.year = value;
    }

    public String toString() {
        return this.year + "/" + this.month + "/" + this.day;
    }

    public String setDate(int year, int month, int day) {
        this.year = year;
        this.month = month;
        this.day = day;
        return this.year + "/" + this.month + "/" + this.day;
    }

}
