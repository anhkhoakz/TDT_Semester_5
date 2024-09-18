public class Time {
    public static void main(String[] args) {
        Time t = new Time(23, 59, 59);
        System.out.println(t.getHour());
        System.out.println(t.getMinute());
        System.out.println(t.getSecond());
        System.out.println(t.toString());
        System.out.println(t.nextSecond().toString());
        System.out.println(t.previousSecond().toString());
    }

    private int hour;
    private int minute;
    private int second;

    public Time(int hour, int minute, int second) {
        this.hour = hour;
        this.minute = minute;
        this.second = second;
    }

    public int getHour() {
        return this.hour;
    }

    public int getMinute() {
        return this.minute;
    }

    public int getSecond() {
        return this.second;
    }

    public void setHour(int value) {
        this.hour = value;
    }

    public void setMinute(int value) {
        this.minute = value;
    }

    public void setSecond(int value) {
        this.second = value;
    }

    public String toString() {
        return String.format("%02d:%02d:%02d", this.hour, this.minute, this.second);
    }

    public Time nextSecond() {
        this.second++;
        if (this.second == 60) {
            this.second = 0;
            this.minute++;
            if (this.minute == 60) {
                this.minute = 0;
                this.hour++;
                if (this.hour == 24) {
                    this.hour = 0;
                }
            }
        }
        return this;
    }

    public Time previousSecond() {
        this.second--;
        if (this.second == -1) {
            this.second = 59;
            this.minute--;
            if (this.minute == -1) {
                this.minute = 59;
                this.hour--;
                if (this.hour == -1) {
                    this.hour = 23;
                }
            }
        }
        return this;
    }
}
