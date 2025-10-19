# สุ่มตัวเลขเป้าหมาย
import random

target = random.randint(1, 100)
print("Target number is:", target)

target = random.randint(1, 100)

# ส่วนของ GUI
root = tk.Tk()
root.title("เกมเดาตัวเลข")

tk.Label(root, text="เดาตัวเลข (1-100):").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

check_button = tk.Button(root, text="ตรวจสอบ", command=check_guess)
check_button.pack(pady=5)

result_label = tk.Label(root, text="เริ่มเกมใหม่! เดาตัวเลข 1-100")
result_label.pack(pady=10)

reset_button = tk.Button(root, text="เริ่มใหม่", command=lambda: reset_game())
reset_button.pack(pady=5)

# เริ่มโปรแกรม
root.mainloop()