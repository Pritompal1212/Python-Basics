#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* createNode(int data) {
    struct Node* n = (struct Node*)malloc(sizeof(struct Node));
    n->data = data;
    n->next = NULL;
    return n;
}

void append(struct Node** head_ref, int new_data) {
    struct Node* new_node = createNode(new_data);
    struct Node* last = *head_ref;

    if (*head_ref == NULL) {
        *head_ref = new_node;
        return;
    }

    while (last->next != NULL) {
        last = last->next;
    }
    last->next = new_node;
}

struct Node* reverse(struct Node* head) {
    struct Node* prev = NULL;
    struct Node* curr = head;
    struct Node* next = NULL;

    while (curr != NULL) {
        next = curr->next;    
        curr->next = prev; 
        prev = curr;       
        curr = next; 
    }
    return prev;
}

struct Node* sumLists(struct Node* l1, struct Node* l2) {
    struct Node* result = NULL;
    int carry = 0;

    while (l1 != NULL || l2 != NULL ||carry) {
        int sum = carry;
        if (l1 != NULL) {
            sum += l1->data;
            l1 = l1->next;
        }
        if (l2 != NULL) {
            sum += l2->data;
            l2 = l2->next;
        } 
        carry = sum / 10;
        append(&result, sum % 10);
    }
    
    return result; 
}

void printList(struct Node* node) {
    while (node != NULL) {
        printf("%d  ", node->data);
        node = node->next;
    }
}

int main()
 {
    struct Node* list1 = NULL;
    struct Node* list2 = NULL;

    append(&list1, 2);
    append(&list1, 4);
    append(&list1, 3);

    append(&list2, 5);
    append(&list2, 6);
    append(&list2, 4);

    list1 = reverse(list1);
    list2 = reverse(list2);

    struct Node* sumList = sumLists(list1, list2);

    printf("Sum List: ");
    printList(sumList);

    
    return 0;
}