public class MyClass implements Cloneable {
    private int id;
    private String name;

    @Override
    protected Object clone() throws CloneNotSupportedException {
        return super.clone();
    }

    public MyClass(int id, String name) {
        this.id = id;
        this.name = name;
    }

    public void display() {
        System.out.println("Id: " + id + " Name: " + name);
    }
}