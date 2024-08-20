

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

Node* reverse(Node *head)
{
    if (head == NULL) {
        return NULL;
    }
    
    Node *current = head, *prev = NULL;
    while (current != NULL) {
        Node *next = current->next;
        current->next = prev;
        
        prev = current;
        current = next;
    }
    head = prev;
    
    return head;
}

Node* reverse_recursive2(Node *curr, Node *prev)
{
    if (curr == NULL) {
        return prev;
    }

    Node *next = curr->next;
    curr->next = prev;
    
    return reverse_recursive2(next, curr);
}

Node* reverse_recursive(Node *head)
{
    return reverse_recursive2(head, NULL);
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
    Node *node = reverse_recursive(head);
    print_list(node);

    return 0;
}
