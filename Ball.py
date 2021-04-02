from Paddle import Paddle

color_progression = ['#FFFFFF', '#FFFF00', '#FFFA00', '#FF0000',
                     '#800080', '#0000FF']

class Ball():
    def __init__(self, radius=20, ball_speed=5):
        self.x = width / 2
        self.y = height / 2 
        self.radius = radius
        self.speed = ball_speed
        self.x_speed = self.speed
        self.y_speed = self.speed
        self.color_index = 0
        self.ball_color = color_progression[self.color_index]
        self.isAlive = False
        self.currently_intersects = False
        
    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        
        if self.x + -(2 * self.radius) or self.x - (2 * self.radius) > width:
            self.is_alive = False
            
        if self.y - (2 * self.radius) <= 0 or self.y + (2 * self.radius >= height:
            self.y_speed = -self.y_speed
        
        
    def draw(self):
        push()
        
        strokeWeight(5)
        fill(self.ball_color, 100)
        ellipse(self.x, self.y, 2 * self.radius, 2 * self.radius)
        
        pop()
        
    def start_ball():
        if not is_alive:
            self.is_alive = True
            self.x = width / 2
            self.y = height / 2
            
        calc_speed = int(random(self.speed)) + 5
        if random(1) >= 0.5:
            self.speed_x = calc_speed
        else:
            self.speed_x = -calc_speed 

        calc_speed = int(random(self.speed)) + 3
        if random(1) >= 0.5:
            self.speed_y = calc_speed
        else:
            self.speed_y = -calc_speed 


    def collision(self, paddle):
        side_x = None
        side_y = None

        # Temporary variables to set edges for testing
        edge_x = self.x
        edge_y = self.y

        if self.x < paddle.x:
            edge_x = paddle.x                  # Ball is left of the paddle
            side_x = 'left'
        elif self.x > paddle.x + paddle.width:
            edge_x = paddle.x + paddle.width   # Ball is right of the paddle
            side_x = 'right'
        if self.y < paddle.y:
            edge_y = paddle.y                  # Ball is above the paddle
            side_y = 'top'
        elif self.y > paddle.y + paddle.height:
            edge_y = paddle.y + paddle.height  # Ball is below the paddle
            side_y = 'bottom'

        # Get distance from pythagoream theorem
        dist_x = self.x - edge_x
        dist_y = self.y - edge_y
        distance = sqrt( (dist_x * dist_x) + (dist_y * dist_y) )

        # If the distance is less than the radius, collision!
        if distance <= self.radius:        
            if not self.currently_intersects:
                self.currently_intersects = True
                
                self.speed_x += 2
                self.speed_y += 2
                
                if self.color_index >= len(color_progression):
                    self.ball_color = color(random(255), random(255), random(255));
                else:
                    self.ball_color = color_progression[color_index]
    
                if side_x == 'right':
                    if self.speed_x < 0:
                        self.x_speed = -self.x_speed
                elif side_x == 'left':
                    if self.speed_x > 0:
                        self.speed_x = -self.x_speed
                
                if side_y == 'top':
                    if self.speed_y > 0:
                        self.speed_y = -self.speed_y
                elif side_y == 'bottom':
                    if self.speed_y < 0:
                        self.speed_y = -self.speed_y
        else:
            # Sometimes upon first collision the ball would still be within
            # the paddle, causing the ball to rebound back and forth.
            # Resetting the variable here ensures there's only 1 change of
            # direction until the ball and paddle no longer intersect 
            if self.currently_intersects:
                self.currently_intersects = False
