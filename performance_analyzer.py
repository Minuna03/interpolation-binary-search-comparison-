"""
Performance Analyzer Module
Generates test data and analyzes performance of both algorithms
"""

import random
import math
from search_algorithms import SearchAlgorithms


class PerformanceAnalyzer:
    """Class to analyze and compare performance of search algorithms"""
    
    def __init__(self):
        """Initialize the analyzer"""
        self.results = []
        self.array_sizes = [1000, 5000, 10000, 50000, 100000]
    
    def generate_sorted_array(self, size):
        """
        Generate a sorted array of given size
        
        Args:
            size: Size of the array to generate
            
        Returns:
            list: Sorted array with unique elements
        """
        arr = sorted(random.sample(range(1, size * 10), size))
        return arr
    
    def analyze_single_size(self, array_size):
        """
        Analyze both algorithms for a single array size
        
        Args:
            array_size: Size of array to test
            
        Returns:
            dict: Results containing timing and comparison data
        """
        print(f"\nAnalyzing array size: {array_size}...", end=" ", flush=True)
        
        # Generate sorted array
        arr = self.generate_sorted_array(array_size)
        
        # Select a random key from the array for realistic search
        search_key = random.choice(arr)
        
        # Run Binary Search
        bs_found, bs_comparisons, bs_time = SearchAlgorithms.timed_binary_search(arr, search_key)
        
        # Run Interpolation Search
        is_found, is_comparisons, is_time = SearchAlgorithms.timed_interpolation_search(arr, search_key)
        
        # Calculate theoretical complexities
        bs_complexity = f"O(log n) = O(log {array_size}) ≈ {math.log2(array_size):.2f}"
        is_complexity = f"O(log log n) = O(log log {array_size}) ≈ {math.log2(math.log2(array_size)):.2f}"
        
        result = {
            'array_size': array_size,
            'search_key': search_key,
            'binary_search': {
                'found': bs_found,
                'comparisons': bs_comparisons,
                'execution_time': bs_time,
                'time_complexity': bs_complexity,
                'space_complexity': 'O(1)'
            },
            'interpolation_search': {
                'found': is_found,
                'comparisons': is_comparisons,
                'execution_time': is_time,
                'time_complexity': is_complexity,
                'space_complexity': 'O(1)'
            }
        }
        
        self.results.append(result)
        print("✓ Done")
        return result
    
    def run_full_analysis(self):
        """
        Run analysis for all array sizes
        
        Returns:
            list: All results
        """
        print("=" * 70)
        print("STARTING PERFORMANCE ANALYSIS")
        print("=" * 70)
        print(f"Array sizes to test: {self.array_sizes}")
        print("Running searches on randomly selected keys from each array...\n")
        
        for size in self.array_sizes:
            self.analyze_single_size(size)
        
        print("\n" + "=" * 70)
        print("ANALYSIS COMPLETE")
        print("=" * 70)
        
        return self.results
    
    def get_results(self):
        """Get stored results"""
        return self.results
    
    def print_detailed_results(self):
        """Print detailed results for each array size"""
        print("\n" + "=" * 100)
        print("DETAILED RESULTS")
        print("=" * 100 + "\n")
        
        for result in self.results:
            size = result['array_size']
            print(f"\nArray Size: {size} elements")
            print("-" * 100)
            
            bs = result['binary_search']
            is_result = result['interpolation_search']
            
            print(f"{'Metric':<30} {'Binary Search':<35} {'Interpolation Search':<35}")
            print("-" * 100)
            print(f"{'Comparisons':<30} {bs['comparisons']:<35} {is_result['comparisons']:<35}")
            print(f"{'Execution Time (ms)':<30} {bs['execution_time']:.6f}ms {'':<23} {is_result['execution_time']:.6f}ms")
            print(f"{'Time Complexity':<30} {bs['time_complexity']:<35} {is_result['time_complexity']:<35}")
            print(f"{'Space Complexity':<30} {bs['space_complexity']:<35} {is_result['space_complexity']:<35}")
            print(f"{'Element Found':<30} {str(bs['found']):<35} {str(is_result['found']):<35}")
            
            # Calculate performance difference
            if bs['execution_time'] > 0:
                ratio = is_result['execution_time'] / bs['execution_time']
                faster = "Interpolation" if ratio < 1 else "Binary"
                print(f"\n{'Performance Winner':<30} {faster:<35}")
                print(f"{'Speed Ratio (IS/BS)':<30} {ratio:.4f}x")
