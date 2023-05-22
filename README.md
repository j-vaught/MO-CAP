# MO-CAP
Material Optimization Computational Analysis Program (v2)

In the Fall term of 2022, my colleague Jacob Whisenant presented an intellectually challenging quandary related to a scientific project involving composite materials. His task was the construction of a frame, for which the optimal procurement strategy was a key concern. The target was to accomplish the task with the least volume of resources. 

While this might appear elementary initially, upon closer inspection it became evident that we were, in fact, confronting a problem that has been a subject of extensive academic discourse among mathematicians for many years. Our situation was identified as a variant of a well-known Combinatorial Optimization Problem, categorically akin to the renowned Traveling Salesman Problem.

In the context of Jacob's project, he had to choose among 10 possible parts available from the manufacturer, and was required to cut 37 pieces of different lengths. The complexity of computing every possible permutation manually made it clear that a more efficient technique was necessary.

After thoroughly examining the problem, I postulated a solution that would streamline the process. I made the assumption that a part could only be sectioned a maximum of two times. Although this led to an approximately 54-inch waste, there was potential for further improvement.

In the second version of the Material Optimization Computational Analysis Program (MO-CAP v2), I modified the cutting limit to three per manufactured piece, concurrently optimizing and modularizing the code for future ease of modification. This strategic change led to a significant reduction in the total waste, down to 27 inches.

The code is executed entirely in Python 3, following best programming practices for readability, reusability, and efficiency.

## Contact and Licensing

For further information, to report issues or to contribute to the development of MO-CAP, please feel free to contact me via jvaught@sc.edu. 

This project is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the condition that the copyright notice and this permission notice are included in all copies or substantial portions of the software.
