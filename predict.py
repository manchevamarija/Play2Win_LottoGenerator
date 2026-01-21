import numpy as np

from data import load_draws
from features import make_features, draw_to_multihot
from model import build_model
from plots import plot_probs


WINDOW = 8
TOPN = 16


draws = load_draws()

if len(draws) < WINDOW + 1:
    raise SystemExit(" Нема доволно податоци за тренинг.")

X, Y = [], []

for i in range(WINDOW, len(draws)):
    X.append(make_features(draws[i - WINDOW:i]))
    Y.append(draw_to_multihot(draws[i]))

X = np.array(X)
Y = np.array(Y)

print(f" Вчитани кола: {len(draws)}")
print(f" Training samples: {len(X)}")



model = build_model()
model.fit(X, Y)

x_next = make_features(draws[-WINDOW:]).reshape(1, -1)
probs = model.predict_proba(x_next)[0]

plot_probs(probs)



ranked = np.argsort(probs)[::-1] + 1
top = ranked[:TOPN]

print("\nНајчесто појавувани броеви:")
for n in top:
    print(f"{n:2d} → {probs[n-1]:.4f}")



ml_combo = sorted(int(n) for n in top[:7])

print("\nПредложена комбинација:")
print(ml_combo)


def score_user_combo(combo, probs):
    if len(combo) != 7:
        raise ValueError("Комбинацијата мора да има точно 7 броеви.")

    if any(n < 1 or n > 37 for n in combo):
        raise ValueError("Броевите мора да бидат во опсег 1–37.")

    score = sum(probs[n - 1] for n in combo) / 7
    return score

user_input = input(
    "\nВнеси твоја комбинација (7 броеви, разделени со запирка) или Enter за skip:\n> "
).strip()

if user_input:
    try:
        user_combo = [int(x) for x in user_input.replace(",", " ").split()]

        if len(user_combo) != 7:
            print(" Мора да внесеш точно 7 броеви.")
        else:
            user_combo = sorted(user_combo)
            user_score = score_user_combo(user_combo, probs)
            ml_score = score_user_combo(ml_combo, probs)

            print("Твоја комбинација :", user_combo)
            print(f"Score              : {user_score:.4f}")

            print("\nСпоредба со ML предлог:")
            print("ML комбинација     :", ml_combo)
            print(f"ML score           : {ml_score:.4f}")

            if user_score > ml_score:
                print("\nТвојата комбинација е ПОДОБРА според моделот.")
            else:
                print("\n ML комбинацијата е ПОДОБРА според моделот.")

    except Exception as e:
        print("Невалиден внес:", e)
