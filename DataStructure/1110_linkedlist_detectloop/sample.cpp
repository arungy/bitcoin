

#include <iostream>
using namespace std;

struct Node
{
    int data;
    Node *next;
    bool visited;
    
    public:
    Node(int d) {
        this->data = d;
        this->next = NULL;
        this->visited = false;
    }
};

Node* insert_node(Node *head, int data)
{
    Node *new_node = new Node(data);

    if (head == NULL) {
        return new_node;
    }
    
    new_node->next = head;
    
    return new_node;
}

bool detect_loop_method2(Node *head)
{
    if (head == NULL) {
        return NULL;
    }
   
    Node *current = head;
    while (current != NULL) {
        if (current->visited == true) {
            return true;
        }
        current->visited = true;
        current = current->next;
    }
    
    return false;
}

bool detect_loop_method3(Node *head)
{
    if (head == NULL) {
        return NULL;
    }
    
    Node *temp = new Node(0);
    
    Node *current = head;
    while (current != NULL) {
        if (current->next == NULL) {
            return false;
        }
        
        if (current->next == temp) {
            return true;
        }
        Node *next = current->next;
         current->next = temp;
        current = next;
    }
    
    return false;
}

//best method
bool detect_loop_floyd(Node *head)
{
    if (head == NULL) {
        return NULL;
    }
    
    Node *slow = head, *fast = head;
    while (fast != NULL && fast->next != NULL) {
        slow = slow->next;
        fast = fast->next->next;
        if (slow == fast) {
            return true;
        }
    }
    
    return false;
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
    Node *head = NULL, *temp = NULL;
    
    head = insert_node(head, 30);
    head = insert_node(head, 20);
    temp = head = insert_node(head, 25);
    head = insert_node(head, 5);
    head = insert_node(head, 200);
    head = insert_node(head, 150);
    temp->next = head;
    
    head = insert_node(head, 5);
    head = insert_node(head, 200);
    head = insert_node(head, 150);
    
    cout << "Is loop detected for this linked list: " << (true == detect_loop_floyd(head) ? "Yes" : "No") << endl;
    //print_list(head);
    //Node *node = remove_group(head, 4);
    //print_list(node);

    return 0;
}
