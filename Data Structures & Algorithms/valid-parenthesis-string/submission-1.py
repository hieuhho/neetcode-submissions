class Solution:
    def checkValidString(self, s: str) -> bool:
        left = []
        star = []

        for i, p in enumerate(s):
            # add ( and * to stack
            if p == "(":
                left.append(i)
            elif p == "*":
                star.append(i)
            else:
                # when encountering ):
                # if there is not open or *: is auto invalid
                if not left and not star:
                    return False
                # else pop a left to close ()
                if left:
                    left.pop()
                # else pop a * to close ()
                else:
                    star.pop()
                # this should close out all (), ) should no longer exists

        # if there's any remaining
        # the star is then = ), and should appear AFTER (
        while left and star:
            if left.pop() > star.pop():
                return False
        
        # left should be empty
        return not left
