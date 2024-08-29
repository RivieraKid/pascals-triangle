row_num = int(input("Enter row number to calculate: "))


def get_row(desired_row_num):
    this_row_num = 1
    this_row = []
    prev_row = []
    while this_row_num <= desired_row_num:
        # Hardcode the first three rows since they're simple, but also ensuring that the previous row has at least three
        # items makes the algorithm in the for loop below a bit simpler
        if this_row_num == 1:
            prev_row = this_row
            this_row = [1]
        elif this_row_num == 2:
            prev_row = this_row
            this_row = [1, 1]
        elif this_row_num == 3:
            prev_row = this_row
            this_row = [1, 2, 1]
        else:
            prev_row = this_row
            this_row = []
            # 'i' represents the numbered position of the item from the previous row that we are processing
            for i in range(len(prev_row)):
                # First item in the new row is always 1
                if i == 0:
                    this_row.append(1)
                else:
                    # Calculate item number i for the current row
                    this_row.append(prev_row[i-1] + prev_row[i])
            # Final item is always 1
            this_row.append(1)
        # Calculate the next row
        this_row_num += 1
    return this_row


row = get_row(row_num)
print(row)
