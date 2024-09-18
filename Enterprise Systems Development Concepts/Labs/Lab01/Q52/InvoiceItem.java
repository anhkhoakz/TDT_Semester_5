public class InvoiceItem {
    public static void main(String[] args) {
        InvoiceItem i = new InvoiceItem("1", "Apple", 5, 2.5);
        System.out.println(i.getID());
        System.out.println(i.getDesc());
        System.out.println(i.getQty());
        i.setQty(10);
        System.out.println(i.getUnitPrice());
        i.setUnitPrice(5.0);
        System.out.println(i.getTotal());
        System.out.println(i.toString());

    }

    private String id;
    private String desc;
    private int qty;
    private double unitPrice;

    public InvoiceItem(String id, String desc, int qty, double unitPrice) {
        this.id = id;
        this.desc = desc;
        this.qty = qty;
        this.unitPrice = unitPrice;
    }

    public String getID() {
        return this.id;
    }

    public String getDesc() {
        return this.desc;
    }

    public int getQty() {
        return this.qty;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }

    public double getUnitPrice() {
        return this.unitPrice;
    }

    public void setUnitPrice(double unitPrice) {
        this.unitPrice = unitPrice;
    }

    public double getTotal() {
        return this.unitPrice * this.qty;
    }

    public String toString() {
        return "InvoiceItem[id=" + this.id + ",desc=" + this.desc + ",qty=" + this.qty + ",unitPrice=" + this.unitPrice
                + "]";
    }
}
