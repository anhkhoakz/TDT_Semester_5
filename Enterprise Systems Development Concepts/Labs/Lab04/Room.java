public class Room {
    private int roomType;
    private double price;
    private int availability;

    public Room(int roomType, double price, int availability) {
        this.roomType = roomType;
        this.price = price;
        this.availability = availability;
    }

    public int getRoomType() {
        return roomType;
    }

    public void setRoomType(int roomType) {
        this.roomType = roomType;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }

    public int getAvailability() {
        return availability;
    }

    public void setAvailability(int availability) {
        this.availability = availability;
    }
}