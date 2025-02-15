import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Deque<Integer> dq = new ArrayDeque<>();
        Scanner sc = new Scanner(System.in);

        Integer n = sc.nextInt();
        for(int i = 1; i <= n; i++) {
            dq.addLast(i);
        }

        while(!(dq.size() == 1)) {
            dq.pollFirst();
            int num = dq.pollFirst();
            dq.addLast(num);
        }
        System.out.println(dq.pollFirst());
    }
}