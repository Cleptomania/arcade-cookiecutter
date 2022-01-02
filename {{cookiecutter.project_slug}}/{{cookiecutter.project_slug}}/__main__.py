import arcade

SCREEN_TITLE = "{{cookiecutter.project_name}}"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Game(arcade.Window):
    """
    Main Application Class.

    Note: Go ahead and delete the methods you don't need.
    If you do need a method, delete the 'pass' and replace it
    with your own code.
    """

    def __init__(self):
        """
        Should setup any variables the game needs in this method and
        set them to None. Then use the setup function to initialize
        them to create an easy way to restart the game.
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """
        Set up game variables. Call to easily re-start the game.
        """
        pass

    def on_draw(self):
        """
        Render the screen

        The arcade.start_render() call should happen before we draw.
        It will clear the screen to the background color, and erase
        whatever we drew last frame. Put your draw calls after it.
        """
        arcade.start_render()

    def on_update(self, delta_time):
        """
        All game logic goes here. Movement, scores, etc.
        """
        pass

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.
        
        For a full list of keys, see:
        https://api.arcade.academy/en/latest/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is released after
        previously being pressed.
        """
        pass

    def on_mouse_moution(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called whenever a mouse button is pressed.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called whenever a mouse button is released after
        previously being pressed.
        """
        pass

def main() -> None:
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
