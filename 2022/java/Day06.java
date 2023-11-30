import java.util.Scanner;


/**
 * Implementation that reads whole input in one go. Assumes input are all lowercase characters a-z.
 * Time complexity O(n * m), space complexity O(n).
 *
 * java Day06 m
 * java Day06 m < input6.txt
 */
public class Day06 {
    static boolean rangeIsUnique(String s, int start, int end) {
        for (int i = start; i < end - 1; i++) {
            for (int j = i + 1; j < end; j++) {
                if (s.charAt(i) == s.charAt(j)) {
                    return false;
                }
            }
        }

        return true;
    }

    static int findMarker(String s, int markerLength) {
        for (int i = markerLength; i < s.length(); i++) {
            if (rangeIsUnique(s, i - markerLength, i)) {
                return i;
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        String input = new Scanner(System.in).nextLine();
        System.out.println(findMarker(input, 4));
        System.out.println(findMarker(input, 14));
    }
}
