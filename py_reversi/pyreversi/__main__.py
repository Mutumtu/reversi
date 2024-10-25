from pyreversi.gamecontroller import GameController

if __name__ == "__main__":
    game_controller = GameController()
    while True:
        game_controller.start_game()
        if game_controller.will_quit():
            break
    print("Game Over!")
