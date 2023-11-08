# Adjacency Matrix representation in Python


class Graph(object):

    # Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        self.size = size

    # Add edges
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adjMatrix[v1][v2] = 1
        self.adjMatrix[v2][v1] = 1

    # Remove edges
    def remove_edge(self, v1, v2):
        if self.adjMatrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adjMatrix[v1][v2] = 0
        self.adjMatrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print the matrix
    def print_matrix(self):
        for row in self.adjMatrix:
            print(row)

    def depthFirstSearch(self):
        visited = [False] * self.size
        self.dfs(0, visited)
    def dfs(self, start, visited):
        visited[start] = True
        print(start)
        for i in range(self.size):
            if self.adjMatrix[start][i] == 1 and visited[i] == False:
                self.dfs(i, visited)
    def depthFirstSearchStack(self):
        visited = [False] * self.size
        stack = []
        stack.append(0)
        visited[0] = True
        while len(stack) > 0:
            current = stack.pop()
            print(current)
            for i in range(self.size):
                if self.adjMatrix[current][i] == 1 and visited[i] == False:
                    stack.append(i)
                    visited[i] = True
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(i, j, k):
            if not (0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] == word[k]):
                return False

            if k == len(word) - 1:
                return True

            original_char = board[i][j]
            board[i][j] = "#"  # Mark the cell as visited

            # Explore in all four directions
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))

            board[i][j] = original_char  # Unmark the cell

            return found

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

# Example usage
sol = Solution()
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]
word = "ABCCED"
print(sol.exist(board, word))  # Output will be True

        
        





g = Graph(5)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_matrix()

g.depthFirstSearch()
