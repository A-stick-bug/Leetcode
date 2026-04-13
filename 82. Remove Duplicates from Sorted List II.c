// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *root = malloc(sizeof(struct ListNode));
    root->val = 0;
    root->next = head;

    struct ListNode *cur = root;
    while (cur && cur->next) {
        int val = cur->next->val;
        if (!cur->next->next) {
            break;
        }
        if (cur->next->next->val == val) {  // skip
            while (cur->next && cur->next->val == val) {
                struct ListNode *rem = cur->next;
                cur->next = cur->next->next;
                free(rem);
            }
        } else {  // keep
            cur = cur->next;
        }
    }
    struct ListNode *ret = root->next;
    free(root);
    return ret;
}
