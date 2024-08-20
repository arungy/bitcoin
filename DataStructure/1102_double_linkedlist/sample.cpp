
#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    Node *prev;
    
    public:
    Node(int d) {
        this->data = d;
        this->next = NULL;
        this->prev = NULL;
    }
};

Node* insert_begin(Node *head, int data)
{
    Node *new_node = new Node(data);

    if (head != NULL) {
        head->prev = new_node;
        new_node->next = head;
    }
    
    return new_node;
}

Node* insert_end(Node *head, int data)
{
    Node *new_node = new Node(data);

    if (head == NULL)
        return new_node;
    
    Node *current = head;
    while (current->next != NULL) {
        current = current->next;
    }
    
    current->next = new_node;
    new_node->prev = current;
    
    return head;
}

Node* delete_head(Node *head)
{
    if (head == NULL)
        return NULL;
    
    Node *node = head;
    head = head->next;
    
    delete node;
 
    if (head) {
        head->prev = NULL;
    }
    
    return head;
}

Node* delete_tail(Node *head)
{
    if (head == NULL)
        return NULL;
    
    Node *current = head, *prev = NULL;
    while (current->next != NULL) {
        current = current->next;
        prev = current->prev;
    }
    
    delete current;
    
    if (prev) {
        prev->next = NULL;
    } else {
        head = prev;
    }

    return head;
}

Node* reverse_list(Node *head)
{
#if 1
    Node *current = head, *prev = NULL;
    while (current != NULL) {
        Node *next = current->next;
        current->next = prev;
        current->prev = next;
        
        prev = current;
        current = next;
    }
        
    return prev;
#else 
    if (head == NULL || head->next == NULL) {
        return head;
    }
    
    Node *current = head, *prev = NULL;
    while (current != NULL) {
        prev = current->prev;
        current->prev = current->next;
        current->next = prev;
        
        current = current->prev;
    }
    
    return prev->prev;
#endif
}

void print_list(Node *list)
{
    while (list != NULL) {
        cout << list->data << " ";
        list = list->next;
    }
    cout << endl;
}

void print_listrev(Node *list)
{
    while (list->next != NULL) {
        list = list->next;
    }
    
    while (list != NULL) {
        cout << list->data << " ";
        list = list->prev;
    }
    cout << endl;
}

int main()
{
    Node *head = NULL;
    
    head = insert_begin(head, 30);
    head = insert_begin(head, 20);
    head = insert_begin(head, 10);
    head = insert_end(head, 40);
    
    print_list(head);
    head = delete_head(head);
    head = delete_tail(head);
  
    //head = reverse_list(head);
    print_list(head);
    
    return 0;
}
