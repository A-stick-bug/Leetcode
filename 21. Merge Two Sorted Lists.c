// https://leetcode.com/problems/merge-two-sorted-lists/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *mk_node(int val, struct ListNode *nxt) {
    struct ListNode *res = malloc(sizeof(struct ListNode));
    res->val = val;
    res->next = nxt;
    return res;
}

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2) {
    struct ListNode *filler = mk_node(-1, NULL);  // temporary, will be removed at the end

    struct ListNode *cur = filler;
    while (list1 || list2) {
        if (!list1) {
            cur->next = mk_node(list2->val, NULL);
            list2 = list2->next;
        } else if (!list2) {
            cur->next = mk_node(list1->val, NULL);
            list1 = list1->next;
        } else if (list1->val <= list2->val) {
            cur->next = mk_node(list1->val, NULL);
            list1 = list1->next;
        } else {
            cur->next = mk_node(list2->val, NULL);
            list2 = list2->next;
        }
        cur = cur->next;
    }
    struct ListNode *ret = filler->next;
    free(filler);
    return ret;
}
