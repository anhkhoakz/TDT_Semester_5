public class Book {
    private String name;
    private Author[] author;
    private double price;
    private int qty = 0;

    public Book(String name, Author[] author, double price) {
        this.name = name;
        this.author = author;
        this.price = price;
    }

    public Book(String name, Author[] author, double price, int qty) {
        this.name = name;
        this.author = author;
        this.price = price;
        this.qty = qty;
    }

    public String getName() {
        return this.name;
    }

    public Author[] getAuthor() {
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
        String authorString = "";
        for (Author author : this.author) {
            authorString += author.toString() + ", ";
        }
        authorString = authorString.substring(0, authorString.length() - 2);

        return String.format("Book[name=%s, authors},={%s price=%.2f, qty=%d]", this.name, authorString,
                this.price, this.qty);
    }
}
