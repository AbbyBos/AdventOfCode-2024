def solve():
    with open("c:\\Users\\Abby\\Documents\\Python\\AdventOfCode 2024\\Day 3\\Day 3 Prod.txt", 'r') as file:
        data = file.read()

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])  # Assuming all rows have the same length
    count = 0
    for r in range(rows):
        for c in range(cols):
             # ... (other checks) ...

            # Backwards (with complete bounds checks)
            if c - 4 >= 0 and grid[r][c-4:c+1] == "SAMX": # Corrected
                count += 1
            if r - 4 >= 0 and all(grid[r-i][c] == "SAMX"[i] for i in range(5) if 0<= r-i < rows and 0<=c<cols): # Corrected
                count += 1
            if r - 4 >= 0 and c + 4 < cols and all(grid[r-i][c+i] == "SAMX"[i] for i in range(5) if 0<= r-i < rows and 0<=c+i<cols): # Corrected
                count += 1
            if r - 4 >= 0 and c - 4 >= 0 and all(grid[r-i][c-i] == "SAMX"[i] for i in range(5) if 0<= r-i < rows and 0<=c-i<cols): # Corrected
                count += 1

    return count

    def count_x_mas(grid):
        rows = len(grid)
        cols = len(grid[0])
        count = 0

        for r in range(1, rows - 1): #Important change bounds checking at edges of the grid
            for c in range(1, cols - 1): #Important change bounds checking at edges of the grid
                # Check for X shape with MAS (Corrected bounds checks AND logic)
                if grid[r][c] == 'A' and (
                    (grid[r-1][c-1] == 'M' and grid[r+1][c-1] == 'S') or
                    (grid[r-1][c-1] == 'S' and grid[r+1][c-1] == 'M') or
                    (grid[r-1][c+1] == 'M' and grid[r+1][c+1] == 'S') or
                    (grid[r-1][c+1] == 'S' and grid[r+1][c+1] == 'M')
                ):
                    count += 1
        return count

    grid = data.splitlines()

    xmas_count = count_xmas(grid)
    x_mas_count = count_x_mas(grid)

    print("Part 1:", xmas_count)
    print("Part 2:", x_mas_count)

solve()
