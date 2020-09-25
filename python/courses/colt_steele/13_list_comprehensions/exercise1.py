answer = [name[0] for name in ["Elie", "Tim", "Matt"]]

print(answer)

answer_2 = [num for num in [1,2,3,4,5,6] if num%2 ==0]

print(answer_2)

answer_3 = [num for num in [1,2,3,4] if num in [3,4,5,6]]

print(answer_3)

answer_4 = [name[::-1] for name in ["Ellie", "Tim", "Matt"]]

print(answer_4)