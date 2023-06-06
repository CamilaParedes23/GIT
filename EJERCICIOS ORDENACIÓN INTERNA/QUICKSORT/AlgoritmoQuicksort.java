public class AlgoritmoQuicksort {
    public static void AlgoritmoQuicksort(int[] arr, int low, int high) {
        if (low < high) {
            int pi = partition(arr, low, high);
            AlgoritmoQuicksort(arr, low, pi - 1);
            AlgoritmoQuicksort(arr, pi + 1, high);
        }
    }

    public static int partition(int[] arr, int low, int high) {
        int pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j < high; j++) {
            if (arr[j] < pivot) {
                i++;

                // Intercambia arr[i] y arr[j]
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        // Intercambia arr[i+1] y arr[high] (o el pivote)
        int temp = arr[i + 1];
        arr[i + 1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }

    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        int n = arr.length;

        AlgoritmoQuicksort(arr, 0, n - 1);

        System.out.println("Array ordenado:");
        for (int i = 0; i < n; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
