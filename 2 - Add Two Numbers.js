/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
    // 98ms beats 30,41%
    let carry = 0
    let sum = 0

    let result = new ListNode(0)
    let root = result

    while(l1 || l2 || carry > 0) {
        sum = carry
        carry = 0
        if(l1) {
            sum += l1.val
            l1 = l1.next
        }
        if(l2) {
            sum += l2.val
            l2 = l2.next

        }
        if(sum >= 10) {
            sum -= 10
            carry = 1
        }

        result.val = sum

        result.next = l1 || l2 || (carry > 0) ? new ListNode(0) : null
        result = result.next
    }

    return root
        
};
