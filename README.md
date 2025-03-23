# Sorting Algorithm Performance Comparison

This project provides a Python script to compare the performance of four popular sorting algorithms: **Bubble Sort**, **Insertion Sort**, **Merge Sort**, and **Quick Sort**. The script measures the execution time of each algorithm for different array sizes and visualizes the results using `matplotlib`.

---

## Table of Contents
1. [Introduction](#introduction)
2. [Algorithms Implemented](#algorithms-implemented)
3. [How It Works](#how-it-works)
4. [Requirements](#requirements)
5. [Usage](#usage)
6. [Expected Insights](#Expected-Insights)
7. [License](#license)

---

## Introduction

Sorting algorithms are fundamental in computer science, and their performance can vary significantly depending on the size and nature of the input data. This project aims to compare the execution time of four sorting algorithms as the size of the input array increases. The results are visualized to help understand the time complexity of each algorithm in practice.

---

## Algorithms Implemented

1. **Bubble Sort**:
   - A simple comparison-based algorithm that repeatedly swaps adjacent elements if they are in the wrong order.
   - Optimized to stop early if no swaps are made during a pass.

2. **Insertion Sort**:
   - Builds the final sorted array one element at a time by inserting each element into its correct position.

3. **Merge Sort**:
   - A divide-and-conquer algorithm that recursively splits the array into halves, sorts them, and merges the sorted halves.

4. **Quick Sort**:
   - Another divide-and-conquer algorithm that selects a pivot element and partitions the array into elements less than, equal to, and greater than the pivot.

---

## How It Works

1. **Array Generation**:
   - Random arrays of integers are generated for sizes ranging from 100 to 1000 (in increments of 100).

2. **Time Measurement**:
   - The `measure_time` function measures the execution time of a given sorting algorithm on a copy of the array to avoid modifying the original data.

3. **Visualization**:
   - The `visualize_sorting_time` function plots the execution times of all four algorithms for each array size using `matplotlib`.

---

## Requirements

To run this project, you need the following Python libraries:

- `numpy`
- `matplotlib`

You can install these dependencies using `pip`:

```bash
pip install numpy matplotlib
````

## Usage

**Run the script:**

   ```bash
   python compare_sort_viz.py
   ```

**View the graph** showing the execution time of each sorting algorithm.

## Expected Insights
📌 **Bubble & Insertion Sort** → Slow for large datasets due to high time complexity.

📌 **Merge & Quick Sort** → Faster due to efficient divide-and-conquer techniques.

📌 **Quick Sort** may outperform **Merge Sort** in some cases.



## License
Feel free to customize or extend this project! 🚀

