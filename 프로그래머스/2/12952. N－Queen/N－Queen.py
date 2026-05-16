def solution(n):
    answer = 0

    def backtracking(row, col_list):
        nonlocal answer

        if row == n:
            answer += 1
            return

        for col in range(n):
            possible = True

            for prev_row in range(row):
                prev_col = col_list[prev_row]

                if prev_col == col:
                    possible = False
                    break

                if abs(prev_row - row) == abs(prev_col - col):
                    possible = False
                    break

            if possible:
                col_list.append(col)
                backtracking(row + 1, col_list)
                col_list.pop()

    backtracking(0, [])

    return answer