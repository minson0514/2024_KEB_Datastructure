"""
def factorial(number)-> int: #-> 이 뒤에 오는게 리턴 타입
    '''
    factorial by repetition
    Args:
        number: number(int)

    Returns: factorial result(int)

    '''
    result = 1
    for i in range(1, number+1):
        result = result * i
    return result
"""

def factorial(number) -> int:
    '''
    factorial by recursion
    Args:
        number: number(int)

    Returns:factorial result(int)

    '''
    if number ==1:
        return 1
    else:
        return number * factorial(number - 1)

def nCr(n,r)-> int:
    '''
    조합 함수
    Args:
        n:
        r:

    Returns:

    '''
    numerator = factorial(n) #분자
    denominator = factorial(n-r) * factorial(r) #분모
    return int(numerator / denominator) #강제 형변환, 변환 안 하면 double로 리턴되더라

if __name__ == "__main__": #모듈 배울 때 했다네요~
    """
    n = int(input("Input n : "))
    r = int(input("Input r : "))
    print(f"{n}C{r} = {nCr(n,r)}")
    """
    f = int(input())
    print(factorial(f))