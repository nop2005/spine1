import tkinter as tk
from tkinter import messagebox

# ฟังก์ชันสำหรับตรวจสอบผู้ชนะ
def check_winner():
    for row in board:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return row[0]["text"]
    for col in range(3):
        if board[0][col]["text"] == board[1][col]["text"] == board[2][col]["text"] != "":
            return board[0][col]["text"]
    if board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"] != "":
        return board[0][0]["text"]
    if board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"] != "":
        return board[0][2]["text"]
    return None

# ฟังก์ชันสำหรับการคลิกปุ่ม
def button_click(row, col):
    global current_player
    if board[row][col]["text"] == "" and not check_winner():
        board[row][col]["text"] = current_player
        winner = check_winner()
        if winner:
            messagebox.showinfo("ผลลัพธ์", f"ผู้เล่น {winner} ชนะ!")
            reset_game()
        elif all(board[r][c]["text"] != "" for r in range(3) for c in range(3)):
            messagebox.showinfo("ผลลัพธ์", "เสมอกัน!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

# ฟังก์ชันสำหรับรีเซ็ตเกม
def reset_game():
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            board[row][col]["text"] = ""

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("เกม XO")

# สร้างตาราง 3x3
board = [[None for _ in range(3)] for _ in range(3)]
current_player = "X"

for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), width=5, height=2,
                           command=lambda r=row, c=col: button_click(r, c))
        button.grid(row=row, column=col)
        board[row][col] = button

# เริ่มโปรแกรม
root.mainloop()