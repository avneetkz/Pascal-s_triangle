# Pascal-s_triangle
In the rows of a Pascal’s Triangle, each number is the sum of two numbers directly above it. 
The image below shows the structure of Pascal’s Triangle.

![image](https://user-images.githubusercontent.com/108647289/192099054-3bc07f50-76f8-4239-b009-6f92361d891e.png)

# Code explanation
In this you will get number of rows as the input. Prior to that import factorial library from math module. The main for loop is from the range 0 to number of rows followed by two more nesting for loops. First nested for loop is for left spacing and second nested for loop is for printing the elements of pascal's triangle. For printing the elements we use combination formula which is nCr means if you are given “n” number different items and you have to chose “r” number of items from it. The formula is 
### n!/ ((n-r)! * r!)
