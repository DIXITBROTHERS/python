def divide_numbers(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        print("Cannot Divide")
        return None
    except ValueError:
        print("Invalid Data")
        return None
    else:
        return result

nu = int(input())
de = int(input())

divide_numbers(nu,de)