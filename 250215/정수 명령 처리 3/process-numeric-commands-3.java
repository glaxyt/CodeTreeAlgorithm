import java.util.Deque;
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Deque<Integer> dq = new ArrayDeque<>();
        Scanner sc = new Scanner(System.in);

        Integer n = sc.nextInt();

        for(int i = 0; i < n; i++){
            String command = sc.next();
            if(command.equals("push_front")) {
                Integer num = sc.nextInt();
                dq.addFirst(num);
            } else if(command.equals("push_back")) {
                Integer num = sc.nextInt();
                dq.addLast(num);
            } else if(command.equals("pop_front")) {
                System.out.println(dq.pollFirst());
            } else if(command.equals("pop_back")) {
                System.out.println(dq.pollLast());
            } else if(command.equals("front")) {
                System.out.println(dq.peekFirst());
            } else if(command.equals("back")) {
                System.out.println(dq.peekLast());
            } else if(command.equals("size")) {
                System.out.println(dq.size());
            } else if(command.equals("empty")) {
                if(dq.isEmpty()) {
                    System.out.println("1");
                    continue;
                }
                System.out.println("0");
            }
        }   
    }
}