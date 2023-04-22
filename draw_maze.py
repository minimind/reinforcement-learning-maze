import pygame

_initialised_screen = False
_screen = None


def get_color_code(code):
    if code == 0:  # the background
        return pygame.colordict.THECOLORS['grey']
    elif code == 1:  # the wall
        return pygame.colordict.THECOLORS['green4']
    elif code == 2:  # the goal
        return pygame.colordict.THECOLORS['red']
    elif code == 3:  # the player
        return pygame.colordict.THECOLORS['dodgerblue3']


def draw_maze(maze_problem):
    global _initialised_screen
    global _screen
    if not _initialised_screen:
        pygame.init()
        _screen = pygame.display.set_mode((720, 720))
        _initialised_screen = True

    for r, row in enumerate(maze_problem.get_maze_definition()):
        x, y = maze_problem.get_state()
        goal_x, goal_y = maze_problem.get_goal()

        for c, column in enumerate(row):
            if r == y and c == x:
                color = get_color_code(2)
            elif r == goal_y and c == goal_x:
                color = get_color_code(3)
            else:
                color = get_color_code(column)

            pygame.draw.rect(
                surface=_screen,
                rect=pygame.Rect(
                    c * _screen.get_width() / 20,
                    r * _screen.get_height() / 20,
                    _screen.get_width() / 20,
                    _screen.get_height() / 20
                ),
                color=color
            )

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False

    return True
