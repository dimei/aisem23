def mysum(numbers):
    result=sum(numbers)
    return result

x=[1,2,3]

# manual testing
y = mysum(x)
print(y)

# automatic testing
assert mysum(x) == 6


# embed assert inside function 
def test_mysum():
    
    assert mysum([1,2,3]) == 6, "Should be 6"


def test_mysum_tuple():
    assert mysum((1,2,3)) == 6, "Should be 6"

def test_mysum_wrong_result():
    assert mysum((1,2,2)) == 6, "Should be 6"

def test_mysum_wrong_type():
    assert mysum((1,2,'3')) == 6, "Should be 6"