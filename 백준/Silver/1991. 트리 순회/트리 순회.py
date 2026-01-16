import sys
input = sys.stdin.readline

N = int(input())
left = [-1 for _ in range(26)]
right = [-1 for _ in range(26)]

for _ in range(N):
    root, l, r = map(str, input().rstrip().split())
    root_alpha = ord(root) - ord('A')
    if l != '.':
        left[root_alpha] = ord(l) - ord('A')
    if r != '.':
        right[root_alpha] = ord(r) - ord('A')
    

def preorder(cur):
    if cur == -1:
        return
    print(chr(cur + ord('A')), end='')
    preorder(left[cur])
    preorder(right[cur])


def inorder(cur):
    if cur == -1:
        return
    inorder(left[cur])
    print(chr(cur + ord('A')), end='')
    inorder(right[cur])


def postorder(cur):
    if cur == -1:
        return
    postorder(left[cur])
    postorder(right[cur])
    print(chr(cur + ord('A')), end='')

preorder(0)
print()
inorder(0)
print()
postorder(0)