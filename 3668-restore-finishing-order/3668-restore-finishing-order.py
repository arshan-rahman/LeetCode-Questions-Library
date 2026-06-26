class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_set = set(friends)
        arr = []

        for x in order:
            if x in friend_set:
                arr.append(x)

        return arr