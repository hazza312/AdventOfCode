import java.util.*;
import java.util.function.BiPredicate;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class Day12 {

    static <S> Optional<S> bfs(S initial, Function<S, Collection<S>> nextStates, Predicate<S> endPredicate) {
        Queue<S> queue = new ArrayDeque<>();
        queue.add(initial);

        while(!queue.isEmpty()) {
            S curr = queue.remove();
            if (endPredicate.test(curr)) {
                return Optional.of(curr);
            }

            queue.addAll(nextStates.apply(curr));
        }

        return Optional.empty();
    }


    static List<char[]> grid = new ArrayList<>();
    record State(int x, int y) {};

    static boolean hasEdge(State s1, State s2) {
        char src = grid.get(s1.y)[s1.x] == 'S' ? 'a' : grid.get(s1.y)[s1.x];
        char dst = grid.get(s2.y)[s2.x] == 'E' ? 'z' : grid.get(s2.y)[s2.x];
        return dst <= src + 1;
    }

    static List<State> nextStates(State curr, Map<State, Integer> visited, boolean forward) {
        Predicate<State> inGrid = s -> s.x >= 0 && s.x < grid.get(0).length && s.y >= 0 && s.y < grid.size();
        BiPredicate<State, State> hasEdge = forward ? Day12::hasEdge : (s1, s2) -> hasEdge(s2, s1);

        int currSteps = visited.getOrDefault(curr, 0);
        List<State> ret = Stream.of(
                new State(curr.x+1, curr.y),
                new State(curr.x-1, curr.y),
                new State(curr.x, curr.y+1),
                new State(curr.x, curr.y-1))
                .filter(inGrid)
                .filter(s -> !visited.containsKey(s))
                .filter(n -> hasEdge.test(curr, n))
                .collect(Collectors.toList());

        ret.forEach(s -> visited.put(s, currSteps + 1));
        return ret;
    }

    static State find(char c) {
        for (int y = 0; y < grid.size(); y++) {
            char[] row = grid.get(y);
            for (int x = 0; x < grid.get(0).length; x++) {
                if (row[x] == c) {
                    return new State(x, y);
                }
            }
        }
        throw new IllegalArgumentException("no such location");
    }

    static int findMinPathLength(char initalChar, String end, boolean forwardEdgeDirection) {
        Map<State, Integer> visited = new HashMap<>();
        State start = find(initalChar);

        Function<State, Collection<State>> nextStates = s -> nextStates(s, visited, forwardEdgeDirection);
        Predicate<State> reachedGoal = s -> end.contains(Character.toString(grid.get(s.y)[s.x]));

        return visited.get(bfs(start, nextStates, reachedGoal).get());
    }


    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        while (in.hasNextLine()) {
            grid.add(in.nextLine().toCharArray());
        }

        System.out.println(findMinPathLength('S', "E", true));
        System.out.println(findMinPathLength('E', "Sa", false));
    }
}
