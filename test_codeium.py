# define a function to sum num1 and num2
def sum(num1: int, num2: int) -> int:
    """
    計算兩個整數的總和。

    Args:
        num1 (int): 第一個整數。
        num2 (int): 第二個整數。

    Returns:
        int: 兩個整數的總和。
    """
    # Add the two integers together and return the result
    return num1 + num2

def get_dict():
    return {"a": 1, "b": 2}



def main() -> None:
    """
    The main function that executes the program.
    It calls the `sum` function with two integers and prints the result.

    This function does not take any parameters.
    It does not return anything.
    """
    # Call the `sum` function with two integers and store the result in a variable
    result = sum(10, 20)

    # Print the result of the `sum` function
    print(result)

