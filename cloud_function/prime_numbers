import math

def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_numbers(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>
    """
    prime_numbers = [num for num in range(1, 101) if is_prime(num)]
    return ','.join(map(str, prime_numbers))
