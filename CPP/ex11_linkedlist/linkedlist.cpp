#include <iostream>
using namespace std;

struct Node {
    int data;
    struct Node *next;
    
    Node(int data) {
        this->data = data;
        this->next = NULL;
    }
};

struct LinkedList {
    Node *head;
    LinkedList() {
        head = NULL;
    }
    
    void reverse() {
        Node *current = head;
        
        Node *prev = NULL, *next = NULL;
        while(current != NULL) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }
    
    void push(int data) {
        Node *temp = new Node(data);
        temp->next = head;
        head = temp;
    }
    
    void print() {
        Node *list = head;
        while (list != NULL) {
            cout << list->data << " ";
            list = list->next;
        }
    }
};

int main()
{
    LinkedList ll;
    
    ll.push(10);
    ll.push(5);
    ll.push(23);
    ll.push(109);
    
    ll.print();
    ll.reverse();
    ll.print();
    return 0;
}