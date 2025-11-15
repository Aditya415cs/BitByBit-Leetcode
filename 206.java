/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode now=head;
        ListNode prev=null;
        while(now!=null){
            ListNode next=now.next;
            now.next=prev;
            prev=now;
            now=next;
        }
        return prev;
    }

}
