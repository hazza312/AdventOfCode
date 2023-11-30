import org.antlr.v4.runtime.misc.IntervalSet;
import org.apache.commons.math3.geometry.euclidean.twod.Vector2D;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Day15 {
    static final Pattern INPUT_PATTERN = Pattern.compile(".*?x=(-?\\d+), y=(-?\\d+).*?x=(-?\\d+), y=(-?\\d+)");
    static final int MAX_GRID_SIZE = 4000000;
    static final IntervalSet[] EXCLUDED_BY_Y = new IntervalSet[MAX_GRID_SIZE + 1];

    static final IntervalSet getOrInitRow(int y) {
        if (EXCLUDED_BY_Y[y] == null) {
            EXCLUDED_BY_Y[y] = new IntervalSet();
        }

        return EXCLUDED_BY_Y[y];
    }

    static void excludeInManhattanRadius(Vector2D sensor, Vector2D beacon) {
        int r = (int) sensor.distance1(beacon);
        int x1 = (int) sensor.getX();
        int y1 = (int) sensor.getY();

        for (int y = Math.max(0, y1 - r); y <= Math.min(y1 + r, MAX_GRID_SIZE); y++) {
            int yDiff = Math.abs(y - y1);
            getOrInitRow(y).add(x1 - r + yDiff, x1 + r - yDiff);
        }
    }

    static long getTuningFrequency(int n) {
        for (int y = 0; y <= n; y++) {
            IntervalSet blockedRegion = getOrInitRow(y);
            IntervalSet okRegion = blockedRegion.complement(0, n);
            if (okRegion.size() == 1) {
                return okRegion.get(0) * (long) n + y;
            }
        }

        return -1;
    }

    static int numPointsBeaconImpossible(int y, Collection<Vector2D> beacons) {
        IntervalSet row = EXCLUDED_BY_Y[y];
        for (Vector2D beacon: beacons) {
            if (beacon.getY() == y) {
                row.remove((int) beacon.getX());
            }
        }
        return row.size();
    }


    public static void main(String[] args) {
        List<Vector2D> beacons = new ArrayList<>();

        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            String line = in.nextLine();
            Matcher match= INPUT_PATTERN.matcher(line);
            if (match.matches()) {
                Vector2D sensor = new Vector2D(Integer.parseInt(match.group(1)), Integer.parseInt(match.group(2)));
                Vector2D beacon = new Vector2D(Integer.parseInt(match.group(3)), Integer.parseInt(match.group(4)));
                excludeInManhattanRadius(sensor, beacon);
                beacons.add(beacon);
            }
        }

        System.out.println(numPointsBeaconImpossible(2000000, beacons));
        System.out.println(getTuningFrequency(MAX_GRID_SIZE));
    }
}
