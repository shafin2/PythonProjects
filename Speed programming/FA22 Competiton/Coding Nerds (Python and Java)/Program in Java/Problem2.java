import java.util.Scanner;

/**
 * Problem1
 */
public class Problem2 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Number of Test Cases: ");
        int input = sc.nextInt();
        int cases[] = new int[input];

        for (int i = 0; i < input; i++) {
            System.out.printf("Enter number-%d: ",i+1);
            cases[i] = convertBase(sc.nextInt());
        }

        sc.close();

        for (int i = 0; i < cases.length; i++) {
            System.out.printf("Case#%d: %d\n", i+1, cases[i]);
        }

    }

    static int convertBase(int number) {
        int base = 0;
        int remainder;
        for (int i = 2; i <= number; i++) {
            int temp = number;
            while (true) {
                remainder = temp % i;
                if (remainder == 1) {
                    temp /= i;
                    if (temp == 0) {
                        base = i;
                        break;
                    }
                } else {
                    break;
                }
            }
            if (base == i) {
                break;
            }
        }
        return base;
    }
}