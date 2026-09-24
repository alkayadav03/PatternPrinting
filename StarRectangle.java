import java.util.Scanner;
public class StarRectangle{
    public static void main(String[] args) {
       Scanner sc = new Scanner(System.in);
       System.out.print("Enter number of rows: ");
        int row = sc.nextInt();
        System.out.print("Enter number of columns: ");
        int col = sc.nextInt();
        for(int i=0;i<=row;i++){ //outer loop for rows kitni lines hongi
            for(int j=0;j<=col;j++){ //inner loop for columns hr line me kitne star honge
                System.out.print(" * ");
            }
            System.out.println();
        }
}
}