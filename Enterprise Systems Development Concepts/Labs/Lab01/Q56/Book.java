package Q56;

public class Book {
    public static void main(String[] args) {
        Author author1 = new Author("Kara Smith", "martinezluc@peron.fr", 'm');
        Book book1 = new Book("The Systems Analyst Information Systems Development Project Selection and Management",
                author1, 15.99, 100);
        System.out.println(book1.toString());
        book1.setPrice(19.99);
        book1.setQty(50);
        System.out.println(book1.toString());

    }

    private String name;
    private Author author;
    private double price;
    private int qty = 0;

    public Book(String name, Author author, double price) {
        this.name = name;
        this.author = author;
        this.price = price;
    }

    public Book(String name, Author author, double price, int qty) {
        this.name = name;
        this.author = author;
        this.price = price;
        this.qty = qty;
    }

    public String getName() {
        return this.name;
    }

    public Author getAuthor() {
        return this.author;
    }

    public double getPrice() {
        return this.price;
    }

    public void setPrice(double value) {
        this.price = value;
    }

    public int getQty() {
        return this.qty;
    }

    public void setQty(int value) {
        this.qty = value;
    }

    public String toString() {
        return String.format("Book[name=%s,%s,price=%.2f,qty=%d]", this.name, this.author.toString(), this.price,
                this.qty);
    }
}
