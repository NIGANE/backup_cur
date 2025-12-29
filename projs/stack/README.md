This project has been created as part of the 42 curriculum by amerkht

# Push_swap

## Description
The push_swap project is a sorting challenge that requires organizing a stack of integers using two stacks and a restricted instruction. The objective is to produce the shortest possible sequence of operations to achieve a fully sorted state in Stack A. This implementation utilizes a cost-efficient, which calculates the mathematical "price" of moving each node based on its current position relative to its target. By applying synchronized double rotations, the algorithm minimizes moves by performing shared actions on both stacks simultaneously. The process begins with a chunking strategy to organize data, followed by a meticulous search for the "cheapest" node to return to Stack A. This optimized approach ensures high-performance results, consistently meeting the rigorous move limits for both 100 and 500 member.

## Instructions
-- Compilation: Run make in the root directory to generate the push_swap executable
-- Execution: Provide a list of unique integers as arguments, e.g. -> ./push_swap 4 67 3 87 23.
-- Validation: Use ./push_swap $ARG | ./checker_OS $ARG to verify the sort and wc -l to count moves.

## Resources
https://youtu.be/KMLnRxG0Nc0?si=E7R9vYND8waIX1KK
- this link provides bref explaination of chunking alog, and how it works
- Through peer learning and collaboration within students, I had ideas about the Turk Algorithm, a strategy that achieves optimal efficiency by calculating the cheapest move cost for each node to reach its target position.

## Ai Usage
-- Algorithmic Deep-Dive: Used AI as a technical helper to explore the internal mechanics of chunking and cost-based algorithms, ensuring a deep understanding of their theoretical efficiency.
-- Testing & Validation: Leveraged AI to generate diverse number sets and identify complex edge cases, such as pre-sorted sequences and reverse-sorted inputs, to ensure robust sorting.