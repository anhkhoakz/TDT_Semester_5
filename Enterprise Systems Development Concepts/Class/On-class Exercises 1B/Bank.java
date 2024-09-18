public class Bank {
    public static void main(String[] args) {
        Bank bank = new Bank(8916, "Jasmine Jones", 1000);
        System.out.println(bank.balance);
        bank.deposit(500);
        System.out.println(bank.balance);
        bank.withdraw(1501);
        System.out.println(bank.balance);
    }

    private int accountNumber;
    private String accountHolderName;
    private double balance;

    public Bank(int accountNumber, String accountHolderName, int balance) {
        this.accountNumber = accountNumber;
        this.accountHolderName = accountHolderName;
        this.balance = balance;
    }

    public void deposit(double amount) {
        this.balance += amount;
    }

    public void withdraw(double amount) {
        if (this.balance < amount || this.balance == 0) {
            System.out.println("Insufficient balance");
        } else {
            this.balance -= amount;
        }
    }

}
