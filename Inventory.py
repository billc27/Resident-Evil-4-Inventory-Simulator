class Inventory:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[None for j in range(width)] for i in range(height)]

    def printInventory(self):
        for i in range(self.height):
            for j in range(self.width):
                print(self.matrix[i][j] or "XX", end=' ')
            print()

    def ffd(self, items_list):
        items_list.sort(key = lambda item: item.width * item.height, reverse = True)
        for item in items_list:
            placed = False
            for i in range(self.height):
                if placed:
                    break
                for j in range(self.width):
                    if self.fits(item, i, j):
                        self.place(item, i, j)
                        placed = True
                        break
                    elif self.fits(item.get_rotated_item(), i, j):
                        item.rotate_item()
                        self.place(item, i, j)
                        placed = True
                        break

    def bfd(self, items):
        for item in items:
            best_row, best_col, best_score = None, None, None
            for i in range(self.height):
                for j in range(self.width):
                    if self.fits(item, i, j):
                        score = self.get_score(item, i, j)
                        if best_score is None or score < best_score:
                            best_row, best_col, best_score = i, j, score
                    elif self.fits(item.get_rotated_item(), i, j):
                        score = self.get_score(item.get_rotated_item(), i, j)
                        if best_score is None or score < best_score:
                            best_row, best_col, best_score = i, j, score
                            item.rotate_item()
            if best_row is not None:
                self.place(item, best_row, best_col)

    def get_score(self, item, row, col):
        max_score = 0
        for i in range(row, min(row + item.height, self.height)):
            for j in range(col, min(col + item.width, self.width)):
                if self.matrix[i][j] is None: # Empty Place
                    max_score += 1
        return max_score

    def fits(self, item, row, col):
        for i in range(item.height):
            for j in range(item.width):
                if row + i >= self.height - 1 or col + j >= self.width - 1 or self.matrix[row + i][col + j] is not None:
                    return False
        return True

    def place(self, item, row, col):
        for i in range(item.height):
            for j in range(item.width):
                self.matrix[row + i][col + j] = item.id

    def add(self, item, row, col):
        if row + item.height > self.height or col + item.width > self.width:
            print("Not Enough Space!")
            return False
        
        for i in range(item.height):
            for j in range(item.width):
                if self.matrix[row + i][col + j] is not None:
                    print("Space Occupied!")
                    return False
                
        for i in range(item.height):
            for j in range(item.width):
                self.matrix[row + i][col + j] = item.id
        return True

    def clear(self):
        self.matrix = [[None for j in range(self.width)] for i in range(self.height)]
