import pygame
import random
"""
STEP 06.블록 회전
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
BLOCK_SIZE = 40 # Tetris block cell
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step05-블록 회전")

# color of tetris block 
COLORS = [(0,255,255), (0,0,255), (255,165,0),
          (255,255,0), (0,255,0), (128,0,128), (255,0,0)
          ]

# shape of Tetris block
BLOCKS = [
    [[1,1,1,1]], # I shape
    [[1,1],
     [1,1]], # O square  
    [[1,1,1], 
     [0,1,0]] # T shape
]

block = random.choice(BLOCKS)
color = random.choice(COLORS)
x, y = 5, 0 # 처음 블록 위치

# 시간 추적용 변수
drop_time = pygame.time.get_ticks()

# 블록 회전함수 추가
def rotate(shape):
    rows = len(shape)
    cols = len(shape[0])
    rotated = []
    for j in range(cols):
        new_row = []
        for i in range(rows -1, -1, -1):
            new_row.append(shape[i][j])
        rotated.append(new_row)
    return rotated 

"""
rotate - clock 90 ->
[[1,1,1],
[0,1,0]]

[
  [0,1],
  [1,1],
  [0,1]
]
"""
def rotate_zip(shape):
    return [list(row for now in zip(*shape[::-1]))]

"""
# list comprehesion 
[list(row) for row in zip(*shape[::-1])]
# ->
empty_lst = []
for row in zip(*shape[::-1]):
    empty_lst.append(list(row))
"""
running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0,0,0)) # 화면 검은색으로 덮고 다시 화면 보여주기 위해서
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # 방향키로 블록 이동
        elif event.type == pygame.KEYDOWN: # 키가 눌리는 이벤트 발생
            if event.key == pygame.K_LEFT: # 눌린 키가 왼쪽 화살표키이면
                x -= 1 # 왼쪽 이동
            elif event.key == pygame.K_RIGHT:
                x += 1 # 오른쪽 이동
            elif event.key == pygame.K_DOWN:
                y += 1
            elif event.key == pygame.K_UP: #회전
                block = rotate(block)
                
    # 0.5초마다 블록이 한 칸씩 내려옴
    if pygame.time.get_ticks() - drop_time > 500:
        y += 1
        drop_time = pygame.time.get_ticks()
        
    # 블록 그리기
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j]: 
                screen_x  = (x+j) * BLOCK_SIZE
                screen_y = (y+i) * BLOCK_SIZE
                
                pygame.draw.rect(screen, color, (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, (100,100,100), (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE),1)

    pygame.display.flip()
    # 초당 최대 30프레임 (30FPS) 제한
    clock.tick(30) # 1초에 최대 30번만 루프가 실행되게 만듦.

pygame.quit()