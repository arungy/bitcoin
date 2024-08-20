
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
    
    print_list(head);

    return 0;
}
