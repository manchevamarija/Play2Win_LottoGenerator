# data.py
import ast, re

def load_draws(path="data.txt"):
    draws = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            m = re.search(r"\[(.*?)\]", line)
            if m:
                nums = ast.literal_eval("[" + m.group(1) + "]")
                if len(nums) == 7:
                    draws.append(sorted(nums))
    return draws
