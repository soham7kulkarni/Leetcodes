# TC - O(M*N), SC - O(M*N)
# IMP THING IS - your order of conditions decides your if-else conditions 
# when trying tp cover the edge case.Although 1 way is implemented here, 
# changing the sequenece will result in slight modification of if-else conditions.

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])
        r = 0
        c = 0
        flag = False
        result = [0]*(m*n)
        for i in range(len(result)):
            print(mat[r][c])
            result[i] = mat[r][c]
            if not flag:
                if r == 0 and c != n-1:
                    flag = True
                    c+=1
                elif c == n-1:
                    flag = True
                    r += 1
                else:
                    r-=1
                    c+=1
            else:
                if r != m-1 and c == 0:
                    flag = False
                    r += 1
                elif r == m-1 :
                    flag = False
                    c+=1
                else:
                    r += 1
                    c -= 1
        return result

        