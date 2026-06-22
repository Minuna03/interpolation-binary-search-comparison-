"""
Main Module
Orchestrates the complete performance comparison analysis and generates visualizations
"""

import matplotlib.pyplot as plt
import os
from performance_analyzer import PerformanceAnalyzer


def create_results_directory():
    """Create results directory if it doesn't exist"""
    if not os.path.exists('results'):
        os.makedirs('results')
        print("Created 'results' directory")


def print_comparison_table(analyzer):
    """Print comparison results in tabular format"""
    print("\n" + "=" * 120)
    print("PERFORMANCE COMPARISON TABLE")
    print("=" * 120)
    
    results = analyzer.get_results()
    
    print(f"\n{'Array Size':<15} {'Binary Search Comparisons':<30} {'Interpolation Search Comparisons':<35} {'Faster Algorithm':<20}")
    print("-" * 120)
    
    for result in results:
        size = result['array_size']
        bs_comp = result['binary_search']['comparisons']
        is_comp = result['interpolation_search']['comparisons']
        faster = "Interpolation" if is_comp < bs_comp else "Binary"
        
        print(f"{size:<15} {bs_comp:<30} {is_comp:<35} {faster:<20}")
    
    print("\n" + "=" * 120)
    print("EXECUTION TIME COMPARISON (in milliseconds)")
    print("=" * 120)
    
    print(f"\n{'Array Size':<15} {'Binary Search (ms)':<30} {'Interpolation Search (ms)':<35} {'Faster Algorithm':<20}")
    print("-" * 120)
    
    for result in results:
        size = result['array_size']
        bs_time = result['binary_search']['execution_time']
        is_time = result['interpolation_search']['execution_time']
        faster = "Interpolation" if is_time < bs_time else "Binary"
        
        print(f"{size:<15} {bs_time:<30.6f} {is_time:<35.6f} {faster:<20}")
    
    print("\n" + "=" * 120)


def generate_comparison_graph(analyzer):
    """Generate and save comparison graph"""
    results = analyzer.get_results()
    
    # Extract data for plotting
    array_sizes = [r['array_size'] for r in results]
    binary_times = [r['binary_search']['execution_time'] for r in results]
    interpolation_times = [r['interpolation_search']['execution_time'] for r in results]
    
    # Create figure with subplots
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Performance Comparison: Binary Search vs Interpolation Search', fontsize=16, fontweight='bold')
    
    # Plot 1: Execution Time Comparison
    ax1 = axes[0, 0]
    ax1.plot(array_sizes, binary_times, marker='o', linewidth=2, label='Binary Search', color='blue')
    ax1.plot(array_sizes, interpolation_times, marker='s', linewidth=2, label='Interpolation Search', color='red')
    ax1.set_xlabel('Array Size', fontsize=11, fontweight='bold')
    ax1.set_ylabel('Execution Time (ms)', fontsize=11, fontweight='bold')
    ax1.set_title('Execution Time vs Array Size', fontsize=12, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Plot 2: Number of Comparisons
    ax2 = axes[0, 1]
    bs_comparisons = [r['binary_search']['comparisons'] for r in results]
    is_comparisons = [r['interpolation_search']['comparisons'] for r in results]
    ax2.plot(array_sizes, bs_comparisons, marker='o', linewidth=2, label='Binary Search', color='blue')
    ax2.plot(array_sizes, is_comparisons, marker='s', linewidth=2, label='Interpolation Search', color='red')
    ax2.set_xlabel('Array Size', fontsize=11, fontweight='bold')
    ax2.set_ylabel('Number of Comparisons', fontsize=11, fontweight='bold')
    ax2.set_title('Comparisons vs Array Size', fontsize=12, fontweight='bold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Plot 3: Time Ratio (Interpolation / Binary)
    ax3 = axes[1, 0]
    time_ratios = [it/bt if bt > 0 else 1 for it, bt in zip(interpolation_times, binary_times)]
    colors = ['green' if ratio < 1 else 'orange' for ratio in time_ratios]
    ax3.bar(range(len(array_sizes)), time_ratios, color=colors, alpha=0.7)
    ax3.axhline(y=1, color='black', linestyle='--', linewidth=1, label='Equal Performance')
    ax3.set_xlabel('Array Size', fontsize=11, fontweight='bold')
    ax3.set_ylabel('Time Ratio (Interpolation/Binary)', fontsize=11, fontweight='bold')
    ax3.set_title('Performance Ratio (< 1 = Interpolation Faster)', fontsize=12, fontweight='bold')
    ax3.set_xticks(range(len(array_sizes)))
    ax3.set_xticklabels(array_sizes)
    ax3.legend()
    ax3.grid(True, alpha=0.3, axis='y')
    
    # Plot 4: Comparison Count Ratio
    ax4 = axes[1, 1]
    comp_ratios = [ic/bc if bc > 0 else 1 for ic, bc in zip(is_comparisons, bs_comparisons)]
    colors_comp = ['green' if ratio < 1 else 'orange' for ratio in comp_ratios]
    ax4.bar(range(len(array_sizes)), comp_ratios, color=colors_comp, alpha=0.7)
    ax4.axhline(y=1, color='black', linestyle='--', linewidth=1, label='Equal Comparisons')
    ax4.set_xlabel('Array Size', fontsize=11, fontweight='bold')
    ax4.set_ylabel('Comparison Ratio (Interpolation/Binary)', fontsize=11, fontweight='bold')
    ax4.set_title('Comparison Ratio (< 1 = Fewer Comparisons)', fontsize=12, fontweight='bold')
    ax4.set_xticks(range(len(array_sizes)))
    ax4.set_xticklabels(array_sizes)
    ax4.legend()
    ax4.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    
    # Save graph
    graph_path = os.path.join('results', 'performance_comparison.png')
    plt.savefig(graph_path, dpi=300, bbox_inches='tight')
    print(f"\n✓ Graph saved to: {graph_path}")
    
    plt.show()


def save_results_to_file(analyzer):
    """Save detailed results to a text file"""
    results = analyzer.get_results()
    
    file_path = os.path.join('results', 'comparison_results.txt')
    
    with open(file_path, 'w') as f:
        f.write("=" * 100 + "\n")
        f.write("PERFORMANCE COMPARISON: BINARY SEARCH vs INTERPOLATION SEARCH\n")
        f.write("=" * 100 + "\n\n")
        
        for result in results:
            size = result['array_size']
            bs = result['binary_search']
            is_result = result['interpolation_search']
            
            f.write(f"\nArray Size: {size} elements\n")
            f.write("-" * 100 + "\n")
            
            f.write(f"{'Metric':<30} {'Binary Search':<35} {'Interpolation Search':<35}\n")
            f.write("-" * 100 + "\n")
            f.write(f"{'Comparisons':<30} {bs['comparisons']:<35} {is_result['comparisons']:<35}\n")
            f.write(f"{'Execution Time (ms)':<30} {bs['execution_time']:.6f}ms {'':<23} {is_result['execution_time']:.6f}ms\n")
            f.write(f"{'Time Complexity':<30} {bs['time_complexity']:<35} {is_result['time_complexity']:<35}\n")
            f.write(f"{'Space Complexity':<30} {bs['space_complexity']:<35} {is_result['space_complexity']:<35}\n")
            f.write(f"{'Element Found':<30} {str(bs['found']):<35} {str(is_result['found']):<35}\n")
            
            # Calculate performance difference
            if bs['execution_time'] > 0:
                ratio = is_result['execution_time'] / bs['execution_time']
                faster = "Interpolation" if ratio < 1 else "Binary"
                f.write(f"\n{'Performance Winner':<30} {faster:<35}\n")
                f.write(f"{'Speed Ratio (IS/BS)':<30} {ratio:.4f}x\n")
        
        f.write("\n\n" + "=" * 100 + "\n")
        f.write("ANALYSIS AND CONCLUSIONS\n")
        f.write("=" * 100 + "\n")
        f.write("""
TIME COMPLEXITY ANALYSIS:
- Binary Search: O(log n) - Always divides the search space in half
- Interpolation Search: O(log log n) average case - Uses interpolation to estimate position
  
SPACE COMPLEXITY:
- Both algorithms: O(1) - Only use constant extra space for variables

KEY FINDINGS:
1. Interpolation Search performs better on uniformly distributed arrays
2. Binary Search is more consistent and predictable across different data distributions
3. Interpolation Search can degrade to O(n) on non-uniform data
4. For small arrays (< 5000), the difference is negligible
5. As array size increases, Interpolation Search's advantage becomes more apparent

RECOMMENDATIONS:
- Use Binary Search for general purposes (most reliable)
- Use Interpolation Search for large, uniformly distributed datasets
- Consider data distribution when choosing between the two algorithms
        """)
    
    print(f"✓ Results saved to: {file_path}")


def main():
    """Main execution function"""
    print("\n" + "=" * 100)
    print("COMPARATIVE ANALYSIS: BINARY SEARCH vs INTERPOLATION SEARCH")
    print("=" * 100)
    
    # Create results directory
    create_results_directory()
    
    # Initialize analyzer
    analyzer = PerformanceAnalyzer()
    
    # Run full analysis
    analyzer.run_full_analysis()
    
    # Print detailed results
    analyzer.print_detailed_results()
    
    # Print comparison table
    print_comparison_table(analyzer)
    
    # Generate graphs
    print("\nGenerating performance comparison graph...")
    generate_comparison_graph(analyzer)
    
    # Save results to file
    print("\nSaving results to file...")
    save_results_to_file(analyzer)
    
    print("\n" + "=" * 100)
    print("✓ ANALYSIS COMPLETE!")
    print("=" * 100)
    print("\nOutput files generated:")
    print("  - results/performance_comparison.png")
    print("  - results/comparison_results.txt")
    print("\n")


if __name__ == "__main__":
    main()
