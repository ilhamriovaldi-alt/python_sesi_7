import time

# Menampilkan jam sebanyak 5 kali, jeda 1 detik setiap tampilan.
for _ in range(5):
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S", current_time)
    print(formatted_time)
    time.sleep(1)
