from circleshape import CircleShape
from shot import Shot
from constants import *
import pygame


class Player(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, PLAYER_RADIUS)
        self.speed = 0
        self.rotation = 0
        self.timer = 0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()

        # turn left
        if keys[pygame.K_a]:
            self.rotate(-dt)
        # turn right
        if keys[pygame.K_d]:
            self.rotate(dt)
        # move forward
        if keys[pygame.K_w]:
            self.move(dt)
        # move back
        if keys[pygame.K_s]:
            self.move(-dt)
        # shoot
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        # We start with a unit vector pointing straight up from (0, 0) to (0, 1).
        # We rotate that vector by the player's rotation, so it's pointing in the direction the player is facing.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # We multiply by PLAYER_SPEED * dt. A larger vector means faster movement.
        # Add the vector to our position to move the player.
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        self.timer = PLAYER_SHOOT_COOLDOWN

        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)

        direction = pygame.Vector2(0,1).rotate(self.rotation)
        shot.velocity = direction * PLAYER_SHOOT_SPEED

        