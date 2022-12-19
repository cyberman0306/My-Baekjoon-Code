
def recursion(s, l, r, count):
    count += 1
    if l >= r: return [1, count]
    elif s[l] != s[r]: return 0, count
    else: return recursion(s, l+1, r-1, count)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 0)


n = int(input())
for i in range(n):
    space = input()
    #print(isPalindrome(space))
    print(isPalindrome(space)[0], isPalindrome(space)[1])
    #print(recursion())
#print('ABBA:', isPalindrome('ABBA'))
#print('ABC:', isPalindrome('ABC'))