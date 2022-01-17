import pygame
import shapes
import piece
import grid
import random
import score
import button
import checkbox
import new_shape

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
    start_clicked = False
    creator_clicked = False
    options_clicked = False
    about_clicked = False
    clear_clicked = False
    save_clicked = False
    boxes = []
    is_visible = [True, True, True, True]
    new_shapes_count = 0

    background_image = pygame.image.load("resources/background.png")

    start_button_image = pygame.image.load("resources/blue_button.png")
    button_width, button_height = start_button_image.get_size()

    creator_button_image = pygame.image.load("resources/pink_button.png")

    options_button_image = pygame.image.load("resources/yellow_button.png")

    about_button_image = pygame.image.load("resources/green_button.png")

    quit_button_image = pygame.image.load("resources/purple_button.png")

    clear_button_image = pygame.image.load("resources/yellow_button.png")

    save_button_image = pygame.image.load("resources/green_button.png")

    back_button_image = pygame.image.load("resources/purple_button.png")

    gap = 80

    # radio buttons - do poprawy
    for i in range(len(shapes.shape_colors)):
        r_button = checkbox.Checkbox(screen, 550, 190 + (i * 50), (255, 255, 255), "color", (0, 0, 0), shapes.shape_colors[i], 20, shapes.shape_colors[i], 570,
                                 190 + (i * 50), "arial", shapes.shape_colors[i])
        boxes.append(r_button)

    start_button = button.Button("START", (
        screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 - gap), "arial",
                                 (0, 0, 0), 23, start_button_image, 1, screen)
    creator_button = button.Button("SHAPE CREATOR", (
        screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2), "arial",
                                   (0, 0, 0), 23, creator_button_image, 1, screen)
    options_button = button.Button("OPTIONS", (
        screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + gap), "arial",
                                   (0, 0, 0), 23, options_button_image, 1, screen)
    about_button = button.Button("ABOUT", (
        screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 2 * gap), "arial",
                                 (0, 0, 0), 23, about_button_image, 1, screen)
    quit_button = button.Button("QUIT", (
        screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 3 * gap), "arial",
                                (0, 0, 0), 23, quit_button_image, 1, screen)
    clear_button = button.Button("CLEAR", (65, 380), "arial",(0, 0, 0), 23, clear_button_image, 0.7, screen)

    save_button = button.Button("SAVE", (0.7 * button_width + 75, 380), "arial", (0, 0, 0), 23, save_button_image, 0.7, screen)

    back_button = button.Button("BACK", (65, 710), "arial", (0, 0, 0), 23, back_button_image, 0.7, screen)

    start2_button = button.Button("START", (75 + 0.7 * button_width, 710), "arial", (0, 0, 0), 23, start_button_image, 0.7, screen)

    # Game Loop
    while running:
        key = pygame.key.get_pressed()
        screen.fill((192, 192, 192))
        falling += clock.tick(FPS)
        rotation_counter += 1
        move_counter += 1
        is_down = False
        selected_color = 0

        # ESC OR GAME OVER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        if key[pygame.K_SPACE]: # chwilowo
            start_clicked = True

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

        if start_button.click_check() is True and is_visible[0] is True:
            start_clicked = True
        elif creator_button.click_check() is True and is_visible[1] is True:
            creator_clicked = True
        elif options_button.click_check() is True and is_visible[2] is True:
            options_clicked = True
        elif about_button.click_check() is True and is_visible[3] is True:
            about_clicked = True
        elif quit_button.click_check() is True:
            running = False


        if start_clicked is False and creator_clicked is True and options_clicked is False and about_clicked is False: # SHAPE CREATOR
            is_visible[0] = False
            is_visible[2] = False
            is_visible[3] = False
            screen.fill((192, 192, 192))
            # draw - "MAKE YOUR OWN SHAPES"
            font = pygame.font.SysFont('arial', 60)
            w2, h2 = font.size("MAKE YOUR OWN SHAPES")
            w, h = font.size("MAKE")
            width = w
            creator_text = font.render("MAKE", True, (30,144,255))
            screen.blit(creator_text, (screen_width / 2 - w2 / 2, 0))
            w, h = font.size(" YOUR")
            creator_text = font.render(" YOUR", True, (255,20,147))
            screen.blit(creator_text, (screen_width / 2 - w2 / 2 + width, 0))
            width += w
            w, h = font.size(" OWN")
            creator_text = font.render(" OWN", True, (50,205,50))
            screen.blit(creator_text, (screen_width / 2 - w2 / 2 + width, 0))
            width += w
            creator_text = font.render(" SHAPES", True, (255,140,0))
            screen.blit(creator_text, (screen_width / 2 - w2 / 2 + width, 0))
            # draw - "COLOR"
            font = pygame.font.SysFont('arial', 30)
            color_text = font.render("COLOR", True, (0, 0, 0))
            screen.blit(color_text, (535, 130))
            #draw - "SELECT SQUARES"
            shape_text = font.render("SELECT SQUARES", True, (0, 0, 0))
            screen.blit(shape_text, (90, 130))
            # radio buttons -> colors
            for box in boxes:
                box.render_checkbox()

            # update checkboxes and check if only one is selected
            if pygame.mouse.get_pressed()[0] == 1:
                for i in range(len(boxes)):
                    boxes[i].update_checkbox()
                    if boxes[i].checked is True:
                        selected_color = boxes[i].check_color
                        for j in range(i):
                            boxes[j].checked = False

            # draw creator grid
            grid_.draw_creator_grid(selected_color)
            # add clear button
            clear_button.create_button()
            if clear_button.click_check() is True:
                grid_.clear_creator_grid(boxes)
            # add save button
            save_button.create_button()
            if save_button.click_check() is True and start_clicked is False:
                new = new_shape.NewShape(grid_)
                empty = new.save_shape(grid_, new_shapes_count)
                # draw - "SAVED"
                if empty is False:
                    new_shapes_count += 1
                    font = pygame.font.SysFont('arial', 30)
                    color_text = font.render("SAVED", True, (0, 0, 0))
                    screen.blit(color_text, (150, 500))
            # add back button
            back_button.create_button()
            if back_button.click_check() is True:
                start_clicked = False
                creator_clicked = False
                options_clicked = False
                about_clicked = False
            # add start button
            start2_button.create_button()
            if start2_button.click_check() is True:
                creator_clicked = False
                start_clicked = True

        elif start_clicked is False and creator_clicked is False and options_clicked is True and about_clicked is False: # OPTIONS
            is_visible[0] = False
            is_visible[1] = False
            is_visible[3] = False
            screen.fill((192, 192, 192))
        elif start_clicked is False and creator_clicked is False and options_clicked is False and about_clicked is True: # ABOUT
            is_visible[0] = False
            is_visible[1] = False
            is_visible[2] = False
            screen.fill((192, 192, 192))
        elif start_clicked is True: # GAME
            is_visible[1] = False
            is_visible[2] = False
            is_visible[3] = False
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

