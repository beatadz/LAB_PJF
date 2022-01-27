#Beata Dziewulska WCY19IJ1S1
import pygame
import shapes
import piece
import grid
import random
import score
import button
import checkbox
import new_shape


def draw_frame(screen, board_width, board_height, line_thickness, color):
    pygame.draw.rect(screen, color, [0, 0, board_width + 2 * line_thickness, board_height], line_thickness)

def game_loop(screen, grid_, current_piece, score_, board_width, board_height, line_thickness, screen_width, screen_height):
    # VARIABLES
    frame_color =  (0, 0, 0)
    background_color = (192, 192, 192)
    text_color = (0, 0, 0)
    time = pygame.time.Clock().tick(1000)
    clock = pygame.time.Clock()
    FPS = 60
    speed = 3000
    max_speed = 3000
    move_speed = 2
    rotation_speed = 10
    rotation_counter = move_counter = new_shapes_count = 0
    running = show = True
    falling = clock.tick(FPS)
    start_clicked = creator_clicked = options_clicked = controls_clicked = game_over_clicked = False
    boxes = []
    pause = saved = incorrect = False
    is_visible = [True, True, True, True]
    gap = 80
    rotate = True

    # IMAGES
    background_image = pygame.image.load("resources/background.png")
    blue_button_image = pygame.image.load("resources/blue_button.png")
    pink_button_image = pygame.image.load("resources/pink_button.png")
    yellow_button_image = pygame.image.load("resources/yellow_button.png")
    green_button_image = pygame.image.load("resources/green_button.png")
    purple_button_image = pygame.image.load("resources/purple_button.png")
    controls_image = pygame.image.load("resources/controls2.png")
    pause_image = pygame.image.load("resources/pause.png")
    button_width, button_height = blue_button_image.get_size()

    # RADIO BUTTONS
    for i in range(len(shapes.shape_colors)):
        r_button = checkbox.Checkbox(screen, 550, 190 + (i * 50), (255, 255, 255), "color", (0, 0, 0),
                                     shapes.shape_colors[i], 20, shapes.shape_colors[i], 570,
                                     190 + (i * 50), "arial", shapes.shape_colors[i])
        boxes.append(r_button)

    dark_mode_button = checkbox.Checkbox(screen, 100, 190, background_color, "DARK MODE", (0, 0, 0),
                                         (102, 178, 255), 20, text_color, 120,
                                         170, "arial", background_color)
    rotation_button = checkbox.Checkbox(screen, 100, 240, background_color, "ROTATION", (0, 0, 0),
                                        (102, 178, 255), 20, text_color, 120,
                                        240, "arial", background_color)
    rotation_button.checked = True

    show_next_shape_button = checkbox.Checkbox(screen, 100, 290, background_color, "SHOW NEXT SHAPE", (0, 0, 0),
                                        (102, 178, 255), 20, text_color, 120,
                                        290, "arial", background_color)
    show_next_shape_button.checked = True

    # BUTTONS
    start_button = button.Button("START", (screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 - gap), "arial", (0, 0, 0), 23, blue_button_image, 1, screen)
    creator_button = button.Button("SHAPE CREATOR", (screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2), "arial", (0, 0, 0), 23, pink_button_image, 1, screen)
    options_button = button.Button("OPTIONS", (screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + gap), "arial", (0, 0, 0), 23, yellow_button_image, 1, screen)
    controls_button = button.Button("CONTROLS", (screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 2 * gap), "arial", (0, 0, 0), 23, green_button_image, 1, screen)
    quit_button = button.Button("QUIT", (screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 3 * gap), "arial", (0, 0, 0), 23, purple_button_image, 1, screen)
    clear_button = button.Button("CLEAR", (65, 380), "arial",(0, 0, 0), 23, yellow_button_image, 0.7, screen)
    save_button = button.Button("SAVE", (0.7 * button_width + 75, 380), "arial", (0, 0, 0), 23, green_button_image, 0.7, screen)
    back_button = button.Button("BACK", (65, 710), "arial", (0, 0, 0), 23, purple_button_image, 0.7, screen)
    start2_button = button.Button("START", (75 + 0.7 * button_width, 710), "arial", (0, 0, 0), 23, blue_button_image, 0.7, screen)
    play_again_button = button.Button("PLAY AGAIN", (screen_width/2 - button_width/2, screen_height/2 - button_height/2), "arial", (0, 0, 0), 23, blue_button_image, 1, screen)
    back2_button = button.Button("BACK", (screen_width/2 - button_width/2, screen_height/2 - button_height/2 + button_height + 20), "arial", (0, 0, 0), 23, purple_button_image, 1, screen)
    back3_button = button.Button("BACK", (screen_width / 2 - button_width / 2, screen_height - 120), "arial", (0, 0, 0), 23, blue_button_image, 1, screen)
    back4_button = button.Button("BACK", (screen_width / 2 - button_width / 2, screen_height - 120), "arial", (0, 0, 0), 23, blue_button_image, 1, screen)
    quit2_button = button.Button("QUIT", (screen_width / 2 - button_width / 2, screen_height / 2 - button_height / 2 + 2 * button_height + 40), "arial", (0, 0, 0), 23, green_button_image, 1, screen)

    # Game Loop
    while running:
        key = pygame.key.get_pressed()
        screen.fill(background_color)
        falling += clock.tick(FPS)
        rotation_counter += 1
        move_counter += 1
        is_down = False
        selected_color = 0

        time += pygame.time.Clock().tick(1000)

        # ESC OR GAME OVER
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # MAIN WINDOW
        tetris_title = pygame.image.load("resources/Tetris.png")
        tetris_title = pygame.transform.scale(tetris_title, (screen_width - 200, 131))
        screen.fill(background_color)
        screen.blit(tetris_title, (screen_width / 2 - ((screen_width - 200) / 2), 100))
        screen.blit(background_image, (0, 0))
        start_button.create_button()
        creator_button.create_button()
        options_button.create_button()
        controls_button.create_button()
        quit_button.create_button()

        # check if user clicked on any button
        if start_button.click_check() is True and is_visible[0] is True:
            start_clicked = True
        elif creator_button.click_check() is True and is_visible[1] is True:
            creator_clicked = True
        elif options_button.click_check() is True and is_visible[2] is True:
            options_clicked = True
        elif controls_button.click_check() is True and is_visible[3] is True:
            controls_clicked = True
        elif quit_button.click_check() is True:
            running = False

        if start_clicked is False and creator_clicked is True and options_clicked is False and controls_clicked is False: # SHAPE CREATOR
            is_visible[0] = False
            is_visible[2] = False
            is_visible[3] = False
            screen.fill(background_color)
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
            color_text = font.render("COLOR", True, text_color)
            screen.blit(color_text, (535, 130))
            #draw - "SELECT SQUARES"
            shape_text = font.render("SELECT SQUARES", True, text_color)
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
                        for j in range(len(boxes)):
                            if j != i:
                                boxes[j].checked = False

            # draw creator grid
            grid_.draw_creator_grid(selected_color)
            # add clear button
            clear_button.create_button()
            if clear_button.click_check() is True:
                grid_.clear_creator_grid(boxes)
                saved = False
                incorrect = False
            # add save button
            save_button.create_button()
            if save_button.click_check() is True and start_clicked is False:
                saved = not saved
                new = new_shape.NewShape(grid_)
                empty = new.save_shape(grid_, new_shapes_count)
                # draw - "SAVED"
                if empty is False:
                    saved = True
                    new_shapes_count += 1
                else:
                    saved = False

                if new.correct is False:
                    incorrect = True

            if saved is True:
                font = pygame.font.SysFont('arial', 50)
                saved_text = font.render("SAVED", True, text_color)
                screen.blit(saved_text, (133, 510))
            elif incorrect is True:
                font = pygame.font.SysFont('arial', 30)
                incorrect_text = font.render("INCORRECT SHAPE", True, text_color)
                screen.blit(incorrect_text, (80, 510))

            # add back button
            back_button.create_button()
            if back_button.click_check() is True:
                start_clicked = False
                creator_clicked = False
                options_clicked = False
                controls_clicked = False
                is_visible[0] = True
                is_visible[1] = True
                is_visible[2] = True
                is_visible[3] = True
                grid_.clear_creator_grid(boxes)
                saved = False
                incorrect = False
            # add start button
            start2_button.create_button()
            if start2_button.click_check() is True:
                creator_clicked = False
                start_clicked = True

        elif start_clicked is False and creator_clicked is False and options_clicked is True and controls_clicked is False: # OPTIONS
            is_visible[0] = False
            is_visible[1] = False
            is_visible[3] = False
            screen.fill(background_color)

            font = pygame.font.SysFont('arial', 60)
            options_text = font.render("OPTIONS", True, text_color)
            text_width, text_height = font.size("OPTIONS")
            screen.blit(options_text, (screen_width / 2 - text_width / 2, 30))

            # radio buttons
            dark_mode_button.render_checkbox()
            rotation_button.render_checkbox()
            show_next_shape_button.render_checkbox()
            if pygame.mouse.get_pressed()[0] == 1:
                dark_mode_button.update_checkbox()
                rotation_button.update_checkbox()
                show_next_shape_button.update_checkbox()
                if dark_mode_button.checked is True:
                    background_color = (64, 64, 64)
                    text_color = (255, 255, 255)
                    frame_color = (255, 255, 255)
                    controls_image = pygame.image.load("resources/controls3.png")
                else:
                    background_color = (192, 192, 192)
                    text_color = (0, 0, 0)
                    frame_color = (0, 0, 0)
                    controls_image = pygame.image.load("resources/controls2.png")

                dark_mode_button.color = rotation_button.color =  show_next_shape_button.color = background_color
                dark_mode_button.text_background = rotation_button.text_background = show_next_shape_button.text_background = background_color
                dark_mode_button.font_color = rotation_button.font_color = show_next_shape_button.font_color = text_color
                if rotation_button.checked is True:
                    rotate = not rotate
                if show_next_shape_button.checked is True:
                    show = True
                else:
                    show = False
            # BACK BUTTON
            back3_button.create_button()
            if back3_button.click_check() is True:
                start_clicked = False
                creator_clicked = False
                options_clicked = False
                controls_clicked = False
                is_visible[0] = True
                is_visible[1] = True
                is_visible[2] = True
                is_visible[3] = True

        elif start_clicked is False and creator_clicked is False and options_clicked is False and controls_clicked is True: # CONTROLS
            is_visible[0] = False
            is_visible[1] = False
            is_visible[2] = False
            screen.fill(background_color)
            # draw - "CONTROLS"
            font = pygame.font.SysFont('arial', 60)
            controls_text = font.render("CONTROLS", True, text_color)
            text_width, text_height = font.size("CONTROLS")
            screen.blit(controls_text, (screen_width / 2 - text_width / 2, 30))
            # BACK BUTTON
            back4_button.create_button()
            # add image
            image_width, image_height = controls_image.get_size()
            screen.blit(controls_image, (screen_width/2 - image_width/2, 120))

            if back4_button.click_check() is True:
                start_clicked = False
                creator_clicked = False
                options_clicked = False
                controls_clicked = False
                is_visible[0] = True
                is_visible[1] = True
                is_visible[2] = True
                is_visible[3] = True

        elif start_clicked is True and game_over_clicked is False: # GAME
            is_visible[1] = False
            is_visible[2] = False
            is_visible[3] = False
            screen.fill(background_color)  # change background color
            grid_.draw_grid() # draw grid
            draw_frame(screen, board_width, board_height, line_thickness, frame_color) # draw frame
            current_piece.draw_shape() # draw first shape
            if show is True:
                grid_.draw_small_grid()  # draw grid for next shape
                current_piece.draw_next_shape() # draw next shape
                shapes.display_next(screen, board_width, text_color)  # display "next"
            score_.display_score(text_color, 30, board_width + 20, 0, 1) # display game score

            if pause is True:
                image_width, image_height = pause_image.get_size()
                screen.blit(pause_image, (screen_width/2 - image_width/2, screen_height/2 - image_height/2))

            c_right = current_piece.check_right()
            c_left = current_piece.check_left()
            c_bottom = current_piece.check_bottom()

            # check stop condition
            current_piece.check_end()
            if current_piece.stop is False:
                game_over_clicked = True
                start_clicked = False

            else:
                # check if there is any full or empty line
                current_piece.check_full_line()
                current_piece.fix_empty_lines()

                # speed depends on lines
                if score_.lines > 0 and score_.lines % 2 == 0 and score_.previous_line != score_.lines:
                    if speed > 0:
                        if speed >= (speed * 2/3):
                            speed -= 400
                        elif speed >= (speed * 1/3):
                            speed -= 150
                        else:
                            speed -= 50
                    print(speed)
                    score_.previous_line = score_.lines

                # draw - "SPEED"
                font = pygame.font.SysFont('arial', 30)
                text = "SPEED: "
                add = str(max_speed - speed + 10)
                text = text + add
                speed_text = font.render(text, True, text_color)
                screen.blit(speed_text, (board_width + 20, 80))

                # KEYBOARD
                if key[pygame.K_SPACE]:
                    if time / 1000.0 > 0.01:
                        time = 0
                        pause = not pause

                if pause is False:
                    if key[pygame.K_UP] or key[pygame.K_w]:
                        if rotation_counter > rotation_speed and current_piece.check_rotation() is True and rotate is True:
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
                        falling = 0

        elif game_over_clicked is True: # GAME OVER
            # GAME OVER WINDOW
            screen.fill(background_color)
            screen.blit(background_image, (0, 0))
            # draw - "GAME OVER"
            font = pygame.font.SysFont('arial', 60)
            game_over_text = font.render("GAME OVER", True, text_color)
            text_width, text_height = font.size("GAME OVER")
            screen.blit(game_over_text, (screen_width / 2 - text_width / 2, screen_height / 2 - 300))
            play_again_button.create_button()
            back2_button.create_button()
            quit2_button.create_button()
            font = pygame.font.SysFont('arial', 50)
            text_width, text_height = font.size("SCORE: ")
            score_.display_score(text_color, 50, screen_width / 2 - text_width / 2, screen_height / 2 - 200, 0)  # display game score
            # check if user wants to start the game
            if play_again_button.click_check() is True:
                grid_.clear_grid() # clean everything
                score_.game_score = 0 # reset score
                game_over_clicked = False
                current_piece.stop = True
                start_clicked = True
            # check if user wants to back to the main window
            elif back2_button.click_check() is True:
                start_clicked = False
                creator_clicked = False
                options_clicked = False
                controls_clicked = False
                grid_.clear_grid()  # clean everything
                score_.game_score = 0  # reset score
                game_over_clicked = False
                current_piece.stop = True
                grid_.clear_creator_grid(boxes)
                saved = False
                incorrect = False

                is_visible[0] = True
                is_visible[1] = True
                is_visible[2] = True
                is_visible[3] = True

            # check if user wants to end the game
            elif quit2_button.click_check() is True:
                running = False

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

