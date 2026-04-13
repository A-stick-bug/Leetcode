// https://leetcode.com/problems/rotate-list/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int len(struct ListNode *start) {
    if (!start) {
        return 0;
    }
    int len = 1;
    while(start->next) {
        len++;
        start = start->next;
    }
    return len;
}


struct ListNode* rotateRight(struct ListNode* head, int k) {
    if (!head || !head->next) {
        return head;
    }
    int n = len(head);
    k %= n;

    if (k == 0) {
        return head;
    }

    struct ListNode *last = head;
    // get last and k-th from the end
    for (int i = 0; i < n - 1; i++) {
        last = last->next;
    }
    struct ListNode *kth = head;
    for (int i = 0; i < n - k - 1; i++) {
        kth = kth->next;
    }

    last->next = head;
    struct ListNode *ret = kth->next;
    kth->next = NULL;
    return ret;
}