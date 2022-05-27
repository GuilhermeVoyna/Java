import java.beans.VetoableChangeListener;
import java.util.Arrays;
import java.util.Vector;

public class App {
    public static void main(String[] args) throws Exception {
         
        System.out.println("---------------------------------------------------");
       int[] numbers = {0,5,444,3,33,1};
       System.out.println(Arrays.toString(numbers));

       var sorter = new InsertionSort();
       sorter.sort(numbers);
       System.out.println(Arrays.toString(numbers));


        System.out.println("\nfim do codigo\n---------------------------------------------------");
    }
}
