import pygame

images = {
    "hub_background":"",
    "blackjack_background":"",
    "cards":[],
    "checkers_background":"",
    "black_piece":"",
    "white_piece":"",
    "black_king":"",
    "white_king":""
}

live_buttons = []

pygame.init()


class txt_button:
    def __init__(self, txt: str, fill_color: tuple, text_color: tuple, pos_x: int, pos_y: int, width: int, height: int) -> None:
        self.text = txt
        self.text_color = text_color
        self.color = fill_color
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def display(self, surface, font_size: int, outline: int = 0) -> None:
        pygame.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.width, self.height), outline)
        if self.text != "":
            font = pygame.font.Font('freesansbold.ttf', font_size)
            text = font.render(self.text, 1, self.text_color)
            surface.blit(text, (self.pos_x + (self.width/2 - text.get_width()/2), self.pos_y + (self.height/2 - text.get_height()/2)))

    def update_rect(self, *dims) -> None:
        """(pos_x, pos_y, width, height) -> None
        Takes the dimensions of the new rectangle and position and updates the internal values
        *Does not redraw the rectangle
        """
        self.pos_x = dims[0]
        self.pos_y = dims[1]
        self.width = dims[2]
        self.height = dims[3]


def display_hub(surface):
    #surface.blit(images["hub_background"],  (0,0))
    #live_buttons.clear()
    blkjck_button = txt_button("PLAY BLACKJACK!", (255,255,255), (0,0,0), 125, 334, 200, 100)
    ckrs_button = txt_button("PLAY CHECKERS!", (255,255,255), (0,0,0,), 625, 334, 200, 100)
    blkjck_button.display(surface, 20)
    ckrs_button.display(surface, 20)
    

def display_init(surface):
    surface.blit(images["blackjack_background"], (0,0))
    #display text label w/up arrow/+ sign, down arrow/- sign to increment countable values in game settings
    #button for num_of_decks, gambling (when changed to true display starting_money button w/incrementors, false remove it)



window = pygame.display.set_mode((900,768))
window.fill((192,192,192))
display_hub(window)
pygame.display.update()

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.QU