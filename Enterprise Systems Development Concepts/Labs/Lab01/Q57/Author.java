public class Author {
    private String name;
    private String email;
    private char gender;

    public Author(String name, String email, char gender) {
        this.name = name;
        this.email = email;
        this.gender = gender;
    }

    public String getName() {
        return this.name;
    }

    public String getEmail() {
        return this.email;
    }

    public void setEmail(String value) {
        this.email = value;
    }

    public char getGender() {
        return this.gender;
    }

    @Override
    public String toString() {
        return String.format("Author[name=%s,email=%s,gender=%s]", this.name, this.email, this.gender);
    }

}
