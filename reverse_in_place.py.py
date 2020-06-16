''' 
Reverse an array in-place.
Time complexity is O(n)
Space complexity is O(1)
'''

def reverse(A):
    if len(A) == 1 or len(A) == 0:
        return A
    start = 0
    end = len(A)-1
    while start < end:
        A[end], A[start] = A[start], A[end]
        start = start + 1
        end = end - 1
    return A

if __name__ == "__main__":
    
    A = [1,2,3,4,5,6,7,8,9]
    print('Before: ', *A)
    print('After:  ', *reverse(A))
