#include <iostream>
using namespace std;

// https://www.geeksforgeeks.org/reverse-a-doubly-linked-list/

struct Node {
    int data;
    struct Node *next;
    struct Node *prev;
    Node(int data) {
        this->data = data;
        this->next = NULL;
        this->prev = NULL;
    }
};

struct LinkedList {
    Node *head;
    LinkedList() {
        head = NULL;
    }
    
    void reverse(Node **node_ref)
    {
        Node *current = *node_ref;
        Node *next = NULL, *prev = NULL;
        
        while (current != NULL) {
            next = current->next;
            
            current->next = prev;
            current->prev = next;
            
            prev = current;
            current = next;
        }
        *node_ref = prev;
    }
    
    void push(Node **node_ref, int data)
    {
        Node *new_node = new Node(data);
        Node *head_node = *node_ref;
        
        new_node->prev = NULL;
        new_node->next = head_node;
        
        if (head_node != NULL) {
            head_node->prev = new_node;
        }
        *node_ref = new_node; 
    }
    
    void print(Node *list)
    {
        while(list != NULL) {
            cout << list->data << " ";
            list = list->next;
        }
        cout << endl;
    }
};

int main()
{
    LinkedList ll;
    
    ll.push(&ll.head, 10);
    ll.push(&ll.head, 11);
    ll.push(&ll.head, 12);
    ll.print(ll.head);
    ll.reverse(&ll.head);
    ll.print(ll.head);
    
    return 0;
}