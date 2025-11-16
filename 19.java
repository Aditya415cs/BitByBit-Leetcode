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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode temp=head;
        int len=0;
        while(temp!=null){
            temp=temp.next;
            len=len+1;
        }
        int m=len-n+1;
        if (m == 1) {
            return head.next;
        }
        ListNode temp2=head;
        ListNode prev=null;
        int i=1;
        while(i!=m){
            prev=temp2;
            temp2=temp2.next;
            i=i+1;
        }
        prev.next=temp2.next;
        return head;
    }
}
