public class Palindrome {

    public static void main(String[] args) {
        String str = "A man a plan a canal Panama";
        if (isPalindrome(str)) {
            System.out.println("Palindrome");
        } else {
            System.out.println("Not palindrome");
        }
    }

    public static boolean isPalindrome(String str) {
        str = str.toLowerCase();
        str = str.replaceAll(" ", "");
        for (int i = 0; i < str.length() / 2; i++) {
            if (str.charAt(i) != str.charAt(str.length() - i - 1)) {
                return false;
            }
        }
        return true;
    }
}