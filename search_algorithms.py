"""
Search Algorithms Module
Implements Binary Search and Interpolation Search with comparison counting
"""

import time


class SearchAlgorithms:
    """Class containing both search algorithms with performance tracking"""
    
    @staticmethod
    def binary_search(arr, key):
        """
        Binary Search Algorithm
        Time Complexity: O(log n)
        Space Complexity: O(1)
        
        Args:
            arr: Sorted array to search in
            key: Element to search for
            
        Returns:
            tuple: (found: bool, comparisons: int, index: int or -1)
        """
        left = 0
        right = len(arr) - 1
        comparisons = 0
        
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            
            if arr[mid] == key:
                return True, comparisons, mid
            elif arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        
        return False, comparisons, -1
    
    @staticmethod
    def interpolation_search(arr, key):
        """
        Interpolation Search Algorithm
        Time Complexity: O(log log n) average case, O(n) worst case
        Space Complexity: O(1)
        
        Args:
            arr: Sorted array to search in
            key: Element to search for
            
        Returns:
            tuple: (found: bool, comparisons: int, index: int or -1)
        """
        left = 0
        right = len(arr) - 1
        comparisons = 0
        
        while left <= right and key >= arr[left] and key <= arr[right]:
            comparisons += 1
            
            # Avoid division by zero
            if arr[right] == arr[left]:
                if arr[left] == key:
                    return True, comparisons, left
                return False, comparisons, -1
            
            # Interpolation formula
            pos = left + int((key - arr[left]) / (arr[right] - arr[left]) * (right - left))
            
            # Boundary check
            if pos < left:
                pos = left
            elif pos > right:
                pos = right
            
            if arr[pos] == key:
                return True, comparisons, pos
            elif arr[pos] < key:
                left = pos + 1
            else:
                right = pos - 1
        
        return False, comparisons, -1
    
    @staticmethod
    def timed_binary_search(arr, key):
        """
        Binary Search with execution time measurement
        
        Returns:
            tuple: (found: bool, comparisons: int, execution_time: float)
        """
        start_time = time.time()
        found, comparisons, _ = SearchAlgorithms.binary_search(arr, key)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        return found, comparisons, execution_time
    
    @staticmethod
    def timed_interpolation_search(arr, key):
        """
        Interpolation Search with execution time measurement
        
        Returns:
            tuple: (found: bool, comparisons: int, execution_time: float)
        """
        start_time = time.time()
        found, comparisons, _ = SearchAlgorithms.interpolation_search(arr, key)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        return found, comparisons, execution_time
