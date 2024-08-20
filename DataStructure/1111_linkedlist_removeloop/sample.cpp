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

//best method
bool remove_loop(Node *head)
{
    if (head == NULL) {
        return NULL;
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
        while (fast->next != slow->next) {
            slow = slow->next;
            fast = fast->next;
        }
        fast->next = NULL;
    }
    
    return loop;
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
    
    cout << "Is loop detected for this linked list: " << (true == remove_loop(head) ? "Yes" : "No") << endl;
    print_list(head);

    return 0;
}
