import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        Queue<Integer> q = new LinkedList<>();
        
        Integer n = sc.nextInt();
        for(int i = 0; i < n; i++) {
            String command = sc.next();

            if(command.equals("push")) {
                Integer num = sc.nextInt();
                q.add(num);
            } else if(command.equals("front")) {
                if(!q.isEmpty()) {
                    System.out.println(q.peek());
                }
            } else if(command.equals("size")) {
                System.out.println(q.size());
            } else if(command.equals("empty")) {
                if(q.isEmpty()) {
                    System.out.println("1");
                } else {
                    System.out.println("0");
                }
            } else if(command.equals("pop")) {
                if(!q.isEmpty()) {
                    System.out.println(q.poll());
                }
            } else {
                System.out.println("wrong command");
            }
        }
    }
}