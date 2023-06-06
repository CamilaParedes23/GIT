def bucketSort(arr, num_buckets):
    buckets = [[] for _ in range(num_buckets)]

    # Colocar los elementos en las cubetas correspondientes
    for num in arr:
        bucket_index = int(num * num_buckets)
        buckets[bucket_index].append(num)

    # Ordenar las cubetas individualmente utilizando otro algoritmo (en este caso, sorted de Python)
    for i in range(num_buckets):
        buckets[i] = sorted(buckets[i])

    # Concatenar los elementos ordenados de las cubetas en el arreglo original
    index = 0
    for bucket in buckets:
        for num in bucket:
            arr[index] = num
            index += 1

arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
num_buckets = 5

bucketSort(arr, num_buckets)

print("Arreglo ordenado:", arr)
