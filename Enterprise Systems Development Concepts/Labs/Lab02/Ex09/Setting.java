package Ex09;

import java.io.Serial;
import java.io.Serializable;

public class Setting implements Serializable {
    @Serial
    private static long serialVersionUID = 1L;

    private String username;
    private String password;
    private boolean autoLogin;

    public Setting(String username, String password, boolean autoLogin) {
        this.username = username;
        this.password = password;
        this.autoLogin = autoLogin;
    }

    public String getUsername() {
        return this.username;
    }

    public String getPassword() {
        return this.password;
    }

    public boolean getAutoLogin() {
        return this.autoLogin;
    }

    public String toString() {
        return "Setting [username=" + getUsername() + ", password=" + getPassword() + ", autoLogin=" + getAutoLogin()
                + "]";
    }
}
