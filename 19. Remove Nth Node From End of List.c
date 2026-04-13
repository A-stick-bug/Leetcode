// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    assert(head);

    int back = n - 1;
    struct ListNode *cur = head;
    struct ListNode *start = head;
    for (int i = 0; i < n - 1; i++) {
        head = head->next;
    }
    struct ListNode *prev = NULL;
    while (head->next) {
        head = head->next;
        prev = cur;
        cur = cur->next;
    }
    if (!prev) {
        struct ListNode *ret = cur->next;
        free(cur);
        return ret;
    } else {
        prev->next = cur->next;
        free(cur);
        return start;
    }
}