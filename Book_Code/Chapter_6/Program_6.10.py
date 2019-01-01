# Program 6.10: Write Python Program to Perform Queue Operations

matrix = [[10, 20],
          [30, 40],
          [50, 60]]

matrix_transpose = [[0, 0, 0],
                    [0, 0, 0]]


def main():
    for rows in range(len(matrix)):
        for columns in range(len(matrix[0])):
            matrix_transpose[columns][rows] = matrix[rows][columns]

    print("Transposed Matrix is")
    for items in matrix_transpose:
        print(items)


if __name__ == "__main__":
    main()

