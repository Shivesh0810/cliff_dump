from direct.showbase.ShowBase import ShowBase
from direct.gui.DirectGui import DirectLabel, DirectButton
from panda3d.core import Vec3
import random

class OpenWorldGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Load the terrain/environment
        self.environment = self.loader.loadModel("models/environment")
        self.environment.reparentTo(self.render)
        self.environment.setScale(0.25, 0.25, 0.25)
        self.environment.setPos(-8, 42, 0)

        # Load the player (a simple Panda model)
        self.player = self.loader.loadModel("models/panda")
        self.player.reparentTo(self.render)
        self.player.setScale(0.005, 0.005, 0.005)
        self.player.setPos(0, 10, 0)

        # List to store NPCs
        self.npcs = []
        self.create_npcs(5)  # Create 5 NPCs

        # Set up scenery objects (trees or rocks)
        self.create_scenery(10)  # Create 10 scenery objects

        # Mouse controls: Look around with the mouse
        self.disableMouse()  # Disable default mouse control
        self.camera.reparentTo(self.player)
        self.camera.setPos(0, 0, 2)  # Position the camera above the player
        self.mouse_speed = 100  # Control mouse sensitivity

        # Control player movement
        self.player_speed = 10
        self.accept("w", self.move_forward)
        self.accept("s", self.move_backward)
        self.accept("a", self.move_left)
        self.accept("d", self.move_right)
        self.accept("escape", self.show_exit_menu)
        self.taskMgr.add(self.update_npcs, "update_npcs_task")

        # Add mouse look around
        self.taskMgr.add(self.mouse_look, "mouse_look_task")

        # Initialize the exit menu to be hidden
        self.exit_menu = None

    # Player movement functions
    def move_forward(self):
        self.player.setPos(self.player, Vec3(0, self.player_speed * globalClock.getDt(), 0))

    def move_backward(self):
        self.player.setPos(self.player, Vec3(0, -self.player_speed * globalClock.getDt(), 0))

    def move_left(self):
        self.player.setPos(self.player, Vec3(-self.player_speed * globalClock.getDt(), 0, 0))

    def move_right(self):
        self.player.setPos(self.player, Vec3(self.player_speed * globalClock.getDt(), 0, 0))

    # Update NPCs movement
    def update_npcs(self, task):
        for npc in self.npcs:
            direction = random.choice(["up", "down", "left", "right"])
            if direction == "up":
                npc.setY(npc, self.player_speed * globalClock.getDt())
            elif direction == "down":
                npc.setY(npc, -self.player_speed * globalClock.getDt())
            elif direction == "left":
                npc.setX(npc, -self.player_speed * globalClock.getDt())
            elif direction == "right":
                npc.setX(npc, self.player_speed * globalClock.getDt())
        return task.cont

    # Create multiple NPCs
    def create_npcs(self, num_npcs):
        for _ in range(num_npcs):
            npc = self.loader.loadModel("models/panda")
            npc.setScale(0.005, 0.005, 0.005)
            npc.setPos(random.randint(-10, 10), random.randint(-10, 10), 0)
            npc.reparentTo(self.render)
            self.npcs.append(npc)

    # Create static scenery objects (trees or rocks)
    def create_scenery(self, num_objects):
        for _ in range(num_objects):
            scenery = self.loader.loadModel("models/box")  # Simple box for now (replace with tree/rock models)
            scenery.setScale(0.5, 0.5, 0.5)
            scenery.setPos(random.randint(-15, 15), random.randint(-15, 15), 0)
            scenery.reparentTo(self.render)

    # Mouse look around (rotate the player based on mouse movement)
    def mouse_look(self, task):
        md = self.win.getPointer(0)
        x = md.getX()
        y = md.getY()

        # Center the mouse pointer after movement
        if self.win.movePointer(0, self.win.getXSize() // 2, self.win.getYSize() // 2):
            self.player.setH(self.player.getH() - (x - self.win.getXSize() // 2) * self.mouse_speed * globalClock.getDt())
            
            # Update camera pitch, but limit it to prevent flipping upside down
            new_pitch = self.camera.getP() - (y - self.win.getYSize() // 2) * self.mouse_speed * globalClock.getDt()
            new_pitch = max(min(new_pitch, 45), -45)  # Clamp between -45 and 45 degrees
            self.camera.setP(new_pitch)
        
        return task.cont

    # Show exit menu
    def show_exit_menu(self):
        if self.exit_menu is None:
            self.exit_menu = DirectLabel(text="Are you sure you want to exit?",
                                          scale=0.1,
                                          pos=(0, 0, 0.2),
                                          frameColor=(0, 0, 0, 0.5),
                                          text_fg=(1, 1, 1, 1))

            # Yes button
            yes_button = DirectButton(text="Yes", scale=0.05, pos=(-0.1, 0, 0),
                                      command=self.exit_game)
            # No button
            no_button = DirectButton(text="No", scale=0.05, pos=(0.1, 0, 0),
                                     command=self.hide_exit_menu)

    # Exit the game
    def exit_game(self):
        self.userExit()

    # Hide the exit menu
    def hide_exit_menu(self):
        if self.exit_menu is not None:
            self.exit_menu.destroy()
            self.exit_menu = None

# Start the game
game = OpenWorldGame()
game.run()
