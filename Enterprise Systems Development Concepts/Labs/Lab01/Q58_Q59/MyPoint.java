package Q58_Q59;

public class MyPoint {
    public static void main(String[] args) {
        MyPoint p1 = new MyPoint(3, 2);
        MyPoint p2 = new MyPoint(1, 4);
        System.out.println(p1.getX());
        System.out.println(p1.getY());
        System.out.println(p2.getXY()[0] + " " + p2.getXY()[1]);
        System.out.println(p1.distance(p2));
        System.out.println(p1.distance(5, 6));
        System.out.println(p1.distance());

    }

    private int x;
    private int y;

    public MyPoint() {
        this.x = 0;
        this.y = 0;
    }

    public MyPoint(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public int getX() {
        return this.x;
    }

    public void setX(int value) {
        this.x = value;
    }

    public int getY() {
        return this.y;
    }

    public void setY(int value) {
        this.y = value;
    }

    public int[] getXY() {
        return new int[] { this.x, this.y };
    }

    public void setXY(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public String toString() {
        return "(" + this.x + "," + this.y + ")";
    }

    public double distance(int x, int y) {
        return Math.sqrt(Math.pow(this.x - x, 2) + Math.pow(this.y - y, 2));
    }

    public double distance(MyPoint another) {
        return Math.sqrt(Math.pow(this.x - another.x, 2) + Math.pow(this.y - another.y, 2));
    }

    public double distance() {
        return Math.sqrt(Math.pow(this.x, 2) + Math.pow(this.y, 2));
    }
}
