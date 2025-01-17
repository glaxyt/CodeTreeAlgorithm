import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double d = sc.nextDouble();
        Double uppper_d = Math.round(30.48 * d * 10.0) / 10.0;
        System.out.println(uppper_d);
    }
}