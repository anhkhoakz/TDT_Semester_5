public class Customer {
    private String name;
    private String ssn;
    private int roomType;

    public Customer(String name, String ssn, int roomType) {
        this.name = name;
        this.ssn = ssn;
        this.roomType = roomType;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getSsn() {
        return ssn;
    }

    public void setSsn(String ssn) {
        this.ssn = ssn;
    }

    public int getRoomType() {
        return roomType;
    }

    public void setRoomType(int roomType) {
        this.roomType = roomType;
    }
}