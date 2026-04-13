// https://leetcode.com/problems/merge-k-sorted-lists/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode *mk_node(int val, struct ListNode *nxt) {
    struct ListNode *ret = malloc(sizeof(struct ListNode));
    ret->val = val;
    ret->next = nxt;
    return ret;
}

int get_len(struct ListNode *start) {
    if (!start) {
        return 0;
    }
    int len = 1;
    while (start->next) {
        len++;
        start = start->next;
    }
    return len;
}

int cmp(const void *a, const void *b) {
    assert(a);
    assert(b);
    const int *ia = a;
    const int *ib = b;
    return *ia - *ib;
}

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (!lists || listsSize == 0) {
        return NULL;
    }

    int total = 0;
    for (int i = 0; i < listsSize; i++) {
        total += get_len(lists[i]);
    }

    int *arr = malloc(sizeof(int) * total);
    int idx = 0;
    for (int i = 0; i < listsSize; i++) {
        struct ListNode *cur = lists[i];
        while (cur) {
            arr[idx] = cur->val;
            idx++;
            cur = cur->next;
        }
    }

    qsort(arr, total, sizeof(int), &cmp);
    struct ListNode *filler = mk_node(-1, NULL);
    struct ListNode *cur = filler;
    for (int i = 0; i < total; i++) {
        cur->next = mk_node(arr[i], NULL);
        cur = cur->next;
    }
    struct ListNode *ret = filler->next;
    free(filler);
    return ret;
}

// // less memory but slower
// struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
//     if (!lists || listsSize == 0) {
//         return NULL;
//     }

//     struct ListNode **first = malloc(listsSize * sizeof(struct ListNode *));
//     for (int i = 0; i < listsSize; i++) {
//         first[i] = lists[i];
//     }

//     struct ListNode *filler = mk_node(-1, NULL);  // removed at the end
//     struct ListNode *cur = filler;
//     while (true) {
//         int best = -1;
//         for (int i = 0; i < listsSize; i++) {
//             if (first[i]) {
//                 if (best == -1 || first[i]->val < first[best]->val) {
//                     best = i;
//                 }
//             }
//         }
//         if (best == -1) {
//             break;
//         }
//         cur->next = mk_node(first[best]->val, NULL);
//         cur = cur->next;
//         first[best] = first[best]->next;
//     }
//     struct ListNode *ret = filler->next;
//     free(filler);
//     free(first);
//     return ret;
// }