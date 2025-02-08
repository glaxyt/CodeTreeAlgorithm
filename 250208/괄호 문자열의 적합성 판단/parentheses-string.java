import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        String word = sc.next();
        Stack<Character> s = new Stack<>(); 
        for(int i = 0; i < word.length(); i++) {
            if(word.charAt(i) == '(') {
                s.push('(');
            } else {
                if(!s.isEmpty()) {
                    s.pop();
                } else {
                    System.out.println("No");
                    System.exit(0);
                }
            }
        }

        if (s.isEmpty()) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}