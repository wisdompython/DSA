// *Definition for singly-linked list.
 function ListNode(val, next) {
    this.val = (val===undefined ? 0 : val)
    this.next = (next===undefined ? null : next)
  }
 
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

var addTwoNumbers = function(l1, l2) {
    let quotient = 0
    let current = new ListNode(0)
    var head = current
    var a = l1 ? l1.val : 0;
    while (l1 || l2 || quotient){

        var v1 = l1 ? l1.val : 0
        var v2 = l2 ? l2.val : 0
        var v3 = v1 + v2 + quotient

        quotient = Math.floor(v3/10)

        current.next = new ListNode(v3 % 10)

        current = current.next

        l1 = l1 ? l1.next: null
        l2 = l2 ? l2.next : null 
    }

    return head.next
};

console.log(addTwoNumbers)