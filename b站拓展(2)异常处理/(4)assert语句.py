def get_average(scores):
    total=0
    for score in scores:
        assert 0<=score<=100
        total+=score
    return total/len(scores)
scores=[85,92,78]
print(f'{get_average(scores):.2f}')