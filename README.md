## Introduction 
This is a receation of tetris split into 13 steps. 
each step adds on new mechanisms to the game and step 13 is the final version
## How to play 
to play just simply press the arrow key to move the blocks and press the up key to rotate your blocks 
and finally press the spacebar to immediately drop the blocks 
## Goal 
the goal of this game is to have the highest score as possible and to do that
you need to clear as many rows as you can as placing blocks in rows.
every row you break will be a 100 points and every 500 points you can go on to the next level
How far can you go?
## picture 
<img width="772" alt="Screenshot 2025-05-10 at 5 25 44 PM" src="https://github.com/user-attachments/assets/a6edd9f0-81fd-4491-bf57-0ae75c7e9f9a" />    
    
![ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/cf190559-47be-4bbe-88ec-61737669b10a)


## Important mechanisms(Codes)

``` python
for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and not game_over: 
            if event.key == pygame.K_LEFT and not check_collision(block, x - 1, y): 
                x -= 1 
            elif event.key == pygame.K_RIGHT and not check_collision(block, x + 1, y):
                x += 1 
            elif event.key == pygame.K_DOWN and not check_collision(block, x, y + 1):
                y += 1
            elif event.key == pygame.K_UP: 
                rotated = rotate(block)
                if not check_collision(rotated, x, y):
                    block = rotated
            elif event.key == pygame.K_SPACE:
                y = drop_block(block,x,y)
                place_block(block,color,x,y)

                lines = clear_lines()

                if lines > 0:
                    score += 100 * lines
                    level = score // 500+1
                    fall_speed = max(100, 500 - (level - 1)*50)


                block, color = next_block, next_color
                next_block, next_color = random_block()
                x, y = COLS // 2 - len(block[0]) // 2,0
                  
                if check_game_over(block,x,y):
                    game_over = True
```
This code is the code that helps the blocks move side to side and even rotate and this code helps you contol the blocks the way you want it to move 

``` python
def check_collision(shape, x, y):
    # 블록이 1인 것들
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j]:
                new_x = x + j 
                new_y = y + i
                if new_x < 0 or new_x >= COLS or new_y >= ROWS:
                    return True
                if new_y >= 0 and board[new_y][new_x]: 
                    return True
```
This code is the code that helps the game to understand if there is a collision happening and this is important because without this the game would not notice if the blocks have been in a row and the game wouldnt work without it
