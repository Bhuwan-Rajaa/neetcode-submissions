# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        dp = {None:0}

        def dfs(root):
            if root in dp:
                return dp[root]
            
            dp[root] = root.val
            if root.left:
                dp[root] += dfs(root.left.left) + dfs(root.left.right)
            if root.right:
                dp[root] += dfs(root.right.right) + dfs(root.right.left)

            l = dfs(root.left)
            r = dfs(root.right)

            dp[root] = max(dp[root] , l+r)

            return dp[root]

        return dfs(root)