import heapq  # 導入堆隊列算法以實現優先隊列

class Node:
    def __init__(self, position, g=0, h=0):
        self.position = position  # 當前節點的位置 (x, y)
        self.g = g  # 從起始節點到此節點的成本
        self.h = h  # 從此節點到目標的啟發式成本
        self.f = g + h  # 總成本 (g + h)

    def __lt__(self, other):
        return self.f < other.f  # 基於 f 成本進行優先隊列比較

def heuristic(a, b):
    # 計算切比雪夫距離以支持對角線移動
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def a_star(start, goal, grid):
    open_set = []  # 待探索的節點的優先隊列
    heapq.heappush(open_set, Node(start))  # 將起始節點添加到開放集合中
    came_from = {}  # 跟蹤路徑的字典

    g_score = {start: 0}  # 從起始節點到每個節點的成本
    f_score = {start: heuristic(start, goal)}  # 從起始節點到目標的估計總成本

    while open_set:  # 當還有節點可被探索時
        current = heapq.heappop(open_set)  # 獲取具有最低 f 分數的節點

        if current.position == goal:  # 檢查是否已到達目標
            return reconstruct_path(came_from, current.position)  # 重建路徑

        # 探索 8 種可能的移動方向（北、南、東、西、東北、西北、東南、西南）
        for dx, dy in [
            (-1, 0), (1, 0), (0, -1), (0, 1), 
            (-1, -1), (-1, 1), (1, -1), (1, 1)
        ]:  
            neighbor_pos = (current.position[0] + dx, current.position[1] + dy)  # 計算鄰居位置

            # 檢查鄰居是否在網格內且可走（0）
            if (0 <= neighbor_pos[0] < len(grid)) and (0 <= neighbor_pos[1] < len(grid[0])) and grid[neighbor_pos[1]][neighbor_pos[0]] == 0:
                # 計算到達鄰居節點的成本
                tentative_g_score = g_score[current.position] + (1.4 if abs(dx) + abs(dy) == 2 else 1)

                # 如果到達鄰居的路徑更好，則記錄該路徑
                if tentative_g_score < g_score.get(neighbor_pos, float('inf')):
                    came_from[neighbor_pos] = current.position  # 記錄最佳路徑
                    g_score[neighbor_pos] = tentative_g_score  # 更新 g 分數
                    f_score[neighbor_pos] = tentative_g_score + heuristic(neighbor_pos, goal)  # 更新 f 分數

                    # 如果鄰居尚未在開放集合中，則添加它
                    if neighbor_pos not in [n.position for n in open_set]:
                        heapq.heappush(open_set, Node(neighbor_pos, tentative_g_score, heuristic(neighbor_pos, goal)))
            else:
                print("blocked", neighbor_pos)

    return None  # 如果未找到路徑，則返回 None

def reconstruct_path(came_from, current):
    total_path = [current]  # 從當前節點開始
    while current in came_from:  # 反向追蹤路徑
        current = came_from[current]  # 移動到上一个節點
        total_path.append(current)  # 添加到路徑中
    return total_path[::-1]  # 返回從起始到目標的正確路徑


def spawn_graph(frame_class):
    #frame_class.board_masons
    #frame_class.board_walls
    #frame_class.board_structures
    graph = [[0 for column in range(frame_class.board_width)] for row in range(frame_class.board_height)]

    #structures block
    for row_index, row_data in enumerate(frame_class.board_structures):
        for column_index, column_data in enumerate(row_data):
            if column_data > 0:
                graph[row_index][column_index] = 1

    #wall
    for row_index, row_data in enumerate(frame_class.board_walls):
        for column_index, column_data in enumerate(row_data):
            if column_data > 0:
                graph[row_index][column_index] = 1

    #board_masons
    for row_index, row_data in enumerate(frame_class.board_masons):
        for column_index, column_data in enumerate(row_data):
            if column_data != 0:
                graph[row_index][column_index] = 1

    return graph