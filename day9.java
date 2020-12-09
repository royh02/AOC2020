import java.util.*;
import java.io.File;
import java.io.FileNotFoundException;

public class day9 {
    public static void main(String[] args) {
        ArrayList<Long> input = new ArrayList<>();
        try {
            File puzzle = new File("./puzzle-inputs/day9.txt");
            Scanner reader = new Scanner(puzzle);
            while (reader.hasNextLine()) {
                input.add(Long.parseLong(reader.nextLine()));
            }
            reader.close();
        } catch (FileNotFoundException e) {
            System.out.println("Xmas is ruined!");
            e.printStackTrace();
        }
        ArrayList<Long> numList = new ArrayList<>();
        long weak = -1;
        for (int i = 0; i < input.size(); i++) {
            long val = input.get(i);
            if (numList.size() <= 25) {
                numList.add(val);
            } else {
                if (!hasPairs(numList, val)) {
                    System.out.println("Weakness: " + val);
                    weak = val;
                    break;
                }
                numList.add(val);
                numList.remove(0);
            }
        }
        long[] range = minMax(input, weak);
        System.out.println(range[0] + range[1]);
    }

    static boolean hasPairs(ArrayList<Long> numList, long n) {
        HashSet<Long> s = new HashSet<Long>();
        for (int i = 0; i < numList.size(); i++) {
            long temp = n - numList.get(i);

            if (s.contains(temp)) {
                return true;
            }
            s.add(numList.get(i));
        }
        return false;
    }

    static int[] subSetSum(ArrayList<Long> input, long val) {
        long curr_sum;

        for (int i = 0; i < input.size() - 1; i++) {
            curr_sum = input.get(i);

            for (int j = i + 1; j < input.size(); j++) {
                if (curr_sum == val) {
                    int[] firstLast = {i, j-1};
                    return firstLast;
                }
                if (curr_sum < val) {
                    curr_sum += input.get(j);
                }
            }
        }
        System.out.println("None found");
        return new int[2];
    }

    static long[] minMax(ArrayList<Long> input, long val) {
        int[] range = subSetSum(input, val);
        List<Long> sorted = input.subList(range[0], range[1]);
        Collections.sort(sorted);
        long[] mM = {sorted.get(0), sorted.get(sorted.size()-1)};
        return mM;
    }
}