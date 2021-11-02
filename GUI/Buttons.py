import pygame

class txt_button:
    def __init__(self, txt: str, color: tuple, width: int, height: int, pos_x: int, pos_y: int) -> None:
        self.text = txt
        self.color = color
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        
    def display(self, surface, outline: int = 0) -> None:
        pygame.draw.rect(surface, self.color, (self.pos_x, self.pos_y, self.width, self.height), outline)
    
    def update_rect(self, *dims) -> None:
        self.pos_x = dims[0]
        self.pos_y = dims[1]
        self.width = dims[2]
        self.height = dims[3]

