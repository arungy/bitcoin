
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

Node* insert_begin(Node *head, int data)
{
    Node *new_node = new Node(data);
    new_node->next = head;
    
    if (head == NULL) {
        new_node->next = NULL;
    }
    
    return new_node;
}

Node* insert_end(Node *head, int data)
{
    Node *new_node = new Node(data);
    
    if (head == NULL)
        return new_node;
        
    Node *current = head;
    while (current->next != NULL)
        current = current->next;
    
    current->next = new_node;
    
    return head;
}

Node* insert_position(Node *head, int data, int pos)
{
    Node *new_node = new Node(data);
    if (pos == 1 ) {
        new_node->next = head;
        return new_node;
    }
    
    Node *current = head;
    for (int i = 1; i <= (pos - 2) && (current != NULL); i++) {
        current = current->next;
    }
    
    if (current == NULL) {
        return head;
    }
    
    new_node->next = current->next;
    current->next = new_node;
    
    return head;
}

int search_key(Node *head, int key)
{
    Node *current = head;
    for (int i = 1; current != NULL; i++) {
        if (current->data == key) {
            return i;
        }
        current = current->next;
    }
            
    return -1;    
}

int search_key_recursive(Node *head, int key)
{
    if (head == NULL) {
        return -1;
    }
    
    if (head->data == key)
        return 1;
    
    int ret = search_key_recursive(head->next, key);

    return  ret < 0 ? -1 : ret + 1;    
}

Node* delete_head(Node *head)
{
    if (head != NULL) {
        Node *current = head;
        head = current->next;
        delete current;
    }
    
    return head;
}

Node* delete_tail(Node *head)
{
    if (head == NULL)
        return head;
        
    Node *current = head, *prev = NULL;
    while (current->next != NULL) {
        prev = current;
        current = current->next;
    }
    
    delete current;
    if (prev == NULL) {
        head = NULL;
    } else {
        prev->next = NULL;
    } 
    
    return head;
}

Node* freelist(Node *head)
{
    Node *current = head, *next = NULL;
    
    while(current != NULL) {
        next = current->next;
        delete current;
        
        current = next;
    }
    
    return current;
}

void print(Node *list) 
{
    while(list != NULL) {
        cout << list->data << endl;
        list = list->next;
    }
}

void print_recursive(Node *list) 
{
    if (list == NULL) {
        cout << endl;
        return;
    }
    
    cout << list->data << " ";
    print_recursive(list->next);
}

int main()
{
    Node *head = NULL;
    
    head = insert_begin(head, 30);
    head = insert_begin(head, 20);
    head = insert_begin(head, 10);
    head = insert_begin(head, 5);
    
    head = insert_end(head, 100);
    
    print_recursive(head);
    
    //head = delete_head(head);
    head = delete_tail(head);
    print_recursive(head);
    
    head = insert_position(head, 15, 5);
    print_recursive(head);
    
    cout << search_key_recursive(head, 20) << endl;
    
    head = freelist(head);
        
    return 0;
}
