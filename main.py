import pygame
import shapes
import piece
import grid
import random
import score
import button

def draw_frame(screen, board_width, board_height, line_thickness):
    pygame.draw.rect(screen, [0,0,0], [0, 0, board_width + 2 * line_thickness, board_height], line_thickness)

def game_loop(screen, grid_, current_piece, score_, board_width, board_height, line_thickness, screen_width, screen_height):
    clock = pygame.time.Clock()
    FPS = 60
    speed = 3000
    move_speed = 2
    rotation_speed = 10
    rotation_counter = 0
    move_counter = 0
    running = True
    falling = clock.tick(FPS)
    clicked = False

    background_image = pygame.image.load("resources/background.png")

    start_button_image = pygame.image.load("resources/blue_button.png")
    start_button_width, start_button_height = start_button_image.get_size()

    creator_button_image = pygame.image.load("resources/pink_button.png")
    creator_button_width, kreator_button_height = creator_button_image.get_size()

    options_button_image = pygame.image.load("resources/yellow_button.png")
    options_button_width, options_button_height = options_button_image.get_size()

    about_button_image = pygame.image.load("resources/green_button.png")
    about_button_width, about_button_height = about_button_image.get_size()

    quit_button_image = pygame.image.load("resources/purple_button.png")
    quit_button_width, quit_button_height = quit_button_image.get_size()

    gap = 80

    # Game Loop
    while running:
        key = pygame.key.get_pressed()
        screen.fill((192, 192, 192))
        falling += clock.tick(FPS)
        rotation_counter += 1
        move_counter += 1
        is_down = False

        # ESC OR GAME OVER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        start_button = button.Button("START", (
            screen_width / 2 - start_button_width / 2, screen_height / 2 - start_button_height / 2 - gap), "arial",
                                     (0, 0, 0), 23, start_button_image, 1, screen)
        creator_button = button.Button("SHAPE CREATOR", (
            screen_width / 2 - creator_button_width / 2, screen_height / 2 - kreator_button_height / 2), "arial",
                                       (0, 0, 0), 23, creator_button_image, 1, screen)
        options_button = button.Button("OPTIONS", (
            screen_width / 2 - options_button_width / 2, screen_height / 2 - options_button_height / 2 + gap), "arial",
                                       (0, 0, 0), 23, options_button_image, 1, screen)
        about_button = button.Button("ABOUT", (
            screen_width / 2 - about_button_width / 2, screen_height / 2 - about_button_height / 2 + 2 * gap), "arial",
                                    (0, 0, 0), 23, about_button_image, 1, screen)
        quit_button = button.Button("QUIT", (
            screen_width / 2 - quit_button_width / 2, screen_height / 2 - quit_button_height / 2 + 3 * gap), "arial",
                                       (0, 0, 0), 23, quit_button_image, 1, screen)

        if start_button.click_check() is False and clicked is not True:
            tetris_title = pygame.image.load("resources/Tetris.png")
            tetris_title = pygame.transform.scale(tetris_title, (screen_width - 200, 131))
            screen.fill((192, 192, 192))
            screen.blit(tetris_title, (screen_width / 2 - ((screen_width - 200) / 2), 100))
            screen.blit(background_image, (0, 0))
            start_button.create_button()
            creator_button.create_button()
            options_button.create_button()
            about_button.create_button()
            quit_button.create_button()

            if creator_button.click_check() is True:
                print("SHAPE CREATOR")
            if options_button.click_check() is True:
                print("OPTIONS")
            if about_button.click_check() is True:
                print("ABOUT")
            if quit_button.click_check() is True:
                running = False
        else:
            clicked = True
            screen.fill((192, 192, 192))  # change background color
            grid_.draw_grid() # draw grid
            grid_.draw_small_grid()
            draw_frame(screen, board_width, board_height, line_thickness) # draw frame
            current_piece.draw_shape() # draw first shape
            current_piece.draw_next_shape()
            score_.display_score() # display game score
            shapes.display_next(screen, board_width) # display "next"

            # check stop condition
            if current_piece.stop is False:
                running = False

            c_right = current_piece.check_right()
            c_left = current_piece.check_left()
            c_bottom = current_piece.check_bottom()

            # check if there is any full or empty line
            current_piece.check_full_line()
            current_piece.fix_empty_lines()

            # KEYBOARD
            if key[pygame.K_UP] or key[pygame.K_w]:
                if rotation_counter > rotation_speed and current_piece.check_rotation() is True:
                    current_piece.rotation += 1
                    rotation_counter = 0

            if key[pygame.K_DOWN] or key[pygame.K_s]:
                is_down = True
                if move_counter > move_speed and c_bottom is True:
                    current_piece.row += 1
                    move_counter = 0
            elif key[pygame.K_RIGHT] or key[pygame.K_d]:
                if move_counter > move_speed and c_right is True:
                    current_piece.column += 1
                    move_counter = 0
            elif key[pygame.K_LEFT] or key[pygame.K_a]:
                if move_counter > move_speed and c_left is True:
                    current_piece.column -= 1
                    move_counter = 0

            if falling / speed > 0.1 and is_down is False:
                current_piece.row += 1
                # print(current_piece.column, current_piece.row)
                # print(current_piece.check_left(), current_piece.check_right())
                falling = 0


        pygame.display.update()
        clock.tick(FPS)

def init_game():
    pygame.init()
    screen_height = 810
    screen_width = 750
    board_height = 810
    board_width = 520
    block_side = 40
    columns = 13
    rows = 20
    line_thickness = 5

    # Create the screen
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.SRCALPHA)
    # Title and icon
    pygame.display.set_caption("TETRIS")
    icon = pygame.image.load("resources/TetrisIcon.png")
    pygame.display.set_icon(icon)

    grid_ = grid.Grid(columns, rows, screen, line_thickness, block_side, board_width)
    score_ = score.Score(0, screen, board_height, board_width)
    current_piece = piece.Piece(4, 0, random.choice(shapes.shapes), screen, block_side, line_thickness,
                                shapes.shape_colors[random.randint(0, len(shapes.shape_colors) - 1)], grid_, columns,
                                rows, score_, screen_width, screen_height, board_width, board_height)

    if current_piece.shape == shapes.S2:
        current_piece.column += 1

    grid_.list_for_grid()

    game_loop(screen, grid_, current_piece, score_, board_width, board_height, line_thickness, screen_width, screen_height)

    pygame.quit()

init_game()

