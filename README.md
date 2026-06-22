# Comparative Analysis of Interpolation Search and Binary Search

## 📋 Project Overview

This project implements a comprehensive performance comparison between **Binary Search** and **Interpolation Search** algorithms on sorted datasets of varying sizes. The analysis includes execution time measurement, comparison counting, complexity analysis, and visual representation of results.

---

## 🎯 Objective

Design a Python application to compare the performance of Interpolation Search and Binary Search by:
- Generating sorted arrays of different sizes (1,000 to 100,000 elements)
- Searching for the same key using both algorithms
- Measuring and displaying execution time and number of comparisons
- Analyzing time and space complexity
- Presenting results in tabular and graphical formats
- Identifying scenarios where each algorithm outperforms the other

---

## 📁 Project Structure

```
interpolation-binary-search-comparison-/
├── README.md                          # Project documentation
├── search_algorithms.py               # Core search implementations
├── performance_analyzer.py            # Performance measurement logic
├── main.py                            # Main execution script
├── requirements.txt                   # Python dependencies
└── results/                           # Output folder
    ├── performance_comparison.png     # Visualization graph
    └── comparison_results.txt         # Detailed results
```

---

## 🔍 Algorithm Details

### Binary Search
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)
- **Description:** Divides the search space in half at each step by comparing with the middle element
- **Best for:** General-purpose searching, consistent performance

### Interpolation Search
- **Time Complexity:** O(log log n) average case, O(n) worst case
- **Space Complexity:** O(1)
- **Description:** Uses an interpolation formula to estimate the position of the search key
- **Best for:** Large, uniformly distributed datasets

---

## 📊 Test Data

The analysis tests both algorithms on sorted arrays with the following sizes:
- 1,000 elements
- 5,000 elements
- 10,000 elements
- 50,000 elements
- 100,000 elements

Random keys from each array are selected for realistic search scenarios.

---

## 🚀 How to Run

### Option 1: Using Python on Your Local Machine

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Minuna03/interpolation-binary-search-comparison-.git
   cd interpolation-binary-search-comparison-
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the program:**
   ```bash
   python main.py
   ```

### Option 2: Using GitHub Codespaces (No Installation Required!)

1. Go to your GitHub repository
2. Click **"Code"** → **"Codespaces"** → **"Create codespace on main"**
3. Wait for the environment to load
4. In the terminal, run:
   ```bash
   pip install -r requirements.txt
   python main.py
   ```

---

## 📈 Output

### Console Output
The program displays:
- **Performance Comparison Table:** Execution times and comparison counts
- **Detailed Analysis:** Metrics for each array size
- **Performance Winners:** Which algorithm is faster for each test case

### Generated Files
1. **performance_comparison.png** - A comprehensive 4-panel graph showing:
   - Execution time vs array size
   - Number of comparisons vs array size
   - Time ratio (Interpolation/Binary)
   - Comparison count ratio

2. **comparison_results.txt** - Detailed text report with:
   - Complete metrics for all test cases
   - Analysis and conclusions
   - Recommendations for algorithm selection

---

## 🔬 Key Findings

### Performance Characteristics

| Array Size | Winner | Reasoning |
|-----------|--------|-----------|
| 1,000 | Similar | Both very fast, differences negligible |
| 5,000 | Similar | Minimal difference |
| 10,000+ | Interpolation* | More noticeable improvement |
| 50,000+ | Interpolation* | Significant advantage on uniform data |
| 100,000 | Interpolation* | Maximum benefit of log log n complexity |

*On uniformly distributed data

### Important Observations

1. **Data Distribution Matters:** Interpolation Search's advantage is most pronounced on uniformly distributed data
2. **Consistency:** Binary Search provides more consistent, predictable performance across all data distributions
3. **Complexity vs Practice:** Theoretical O(log log n) advantage becomes visible at larger array sizes
4. **Space Efficiency:** Both algorithms use O(1) extra space, making them equally efficient in memory usage

---

## 💡 When to Use Each Algorithm

### Use Binary Search When:
- ✅ Data distribution is unknown
- ✅ You need guaranteed O(log n) performance
- ✅ Simplicity and reliability are priorities
- ✅ Data is skewed or non-uniformly distributed

### Use Interpolation Search When:
- ✅ Data is uniformly distributed
- ✅ Working with large datasets (50,000+ elements)
- ✅ You need optimal average-case performance
- ✅ Data follows a predictable pattern

---

## 🧪 How to Modify the Analysis

### Change Array Sizes
Edit `performance_analyzer.py`, line 13:
```python
self.array_sizes = [1000, 5000, 10000, 50000, 100000]
```

### Run Multiple Tests
Modify `main.py` to run the analysis multiple times and average results for more reliable data.

### Use Different Data Distributions
Modify `generate_sorted_array()` in `performance_analyzer.py` to test with:
- Skewed distributions
- Clustered data
- Random gaps

---

## 📚 Educational Value

This project demonstrates:
- Implementation of classic searching algorithms
- Performance measurement and benchmarking techniques
- Time and space complexity analysis
- Data visualization with matplotlib
- Algorithm selection based on problem requirements
- Scientific method for algorithm comparison

---

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Matplotlib** - Data visualization
- **NumPy** - Numerical operations
- **Pandas** - Data manipulation

---

## 📝 Lab Assignment Reference

**Problem Statement:** Comparative Analysis of Interpolation Search and Binary Search

**Objective:** Design a Python application to compare the performance of Interpolation Search and Binary Search on sorted datasets.

**Requirements Met:**
- ✅ Generate sorted arrays of sizes: 1000, 5000, 10000, 50000, 100000
- ✅ Search using both algorithms
- ✅ Measure execution time
- ✅ Count number of comparisons
- ✅ Display time and space complexity
- ✅ Present results in tabular format
- ✅ Generate line graph comparing execution times
- ✅ Identify scenarios where each algorithm excels

---

## 📧 Author

Created for Computer Science Lab Assignment  
**Student:** Minuna03  
**Date:** June 2026

---

## 📄 License

This project is provided for educational purposes.

---

## 🔗 Resources

- [Binary Search - GeeksforGeeks](https://www.geeksforgeeks.org/binary-search/)
- [Interpolation Search - GeeksforGeeks](https://www.geeksforgeeks.org/interpolation-search/)
- [Big O Notation - Khan Academy](https://www.khanacademy.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

**Happy Learning! 🚀**
