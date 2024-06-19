# def neg_vs_pos(a_numbers):
#     positives = 0
#     negatives = 0
#     for el in a_numbers:
#         el = int(el)
#         if el > 0:
#             positives += el
#         else:
#             negatives += el
#     print(negatives)
#     print(positives)
#     if positives > abs(negatives):
#         print("The positives are stronger than the negatives")
#     else:
#         print("The negatives are stronger than the positives")
#
#
# neg_vs_pos(input().split())

def neg_vs_pos(*args):
    positives = sum([el for el in args if el > 0])
    negatives = sum([el for el in args if el < 0])

    if abs(negatives) > positives:
        return f"{negatives}\n{positives}\nThe negatives are stronger than the positives"
    else:
        return f"{negatives}\n{positives}\nThe positives are stronger than the negatives"

numbers = [int(el) for el in input().split()]
print(neg_vs_pos(*numbers))