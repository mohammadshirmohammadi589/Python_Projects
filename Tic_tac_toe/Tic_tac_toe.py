import random

class TicTacToe:
    def __init__(self):
        self.board = [' '] * 10  # خالی کردن صفحه بازی
        self.player_turn = self.get_random_first_player()  # انتخاب بازیکن اول به صورت تصادفی

    def get_random_first_player(self):
        return 'X' if random.randint(0, 1) == 0 else 'O'  # انتخاب تصادفی بین 'X' و 'O'

    def print_board(self):
        print(f'{self.board[1]} | {self.board[2]} | {self.board[3]}')
        print('---------')
        print(f'{self.board[4]} | {self.board[5]} | {self.board[6]}')
        print('---------')
        print(f'{self.board[7]} | {self.board[8]} | {self.board[9]}')

    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.player_turn
            if self.player_turn == 'X':
                self.player_turn = 'O'
            else:
                self.player_turn = 'X'
        else:
            print("این موقعیت قبلاً اشغال شده است.")

    def check_winner(self):
        winning_combinations = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # ردیف‌ها
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # ستون‌ها
            [1, 5, 9], [3, 5, 7]              # قطرها
        ]

        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == self.board[combination[2]] != ' ':
                return self.board[combination[0]]

        return None

    def is_full(self):
        return ' ' not in self.board[1:]

# اجرای بازی
if __name__ == "__main__":
    game = TicTacToe()
    game.print_board()

    while True:
        position = int(input(f'نوبت بازیکن {game.player_turn}، لطفاً یک موقعیت (1-9) را انتخاب کنید: '))
        if position < 1 or position > 9:
            print("لطفا یک عدد بین 1 و 9 وارد کنید.")
            continue
        game.make_move(position)
        game.print_board()

        winner = game.check_winner()
        if winner:
            print(f'تبریک! بازیکن {winner} برنده شد.')
            break

        if game.is_full():
            print("بازی مساوی شد!")
            break