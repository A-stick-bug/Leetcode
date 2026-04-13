// https://leetcode.com/problems/reverse-nodes-in-k-group/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *kth(struct ListNode *cur, int k) {
    if (!cur) {
        return NULL;
    }
    for (int i = 0; i < k; i++) {
        if (!cur->next) {
            return NULL;
        }
        cur = cur->next;
    }
    return cur;
}

struct ListNode *mk_node(int val, struct ListNode *nxt) {
    struct ListNode *res = malloc(sizeof(struct ListNode));
    res->val = val;
    res->next = nxt;
    return res;
}

struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    assert(head);
    if (k == 1) {
        return head;
    }

    struct ListNode *root = mk_node(-1, head);
    struct ListNode *cur = root;
    while (true) {
        struct ListNode *last = kth(cur, k);
        if (!last) {
            break;
        }
        struct ListNode *prev = last->next;
        struct ListNode *it = cur->next;
        struct ListNode *first = it;
        for (int i = 0; i < k; i++) {
            struct ListNode *nxt = it->next;
            it->next = prev;
            prev = it;
            it = nxt;
        }
        cur->next = last;
        cur = first;
    }

    struct ListNode *ret = root->next;
    free(root);
    return ret;
}