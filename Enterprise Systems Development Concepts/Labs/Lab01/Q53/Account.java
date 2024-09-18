public class Account {
    public static void main(String[] args) {
        Account a = new Account("1", "Khoa", 1000);
        Account b = new Account("2", "Khanh", 500);
        System.out.println(a.getID());
        System.out.println(a.getName());
        System.out.println(a.getBalance());
        System.out.println(a.credit(500));
        System.out.println(a.debit(200));
        System.out.println(a.toString());
        System.out.println(b.toString());
        System.out.println(a.transferTo(b, 300));
        System.out.println(a.toString());
        System.out.println(b.toString());
    }

    private String id;
    private String name;
    private int balance = 0;

    public Account(String id, String name) {
        this.id = id;
        this.name = name;
    }

    public Account(String id, String name, int balance) {
        this.id = id;
        this.name = name;
        this.balance = balance;
    }

    public String getID() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public int getBalance() {
        return this.balance;
    }

    public int credit(int amount) {
        this.balance += amount;
        return this.balance;
    }

    public int debit(int amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
        } else {
            System.out.println("Amount exceeded balance");

        }
        return this.balance;
    }

    public int transferTo(Account account, int amount) {
        if (amount <= this.balance) {
            this.balance -= amount;
            account.credit(amount);
        } else {
            System.out.println("Amount exceeded balance");

        }
        return this.balance;
    }

    public String toString() {
        return "Account[id=" + this.id + ",name=" + this.name + ",balance=" + this.balance + "]";
    }
}
