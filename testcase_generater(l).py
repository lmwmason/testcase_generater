import os
import random
import subprocess
import zipfile

MAX_T = 1000
MAX_N = 400_000
MAX_TOTAL_N = 40_000_000

os.makedirs("test", exist_ok=True)

for idx in range(1, 51):
    is_large = idx > 10
    input_lines = []
    total_n = 0
    t = 0

    while t < MAX_T and total_n < MAX_TOTAL_N:
        curr_max_n = 300 if not is_large else MAX_N
        n = random.randint(10, curr_max_n)

        if total_n + n > MAX_TOTAL_N:
            break

        s = ''.join(random.choices("01", k=n))
        input_lines.append(f"{n}\n{s}")
        total_n += n
        t += 1

    with open(f"test/test{idx:03}.in", "w") as f:
        f.write(f"{t}\n" + "\n".join(input_lines) + "\n")

for idx in range(1, 51):
    with open(f"test/test{idx:03}.in", "r") as fin, open(f"test/test{idx:03}.out", "w") as fout:
        subprocess.run(["python3", "run_original.py"], stdin=fin, stdout=fout)

with zipfile.ZipFile("test.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
    for filename in os.listdir("test"):
        filepath = os.path.join("test", filename)
        zipf.write(filepath, arcname=filename)
