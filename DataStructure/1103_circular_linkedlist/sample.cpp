
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

    if (head == NULL) {
        new_node->next = new_node;
        return new_node;
    } else {
#if 0
        Node *current = head;
        while(current->next != head) {
            current = current->next;
        }
        current->next = new_node;
        new_node->next = head;
        
        return new_node;
#else
        new_node->next = head->next;
        head->next = new_node;
        int val = head->data;
        head->data = new_node->data;
        new_node->data = val;
        
        return head;
#endif        
    }
}

Node* insert_end(Node *head, int data)
{
    Node *new_node = new Node(data);

    if (head == NULL) {
        new_node->next = new_node;
        return new_node;
        
    } else {
#if 0
        Node *current = head;
        while(current->next != head) {
            current = current->next;
        }
        current->next = new_node;
        new_node->next = head;
        
        return head;
#else
        new_node->next = head->next;
        head->next = new_node;
        int val = head->data;
        head->data = new_node->data;
        new_node->data = val;
        
        head = head->next;
        
        return head;
#endif
    }
}

Node* delete_head(Node *head)
{
    if (head == NULL) {
        return NULL;
    } else if (head->next == head) {
        delete head;
        return NULL;
    } 
    
    {
        Node *tmp = head->next;
        
        head->data = tmp->data;
        head->next = tmp->next;
        
        delete tmp;
        
        return head;
    }
}

Node* delete_node(Node *head, int k)
{
    if (head == NULL || k < 1) {
        return NULL;
    } 
    
    if (k == 1) {
        return delete_head(head);
    } 
    
    /*
    Node *list = head;
    for (int pos = 1; ((pos < (k - 1)) && (list->next != head)); pos++) {
        list = list->next;
    }
    if (list->next != head) {
        Node *tmp = list->next;
        list->next = tmp->next;
    
        delete tmp;
    }
    */
    Node *curr = head;
    for (int p = 0; p < (k - 2); p++) {
        curr = curr->next;
    }
    Node *tmp = curr->next;
    curr->next = tmp->next;
    
    delete tmp;
    
    return head;
}

void print_list(Node *head)
{
    if (head == NULL)
        return;
    
    Node *list = head;
    do {
        cout << list->data << " ";
        list = list->next;
    } while (list != head);
    cout << endl;
}

int main()
{
    Node *head = NULL;
    
    head = insert_begin(head, 30);
    head = insert_begin(head, 20);
    head = insert_begin(head, 10);
    
    head = insert_end(head, 35);
    head = insert_end(head, 45);
    
    print_list(head);
    //head = delete_head(head);
    head = delete_node(head, 1);
    
    print_list(head);

    return 0;
}
