public class RotateArray {

    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4, 5 };
        int n = 2;
        int len = arr.length;
        n = n % len;
        reverseArray(arr, 0, len - 1);
        reverseArray(arr, 0, n - 1);
        reverseArray(arr, n, len - 1);
        for (int i : arr) {
            System.out.println(i);
        }
    }

    public static void reverseArray(int[] arr, int start, int end) {
        while (start < end) {
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;
            start++;
            end--;
        }
    }
}