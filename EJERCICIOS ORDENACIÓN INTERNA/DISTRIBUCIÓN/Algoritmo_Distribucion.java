import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Algoritmo_Distribucion {
    public static void bucketSort(float[] arr, int numBuckets) {
        List<List<Float>> buckets = new ArrayList<>();
        for (int i = 0; i < numBuckets; i++) {
            buckets.add(new ArrayList<>());
        }

        // Colocar los elementos en las cubetas correspondientes
        for (float num : arr) {
            int bucketIndex = (int) (num * numBuckets);
            buckets.get(bucketIndex).add(num);
        }

        // Ordenar las cubetas individualmente utilizando otro algoritmo (en este caso, sort de la clase Collections)
        for (List<Float> bucket : buckets) {
            Collections.sort(bucket);
        }

        // Concatenar los elementos ordenados de las cubetas en el arreglo original
        int index = 0;
        for (List<Float> bucket : buckets) {
            for (float num : bucket) {
                arr[index++] = num;
            }
        }
    }

    public static void main(String[] args) {
        float[] arr = {0.42f, 0.32f, 0.33f, 0.52f, 0.37f, 0.47f, 0.51f};
        int numBuckets = 5;

        bucketSort(arr, numBuckets);

        System.out.print("Arreglo ordenado: ");
        for (float num : arr) {
            System.out.print(num + " ");
        }
    }
}
