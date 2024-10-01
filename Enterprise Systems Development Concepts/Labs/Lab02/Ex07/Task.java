package Ex07;

import java.io.Serial;
import java.io.Serializable;
import java.util.Date;

public class Task implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String description;
    private Date dueDate;

    public Task(String description, Date dueDate) {
        this.description = description;
        this.dueDate = dueDate;
    }

    public String getDescription() {
        return description;
    }

    public Date getDueDate() {
        return dueDate;
    }

    public String toString() {
        return "Task [description=" + getDescription() + ", dueDate=" + getDueDate() + "]";
    }
}
