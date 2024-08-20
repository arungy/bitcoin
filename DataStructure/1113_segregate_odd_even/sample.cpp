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
Node* segegrate_odd_even(Node *head)
{
    if (head == NULL) {
        return NULL;
    }
    
    Node *eS = NULL, *eE = NULL, *oS = NULL, *oE = NULL;
    for(Node *curr = head; curr != NULL; curr = curr->next) {
        if (curr->data %2 == 0) {
            if (eS == NULL && eE == NULL) {
                eS = eE = curr;
            } else {
                eE->next = curr;
                eE = eE->next;
            }
        } else {
            if (oS == NULL && oE == NULL) {
                oS = oE = curr;
            } else {
                oE->next = curr;
                oE = oE->next;
            }
        }
    }
    
    eE->next = oS;
    oE->next = NULL;
    
    return eS;
    
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
     head = insert_node(head, 15);
    head = insert_node(head, 150);
    head = insert_node(head, 5);
    print_list(head);
    head = segegrate_odd_even(head);
    print_list(head);
    

    return 0;
}
