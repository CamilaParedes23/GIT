#include <iostream>
#include <vector>
#include <algorithm>

void bucketSort(std::vector<float>& arr, int numBuckets) {
    std::vector<std::vector<float>> buckets(numBuckets);

    // Colocar los elementos en las cubetas correspondientes
    for (float num : arr) {
        int bucketIndex = num * numBuckets;
        buckets[bucketIndex].push_back(num);
    }

    // Ordenar las cubetas individualmente utilizando otro algoritmo (en este caso, sort de la STL)
    for (auto& bucket : buckets) {
        std::sort(bucket.begin(), bucket.end());
    }

    // Concatenar los elementos ordenados de las cubetas en el arreglo original
    int index = 0;
    for (auto& bucket : buckets) {
        for (float num : bucket) {
            arr[index++] = num;
        }
    }
}

int main() {
    std::vector<float> arr = {0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51};
    int numBuckets = 5;

    bucketSort(arr, numBuckets);

    std::cout << "Arreglo ordenado: ";
    for (float num : arr) {
        std::cout << num << " ";
    }

    return 0;
}
