def calculate_price(old_score, new_score):
    price = 0
    point = [0, 1500, 2000, 2500, 3000, 3500, 3800, 4000, 4100, 4200, 4300, 4400]
    coef =  [0, 0.02, 0.03, 0.04, 0.05, 0.09, 0.22, 0.26, 0.5, 0.8, 1.3, 1.7]
    score = old_score
    for i in range(1, 12):
        print(score)
        if score >= new_score:
            break
        else:
            print(i)
            print(point[i])
            if score < point[i]:
                diff = (point[i] - score) if point[i] < new_score else (new_score - score)
                print(diff)
                price += diff*coef[i]
                print(price)
                score = point[i] if point[i] < new_score else new_score
    return round(price, 1)
