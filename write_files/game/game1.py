import random
import datetime


class RockPaperScissor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.player_score = 0  # Corrected from player_name to player_score and initialized to 0
        self.computer_score = 0  # Corrected from computer_name to computer_score and initialized to 0

    def play_game(self):
        print('Игра началась!')
        self.log_action('Начало игры! ' + datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

        while self.player_score < 3 and self.computer_score < 3:
            player_choice = str(input("Выберите камень, бумагу или ножницы: ")).lower()
            if player_choice not in ['камень', 'бумага', 'ножницы']:
                print('Неправильный выбор')
                continue

            computer_choice = random.choice(['камень', 'бумага', 'ножницы'])
            print(f'Компьютер показал {computer_choice}')

            result = self.determine_winner(player_choice, computer_choice)
            print(result)
            self.log_action(f'Игрок показал - {player_choice}\n'
                            f'Компьютер показал - {computer_choice}\n'
                            f'Результат - {result}')

        if self.player_score == 3:
            winner_message = "Игрок выиграл!"
        else:
            winner_message = "Компьютер выиграл!"
        print(winner_message)
        self.log_action(winner_message)
        self.log_action("Конец игры " + datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S'))

    def determine_winner(self, player, computer):  # Corrected the method name
        if player == computer:
            return 'Ничья'
        elif (player == 'камень' and computer == 'ножницы') or \
             (player == 'ножницы' and computer == 'бумага') or \
             (player == 'бумага' and computer == 'камень'):
            self.player_score += 1
            return 'Игрок выиграл этот раунд'
        else:
            self.computer_score += 1
            return 'Компьютер выиграл этот раунд'

    def log_action(self, action):
        try:
            with open(self.file_name, 'a') as f:
                f.write(action + '\n')
        except FileNotFoundError:
            print("Error: Файл не найден")


game = RockPaperScissor("game_text.txt")
game.play_game()
