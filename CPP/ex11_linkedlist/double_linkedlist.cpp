#include <iostream>
using namespace std;

// https://www.geeksforgeeks.org/doubly-linked-list/
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
    
    void push(Node **head, int data) {
        Node *temp = new Node(data);
        
        temp->next = *head;
        temp->prev = NULL;
        
        if (*head != NULL) {
            (*head)->prev = temp;
        }
        
        *head = temp;
    }
    
    void insertAfter(Node *prev_node, int new_data) {
        if (prev_node == NULL)
            return;
        
        Node *new_node = new Node(new_data);
        Node *next_node = prev_node->next;
        
        new_node->next = next_node;
        new_node->prev = prev_node;
        
        prev_node->next = new_node;
        
        if (next_node->prev != NULL)
            next_node->prev = new_node;
    }
    
    void insertBefore(Node *next_node, int new_data) {
        if (next_node == NULL)
            return;
        
        Node *new_node = new Node(new_data);
        Node *prev_node = next_node->prev;
        
        new_node->next = next_node;
        next_node->prev = new_node;
            
        if (prev_node == NULL) {
            new_node->prev = NULL;
            head = new_node;
            return;
        }
        
        new_node->prev = prev_node;
        prev_node->next = new_node;
    }
    
    void append(Node **head, int new_data) {
        Node *new_node = new Node(new_data);
        
        Node *last = *head;
        
        new_node->next = NULL;
        
        if (*head == NULL) {
            new_node->prev = NULL;            
            *head = new_node;
            return;
        }
        
        while (last->next != NULL) {
            last = last->next;
        }
        Node *prev_node = last->prev;
        
        
        last->next = new_node;
        new_node->prev = last;
        
        return;
    }

    
    void print(Node *list) {
        Node *last = NULL;
        while (list != NULL) {
            cout << list->data << " ";
            last = list;
            list = list->next;
        }
        cout << endl;
        
        while (last != NULL) {
            cout << last->data << " ";
            last = last->prev;
        }
    }
};

int main()
{
    LinkedList ll, dl;
    
    ll.push(&ll.head, 10);
    ll.push(&ll.head, 5);
    ll.push(&ll.head, 23);
    ll.push(&ll.head, 109);
    
    ll.insertAfter(ll.head, 999);
    //ll.print(ll.head);
    ll.append(&ll.head, -1);
    ll.insertBefore(ll.head->next->next, 222);
    ll.print(ll.head);
    
    return 0;
}