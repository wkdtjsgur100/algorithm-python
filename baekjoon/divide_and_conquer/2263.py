inorder = [4, 2, 7, 5, 1, 3, 6]
postorder = [4, 7, 5, 2, 6, 3, 1]

inorder_pos = [0] * len(inorder)

for i, k in enumerate(inorder):
    inorder_pos[k - 1] = i


def conquer(inorder_start, inorder_end, postorder_start, postorder_end):
    if inorder_start > inorder_end or postorder_start > postorder_end:
        return

    root_value = postorder[postorder_end]
    print(root_value)

    inorder_right = inorder_pos[root_value - 1]

    left_count = inorder_right - inorder_start
    conquer(inorder_start, inorder_right - 1, postorder_start, postorder_start + left_count - 1)
    conquer(inorder_right + 1, inorder_end, postorder_start + left_count, postorder_end - 1)

conquer(0, 7-1, 0, 7-1)