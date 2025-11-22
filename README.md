# Project Overview

This repository contains my submission for a two-part assignment focused on algorithm analysis and fundamental data structure implementations.

The project is divided into:

    Part I – Implementation and Analysis of Selection Algorithms
    Part II – Elementary Data Structures: Implementation and Discussion

Each part includes Python implementations along with performance and complexity analysis.

## Part I – : Implementation and Analysis of Selection Algorithms

  This section includes implementations of:
  
   - Deterministic Selection Algorithm (Median-of-Medians)
   - Randomized Selection Algorithm (QuickSelect)

  **Included files**
  
        Deterministic_Algorithm.py 
        Randomized_Algorithm.py
        Comparision_Deterministic_Randomized.py
        
  **Report**
  
          Part I  Implementation & Analysis of Selection Algorithms.pdf contains the following reports:
            Implementation for both algorithms
            Performance Analysis 
            Empirical Performance Analysis (runtime experiments)
            Space Complexity Discussion

**How to Run the Code:**

  Prerequisites
  
    Python 3.8 or above
    Visual Studio Code or any Python IDE
    matplotlib (install using pip install matplotlib)

 Copy and paste the code from the respective .py files into your IDE, save them, and run them to observe the results.
   
**Summary**

For practical median selection, QuickSelect is generally the preferred algorithm due to its strong average-case performance, making it efficient and easy to use in most real-world scenarios. However, in situations where strict worst-case performance guarantees are required, the Deterministic Median-of-Medians algorithm is more suitable. Although it may be slower in practice, it provides guaranteed linear-time behavior, making it valuable for applications that demand predictable and reliable performance.



## Part II –  Elementary Data Structures: Implementation and Discussion

  This section includes custom implementations of:
    Arrays
    Matrices
    Linked Lists
    Queues
    Stacks

  **Included files**
  
        Arrays.py 
        Matrices.py
        Stack.py
        Queue.py
        Linked_List.py
        Rooted_Trees.py
        
  **Report**
  
          PART II Elementary Data Structures Implementation and Discussion.pdf contains the following reports:
            Python implementations for each data structure with screenshot of outputs
            Performance Analysis (operations such as insert, delete, access, search, etc.) 
            Real-World Use Cases and Discussion of implementation relevance


**How to Run the Code:**

  Prerequisites
  
    Python 3.8 or above
    Visual Studio Code or any Python IDE

 Copy and paste the code from the respective .py files into your IDE, save them, and run them to observe the results.


**Summary**

 Part II focuses on implementing a range of fundamental data structures—including arrays, matrices, linked lists, stacks, queues, and rooted trees—to explore how each structure organizes and manages data. The section analyzes the time and space complexities of common operations such as insertion, deletion, searching, and traversal, highlighting how these complexities influence practical performance. Additionally, it provides a discussion on the trade-offs of choosing one data structure over another, such as the constant-time access of arrays versus the dynamic flexibility of linked lists, or the LIFO/FIFO behavior that makes stacks and queues ideal for specific workflows. Real-world examples illustrate how these structures are applied in systems such as memory management, scheduling, graph processing, and hierarchical data modeling. Together, these analyses help clarify when and why each data structure should be used in practical software development.

