import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Double a = sc.nextDouble();
        int decimalPlaces = 2;

        double scale = Math.pow(10, decimalPlaces);
        double rounded = Math.round((a + 1.5) * scale) / scale;

        System.out.println(rounded);
    }
}