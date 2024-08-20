#include <iostream>
using namespace std;

struct Node {
    Node *next;
    Node *prev;
    int data;
    bool visited;
    
    Node() {
        this->next = NULL;
        this->prev = NULL;
        this->data = 0;
        this->visited = false;
    }
    
    Node(int value) {
        this->next = NULL;
        this->data = value;
        this->visited = false;
    }
};

Node *insert_node(Node *head, int data)
{
    Node *new_node = new Node(data);
    
    if (head == NULL) {
        return new_node;
    }
    
    head->prev = new_node;
    new_node->next = head;

    return new_node;
}

Node *reverse_list(Node *head)
{
    if (head == NULL) {
        return head;
    }
    
    Node *current = head, *prev = NULL;
    while (current != NULL) {
        Node *next = current->next;
        
        current->next = prev;
        current->prev = next;

        prev = current;
        current = next;
    }
    head = prev;
    
    return head;
}

Node *remove_loop(Node *head)
{
    if (head == NULL) {
        return head;
    }
    
    bool loop = false;
    Node *current = head, *prev = NULL;
    while (current != NULL) {
        if (current->visited == true) {
            loop = true;
            break;
        } 
        current->visited = true;

        prev = current;
        current = current->next;
    }
    if (loop == true) 
        prev->next = NULL;

    return head;
}

//best method
Node *remove_loop2(Node *head)
{
    if (head == NULL) {
        return head;
    }
    
    bool loop = false;
    Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        
        if (slow == fast) {
            loop = true;
            break;
        } 
    }
    
    if (loop == true) {
        slow = head;
        while(slow->next != fast->next) {
            slow = slow->next;
            fast = fast->next;
        }
        fast->next = NULL;
    }

    return head;
}

Node* free_list(Node *head)
{
    if (head == NULL) {
        return head;
    }
    
    do {
        Node *tmp = head;
        head = head->next;
        
        delete tmp;
    } while (head != NULL);
    
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

void print_list_rev(Node *head)
{
    if (head == NULL)
        return;
    
    Node *list = head;
    while (list != NULL && list->next != NULL) {
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
    Node *head = NULL, *temp = NULL;
    
    head = insert_node(head, 15);
    head = insert_node(head, 5);
    head = insert_node(head, 240);
    Node *tmp = head; 
    head = insert_node(head, 3);
    head = insert_node(head, 129);
    head = insert_node(head, 1001);
    head = insert_node(head, -10);
    tmp->next = head;    
    head = insert_node(head, -23);
    head = insert_node(head, -7);
    
    head = remove_loop2(head);
    print_list(head);
    //print_list_rev(head);
    
    //head = reverse_list(head);
    //print_list(head);
    //print_list_rev(head);
    
    head = free_list(head);
   
    return 0;
}
