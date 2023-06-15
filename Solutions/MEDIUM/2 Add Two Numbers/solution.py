# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]
 

# Constraints:

# The number of nodes in each linked list is in the range [1, 100].
# 0 <= Node.val <= 9
# It is guaranteed that the list represents a number that does not have leading zeros.

#### SOLUTION #####

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ''
        num2 = ''
        total = ''

        while l1 is not None:
            num1 += str(l1.val)
            l1 = l1.next


        while l2 is not None:
            num2 += str(l2.val)
            l2 = l2.next


        num1 = num1[::-1]
        num2 = num2[::-1]

        total = (int(num1) + int(num2))
        total = str(total)
        total = total[::-1]

        answer = traveler = ListNode()

        for i in range(len(total)):
            traveler.val = total[i]
            if i != len(total) - 1:
                traveler.next = ListNode()
            traveler = traveler.next

        return answer