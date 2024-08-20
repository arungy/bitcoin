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
void delete_node(Node *node)
{
    if (node == NULL) {
        return;
    }
    
    if (node->next != NULL) {
        Node *tmp = node->next;
        node->data = tmp->data;
        node->next = tmp->next;
        delete tmp;
    }
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
    head = insert_node(head, 200);
    head = insert_node(head, 150);
    head = insert_node(head, 5);
    print_list(head);
    delete_node(temp);
    print_list(head);
    

    return 0;
}
