import random

# 初始化游戏界面
width = 10
height = 20
screen = [[0] * width for _ in range(height)]

# 定义方块种类和变化形态
blocks = [
    [[1, 1, 1, 1]],  # I
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1], [1, 1]],  # O
    [[1, 0, 0], [1, 1, 1]],  # L
    [[0, 0, 1], [1, 1, 1]]  # J
]

# 初始化当前方块
current_block = random.choice(blocks)
x, y = width // 2 - len(current_block[0]) // 2, 0

# 标记游戏是否结束
game_over = False

# 移动方块
def move(dx):
    global x
    x += dx
    if check_collision():
        x -= dx

# 旋转方块
def rotate():
    global current_block
    current_block = [[current_block[j][i] for j in range(len(current_block))] for i in range(len(current_block[0]))]
    if check_collision():
        current_block = [[current_block[j][i] for j in range(len(current_block))] for i in range(len(current_block[0]))]

# 检查方块是否和游戏界面碰撞
def check_collision():
    for i in range(len(current_block[0])):
        for j in range(len(current_block)):
            if current_block[j][i] and (x + i < 0 or x + i >= width or y + j >= height or screen[y + j][x + i]):
                return True
    return False

# 更新游戏界面
def update_screen():
    for i in range(height):
        for j in range(width):
            if screen[i][j]:
                print('@', end='')
            elif i >= y and j >= x and i - y < len(current_block) and j - x < len(current_block[0]) and current_block[i - y][j - x]:
                print('*', end='')
            else:
                print(' ', end='')
        print()

# 消除整行方块
def clear_lines():
    global screen
    new_screen = []
    clear = 0
    for i in range(height):
        if sum(screen[height - 1 - i]) == 0:
            break
        if sum(screen[height - 1 - i]) == width:
            clear += 1
        else:
            new_screen.insert(0, screen[height - 1 - i])
    screen = [[0] * width for _ in range(height - clear)] + new_screen

# 主循环
while not game_over:
    command = input()

    # 移动方块
    if command == 'a':
        move(-1)
    elif command == 'd':
        move(1)
    elif command == 'w':
        rotate()
    elif command == 's':
        y += 1
        if check_collision():
            y -= 1

    # 更新游戏界面
    screen = [[0] * width for _ in range(height)]
    for i in range(len(current_block)):
        for j in range(len(current_block[0])):
            if current_block[i][j]:
                screen[y + i][x + j] = 1
    update_screen()

    # 消除整行方块
    clear_lines()

    # 随机生成新的方块
    if y == 0:
        current_block = random.choice(blocks)
        x, y = width // 2 - len(current_block[0]) // 2, 0
        if check_collision():
            game_over = True

print('Game Over!')