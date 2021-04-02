PADDLE_LEFT = 0
PADDLE_RIGHT = 1

class Paddle():
    def __init__(self, name=None, paddle_size=50, paddle_LR, paddle_color=None):
        self.y = height / 2
        self.width = paddle_width
        self.height = paddle_height
        self.x_speed = 0
        
        if paddle_LR == PADDLE_LEFT:
            self.x = 0
        elif paddle
        
        if y is not None:
            self.y = y
        
    def update(self):
        if (self.x + self.x_speed >= 0) and (self.x + self.x_speed <= width - self.width):
            self.x += self.x_speed
        
    def draw(self):
        push()
        fill(255)
        rect(self.x, self.y, self.width, self.height)
        pop()
