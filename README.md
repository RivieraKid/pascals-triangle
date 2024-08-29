# Pascal's Triangle

This repo contains a simple implementation of Pascal's Triangle. You split a triangle up into individual rows, the first row having one item, the second row having two items, the third having three and so on. 

Each item contains the sum of the two items directly above it, if there is only one such item, then the new item is equal to that single item above it.

For example:

```
     1
    1 1
   1 2 1
  1 3 3 1
 1 4 6 4 1
```

# Execution

```
python ./triangle.py
Enter row number to calculate: 5
[1, 4, 6, 4, 1]
```

# Notes

- Error detection and handling is non-existent
- This implementation is fairly naïve, with the first three rows being hardcoded to simplify the algorithm later.