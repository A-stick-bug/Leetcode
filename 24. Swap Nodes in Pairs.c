// https://leetcode.com/problems/swap-nodes-in-pairs/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if (!head) {
        return NULL;
    }
    struct ListNode *root = malloc(sizeof(struct ListNode));
    root->val = -1;
    root->next = head;
    struct ListNode *cur = root;
    while (cur && cur->next && cur->next->next) {
        struct ListNode *temp = cur->next;
        cur->next = cur->next->next;
        temp->next = cur->next->next;
        cur->next->next = temp;

        cur = cur->next->next;
    }
    struct ListNode *ret = root->next;
    free(root);
    return ret;
}
