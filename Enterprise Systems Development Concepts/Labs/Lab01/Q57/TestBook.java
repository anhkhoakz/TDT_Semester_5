public class TestBook {
    public static void main(String[] args) {
        Author author1 = new Author("Kyle Howe", "martinezluc@peron.fr", 'm');
        Author author2 = new Author("Kara Smith", "sgomez@garcia.com", 'f');
        Author author3 = new Author("Maria Burke", "vdelmas@lombard.fr", 'f');
        Author[] authors = { author1, author2, author3 };

        Book book1 = new Book("The Systems Analyst Information Systems Development Project Selection and Management",
                authors, 29.99, 100);

        book1.setPrice(19.99);
        book1.setQty(50);

        System.out.println(book1.toString());

        System.out.println("Book Name: " + book1.getName());
        System.out.println("Book Price: " + book1.getPrice());
        System.out.println("Book Quantity: " + book1.getQty());
        System.out.print("Book Authors: ");
        System.out.println(book1.toString());
    }
}
