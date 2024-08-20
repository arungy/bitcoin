

#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    
    public:
    Node(int d) {
        this->data = d;
        this->next = NULL;
    }
};

Node* insert_node(Node *head, int data)
{
    Node *new_node = new Node(data);

    if (head == NULL) {
        return new_node;
    }
    
    if (data < head->data) {
        new_node->next = head;
        return new_node;
    }

    Node *current = head;
    while (current->next != NULL && data > current->next->data) {
        current = current->next;
    }
    new_node->next = current->next;
    current->next = new_node;
    
    return head;
}

Node* remove_group_recursive(Node *head, int k)
{
    if (head == NULL) {
        return NULL;
    }
    
    int cnt = 0;
    Node *curr = head, *prev = NULL;
    while (curr != NULL && cnt < k) {
        Node *next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
        cnt += 1;
    }
    
    if (curr != NULL) {
        head->next = remove_group_recursive(curr, k);
    }
    
    return prev;
}

Node* remove_group(Node *head, int k)
{
    if (head == NULL) {
        return NULL;
    }
    
    Node *curr = head, *prev_head = NULL;
    while (curr != NULL) {
        Node *first = curr, *prev = NULL;
        for (int cnt = 0; cnt < k && curr != NULL; cnt++) {
            Node *next = curr->next;
            curr->next = prev;
            prev = curr;
            curr = next;
        }
        
        if (prev_head == NULL) {
            head = prev;
        } else {
            prev_head->next = prev;
        }
        prev_head = first;
    }
    
    return head;
}

void print_list(Node *head)
{
    if (head == NULL)
        return;
    
    Node *list = head;
    while (list != NULL) {
        cout << list->data << " ";
        list = list->next;
    }
    cout << endl;
}

int main()
{
    Node *head = NULL;
    
    head = insert_node(head, 30);
    head = insert_node(head, 20);
    head = insert_node(head, 25);
    head = insert_node(head, 5);
    head = insert_node(head, 200);
    head = insert_node(head, 150);
    
    head = insert_node(head, 5);
    head = insert_node(head, 200);
    head = insert_node(head, 150);
    
    print_list(head);
    Node *node = remove_group(head, 4);
    print_list(node);

    return 0;
}
