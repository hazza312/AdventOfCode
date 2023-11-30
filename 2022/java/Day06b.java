import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Queue;


/**
 * Implementation that streams from stdin -- doesn't read all n characters of input in one go, and stops as soon
 * as a match is found. Uses a queue and to maintain the frequency of last m lookback characters.
 * Assumes input are all lowercase characters a-z.
 * Time complexity O(n), space complexity O(m).
 *
 * java Day06b m
 * java Day06b m < input6.txt
 */
public class Day06b {

    /**
     * For large m, check the counts array.
     * The size of this array is not dependent on n or m, but the range of values each character can take
     * (assumed above to be in a-z). With the assumption, this is a constant-time operation.
     */
    static boolean allUnique(Queue<Character> buffer, int[] counts, int markerLength) {
        if (markerLength > counts.length) {
            return Arrays.stream(counts).allMatch(n -> n <= 1);
        }

        return buffer.stream().allMatch(c -> counts[c - 'a'] <= 1);
    }

    static void add(char c, Queue<Character> buffer, int[] counts) {
        buffer.add(c);
        counts[c - 'a']++;
    }

    static void remove(Queue<Character> buffer, int[] counts) {
        counts[buffer.remove() - 'a']--;
    }

    static int findMarker(InputStream in, int markerLength) throws IOException {
        Queue<Character> q = new ArrayDeque<>(markerLength);
        int[] counts = new int['z' - 'a' + 1];

        int i = 0;
        for (; i < markerLength; i++) {
            add((char) in.read(), q, counts);
        }

        int c;
        while ((c = in.read()) != -1) {
            if (allUnique(q, counts, markerLength)) {
                return i;
            }

            remove(q, counts);
            add((char) c, q, counts);
            i++;
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        System.out.println(findMarker(System.in, Integer.parseInt(args[0])));
    }
}
