import java.util.Currency;

public class InsertionSort {

    void sort(int[] array){

        for(var i=1;i<array.length;i++){
            var atual=array[i]; //atual (5)
            var j=i-1;
            while(j>-1&&atual<array[j]){
                array[j+1]=array[j];
                j--;
            }
            array[j+1]=atual;
        }


        }

}
