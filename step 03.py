import pygame
import random
"""
STEP 03. 테트리스 블록 한 개 그리기 
"""
pygame.init()

WIDTH, HEIGHT = 600, 900
BLOCK_SIZE = 40 # Tetris block cell
ROWS, COLS = HEIGHT // BLOCK_SIZE, WIDTH // BLOCK_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("step03-테트리스 블록 하나 그리기")

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
x, y = 5, 5 # 5칸 X 5칸 위치에 그리기


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0)) # black
    
    # print(block) # 로직 이해를 위해 어떤 블록이 선택되었는지 print
    """
    2차원 게임 좌표계 구분
    x : 화면 가로 위치 (오른쪽 축)
    y : 화면 세로 위치 (아래쪽 축)
    j : 블록 가로 방향 (열, 오른쪽 축)
    i : 블록 세로 방향 (행, 아래쪽 축)
    """
    """
    [[1,1,1], 
     [0,1,0]] # T shape
     -> i = 0,1
     -> j = 0,1,2
     """
    for i in range(len(block)):
        for j in range(len(block[i])):
            if block[i][j]: # block 이 1 일 때(True) 블록 셀을 그림
                # j 는 가로 방향(col) -> x 에 더함, i 는 세로 방향(row) -> y 에 더함
                
                # block 의 좌표를 화면의 좌표로 변환 print
                screen_x  = (x+j) * BLOCK_SIZE
                screen_y = (y+i) * BLOCK_SIZE
                # print(f"block coord ({x+j}, {y+i}) -> screen coord ({screen_x}, {screen_y})")
                """
                예를 들어, 
                블록 위치 (x, y) = (5, 0)
                블록 모양:
                1 1 1
                0 1 0

                → 실제 보드 칸 위치
                (5, 0), (6, 0), (7, 0)
                        (6, 1)

                → 픽셀 위치:
                (200, 0), (240, 0), (280, 0)
                          (240, 40)
                """
                
                # draw block
                pygame.draw.rect(screen, color, (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE))
                # 회색 테두리
                pygame.draw.rect(screen, (100,100,100), (screen_x, screen_y, BLOCK_SIZE, BLOCK_SIZE),1)


    pygame.display.flip()


pygame.quit()