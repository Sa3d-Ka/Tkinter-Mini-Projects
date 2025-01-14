import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import random


class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.geometry("250x250")
        self.root.resizable(False, False)


        # Apply a ttkbootstrap theme
        self.style = ttk.Style(theme="cosmo")  # Choose a theme: cosmo, flatly, minty, etc.

        # Create a container frame to hold all pages
        self.container = ttk.Frame(root)
        self.container.pack(fill="both", expand=True)

        # Create frames for each page
        self.frames = {}
        for Page in (MainPage, PlayWithFriendPage, PlayAgainstBotPage):
            page_name = Page.__name__
            frame = Page(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")  # Place all frames in the same location

        # Show the main page
        self.show_frame("MainPage")

    def show_frame(self, page_name):
        """Bring the specified frame to the top."""
        frame = self.frames[page_name]
        frame.tkraise()


class MainPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        label = ttk.Label(self, text="Tic Tac Toe", font=("Arial", 24))
        label.pack(pady=20)

        play_with_friend_btn = ttk.Button(self, text="Play With Friend", bootstyle=PRIMARY,
                                         command=lambda: controller.show_frame("PlayWithFriendPage"))
        play_with_friend_btn.pack(pady=10)

        play_against_bot_btn = ttk.Button(self, text="Play Against Bot", bootstyle=SUCCESS,
                                         command=lambda: controller.show_frame("PlayAgainstBotPage"))
        play_against_bot_btn.pack(pady=10)


class PlayWithFriendPage(ttk.Frame):
    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller

        self.players = ["x", "o"]
        self.player = random.choice(self.players)
        self.game_btns = [[None for _ in range(3)] for _ in range(3)]

        self.label = ttk.Label(self, text=(self.player + " turn"), font=("Arial", 24))
        self.label.pack(side="top")

        # Create a frame to hold the buttons
        self.btns_frame1 = ttk.Frame(self)
        self.btns_frame1.pack(side="top", pady=10)

        # "Back to Main" button
        back_btn = ttk.Button(self.btns_frame1, text="Back to Main", bootstyle=WARNING,
                              command=lambda: controller.show_frame("MainPage"))
        back_btn.pack(side="left", padx=10)

        # "Restart" button
        restart_btn = ttk.Button(self.btns_frame1, text="Restart", bootstyle=INFO,
                                 command=self.start_new_game)
        restart_btn.pack(side="left", padx=10)

        self.btns_frame = ttk.Frame(self)
        self.btns_frame.pack()

        for row in range(3):
            for col in range(3):
                self.game_btns[row][col] = ttk.Button(self.btns_frame, text="", width=6, bootstyle=SECONDARY,
                                                      command=lambda row=row, col=col: self.next_turn(row, col))
                self.game_btns[row][col].grid(row=row, column=col, padx=5, pady=5)

    def next_turn(self, row, col):
        if self.game_btns[row][col]['text'] == "" and self.check_winner() is False:
            self.game_btns[row][col]['text'] = self.player

            if self.check_winner() is False:
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=(self.player + " turn"))
            elif self.check_winner() == "tie":
                self.label.config(text="Tie, No Winner!")
            else:
                self.label.config(text=(self.player + " wins!"))

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.game_btns[row][0]['text'] == self.game_btns[row][1]['text'] == self.game_btns[row][2]['text'] != "":
                self.highlight_winning_cells(row, 0, row, 1, row, 2)
                return True

        # Check columns
        for col in range(3):
            if self.game_btns[0][col]['text'] == self.game_btns[1][col]['text'] == self.game_btns[2][col]['text'] != "":
                self.highlight_winning_cells(0, col, 1, col, 2, col)
                return True

        # Check diagonals
        if self.game_btns[0][0]['text'] == self.game_btns[1][1]['text'] == self.game_btns[2][2]['text'] != "":
            self.highlight_winning_cells(0, 0, 1, 1, 2, 2)
            return True
        elif self.game_btns[0][2]['text'] == self.game_btns[1][1]['text'] == self.game_btns[2][0]['text'] != "":
            self.highlight_winning_cells(0, 2, 1, 1, 2, 0)
            return True

        # Check for tie
        if not self.check_empty_spaces():
            return "tie"
        else:
            return False

    def highlight_winning_cells(self, r1, c1, r2, c2, r3, c3):
        self.game_btns[r1][c1].config(bootstyle=SUCCESS)
        self.game_btns[r2][c2].config(bootstyle=SUCCESS)
        self.game_btns[r3][c3].config(bootstyle=SUCCESS)

    def check_empty_spaces(self):
        for row in range(3):
            for col in range(3):
                if self.game_btns[row][col]['text'] == "":
                    return True
        return False

    def start_new_game(self):
        self.player = random.choice(self.players)
        self.label.config(text=(self.player + " turn"))

        for row in range(3):
            for col in range(3):
                self.game_btns[row][col].config(text="", bootstyle=SECONDARY)


class PlayAgainstBotPage(PlayWithFriendPage):
    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        self.label.config(text=(self.player + " turn (You are X)"))

    def next_turn(self, row, col):
        if self.game_btns[row][col]['text'] == "" and self.check_winner() is False:
            self.game_btns[row][col]['text'] = self.player

            if self.check_winner() is False:
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=(self.player + " turn"))

                if self.player == "o":  # Bot's turn
                    self.bot_move()

            elif self.check_winner() == "tie":
                self.label.config(text="Tie, No Winner!")
            else:
                self.label.config(text=(self.player + " wins!"))

    def bot_move(self):
        empty_cells = [(row, col) for row in range(3) for col in range(3) if self.game_btns[row][col]['text'] == ""]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.game_btns[row][col]['text'] = "o"
            if self.check_winner() is False:
                self.player = self.players[1] if self.player == self.players[0] else self.players[0]
                self.label.config(text=(self.player + " turn"))
            elif self.check_winner() == "tie":
                self.label.config(text="Tie, No Winner!")
            else:
                self.label.config(text=("o wins!"))


# Run the application
if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Apply a ttkbootstrap theme
    app = MainApp(root)
    root.mainloop()