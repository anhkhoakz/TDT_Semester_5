
public class Main {
    public static void main(String[] args) {
        try {
            MyClass obj1 = new MyClass(1, "First");
            MyClass obj2 = (MyClass) obj1.clone();

            obj1.display();
            obj2.display();

        } catch (Exception e) {
            System.err.println(e);
        }

    }
}
