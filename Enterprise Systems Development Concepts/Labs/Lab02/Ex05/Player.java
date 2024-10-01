package Ex05;

import java.io.Serializable;
import java.io.Serial;

public class Player implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String name;
    private String position;
    private int number;

    public Player(String name, String position, int number) {
        this.name = name;
        this.position = position;
        this.number = number;
    }

    public String getName() {
        return name;
    }

    public String getPosition() {
        return position;
    }

    public int getNumber() {
        return number;
    }

    @Override
    public String toString() {
        return "Player [name=" + getName() + ", position=" + getPosition() + ", number=" + getNumber() + "]";
    }

}
