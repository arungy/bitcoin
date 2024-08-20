

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

Node* find_nthnode_end(Node *head, int n)
{
    if (head == NULL) {
        return NULL;
    }
    
    Node *first = head;
    for (int i = 0; i < n; i++) {
        first = first->next;
        if (first == NULL) {
            return NULL;
        }
    }
    
    Node *second = head;
    for (; first != NULL; first = first->next) {
        second = second->next;
    }
    
    return second;
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
    
    print_list(head);
    Node *node = find_nthnode_end(head, 2);
    print_list(node);

    return 0;
}
