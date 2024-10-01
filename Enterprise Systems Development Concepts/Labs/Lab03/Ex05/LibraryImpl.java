import java.rmi.RemoteException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class LibraryImpl implements Library {
    private Map<String, Boolean> books;

    protected LibraryImpl() throws RemoteException {
        super();
        books = new HashMap<>();
        initializeCatalog();
    }

    private void initializeCatalog() {
        books.put("Book A", true);
        books.put("Book B", true);
        books.put("Book C", true);
        books.put("Book D", true);
    }

    public List<String> searchBooks(String query) throws RemoteException {
        List<String> results = new ArrayList<>();
        for (String book : books.keySet()) {
            if (book.toLowerCase().contains(query.toLowerCase())) {
                results.add(book);
            }
        }
        return results;
    }

    public boolean checkOutBook(String bookTitle) throws RemoteException {
        if (books.containsKey(bookTitle) && books.get(bookTitle)) {
            books.put(bookTitle, false);
            return true;
        }
        return false;
    }

    public boolean returnBook(String bookTitle) {
        if (books.containsKey(bookTitle) && !books.get(bookTitle)) {
            books.put(bookTitle, true);
            return true;
        }
        return false;
    }
}
