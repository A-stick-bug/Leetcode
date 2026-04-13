// https://leetcode.com/problems/add-two-numbers/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

#include <stdlib.h>
#include <assert.h>


struct ListNode *mk_node(int val, struct ListNode *nxt) {
    struct ListNode *res = malloc(sizeof(struct ListNode));
    res->val = val;
    res->next = nxt;
    return res;
}

struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    assert(l1);
    assert(l2);

    struct ListNode *res = mk_node((l1->val + l2->val) % 10, NULL);
    int carry = (l1->val + l2->val) / 10;

    l1 = l1->next;
    l2 = l2->next;
    struct ListNode *cur = res;
    while (l1 || l2) {
        if (!l1) {
            int total = l2->val + carry;
            cur->next = mk_node(total % 10, NULL);
            carry = total / 10;
            l2 = l2->next;
        } else if (!l2) {
            int total = l1->val + carry;
            cur->next = mk_node(total % 10, NULL);
            carry = total / 10;
            l1 = l1->next;
        } else {
            int total = l1->val + l2->val + carry;
            cur->next = mk_node(total % 10, NULL);
            carry = total / 10;
            l1 = l1->next;
            l2 = l2->next;
        }
        cur = cur->next;
    }
    if (carry) {
        cur->next = mk_node(1, NULL);
    }
    return res;
}