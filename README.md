# 🔢 Sorting Algorithms Collection

A collection of six classic sorting algorithms implemented from scratch in
Python — three simple comparison-based sorts, two divide-and-conquer sorts,
and one non-comparison-based sort.

## 📋 Overview

| Algorithm      | Function          | Approach                          | Time Complexity (avg) |
| --------------- | ------------------ | ----------------------------------- | ----------------------- |
| Bubble Sort     | `bubble()`         | Repeatedly swap adjacent out-of-order elements | O(n²)                   |
| Selection Sort  | `selection()`      | Repeatedly select the minimum remaining element | O(n²)                   |
| Insertion Sort  | `insertion()`      | Build the sorted array one element at a time | O(n²)                   |
| Quick Sort      | `quick_sort()` + `partition()` | Divide around a pivot, recurse on both halves | O(n log n)               |
| Merge Sort      | `merge_sort()` + `merge()`     | Split in half, sort each half, merge results | O(n log n)               |
| Radix Sort      | `radix_sort()` + `counting_sort()` | Sort digit by digit using counting sort | O(nk) (k = number of digits) |

## ▶️ Usage

```python
from mixsort import bubble, selection, insertion, quick_sort, merge_sort, radix_sort

arr = [64, 34, 25, 12, 22, 11, 90]

print(bubble(arr.copy()))
print(selection(arr.copy()))
print(insertion(arr.copy()))

quick_arr = arr.copy()
print(quick_sort(quick_arr, 0, len(quick_arr) - 1))

print(merge_sort(arr.copy()))
print(radix_sort(arr.copy()))
```

**Output (all verified):**

```
[11, 12, 22, 25, 34, 64, 90]
```

> ⚠️ **Note:** `quick_sort()` takes 3 arguments (`arr, low, high`) and sorts
> in place, unlike the others which just take `arr`. Call it like
> `quick_sort(arr, 0, len(arr) - 1)`.
>
> `radix_sort()` only works correctly on **non-negative integers**, since it
> sorts digit-by-digit.

## 🛠️ Tech Stack

- **Python 3** — no external dependencies

## 🚀 Possible Extensions

- Add a benchmarking script comparing runtime across algorithms for different input sizes
- Add unit tests (e.g. with `pytest`) covering edge cases: empty list, single element, already sorted, reverse sorted, duplicates
- Extend `radix_sort` to handle negative numbers
- Add Heap Sort for a complete classic-algorithms set
