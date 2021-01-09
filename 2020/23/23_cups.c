#include "stdio.h"
#include "stdlib.h"
#include "string.h"


struct Node {
    
    struct Node * next;
    struct Node * prev;
    int data;

};
typedef struct Node Node;


struct CircBuff {
    Node * start;
    Node * end;
    Node * curr;
    int max_data;
};
typedef struct CircBuff CircBuff;



char test[] = "389125467";




void init_cb(CircBuff * cb) {
    cb->start = 0;
    cb->end = 0;
    cb->curr = 0;
    cb->max_data = 0;
}


void append_cb(CircBuff * cb, int data) {

    //printf("append_cb %d\n", data);
    //
    if (data > cb->max_data) {
        cb->max_data = data;
    }
        
    Node * tmp;
    tmp = malloc(sizeof(Node));
    tmp->data = data;
    
    if (cb->curr == 0) {
        
        tmp->next = tmp;
        tmp->prev = tmp;

        cb->curr = tmp;
        cb->end = tmp;
        cb->start = tmp;

    }
    else {
        
        tmp->next = cb->start;
        tmp->prev = cb->end;

        cb->end->next = tmp;
        cb->end = tmp;
    }

}


void print_cb(CircBuff * cb) {

    Node * curr, * last;
    last = cb->start;
    curr = cb->start;

    //printf("max_data: %d\n", cb->max_data);

    if (last != 0) {
        last = cb->start;

        while(curr->next != last) {

            printf("%d ", curr->data);
            curr = curr->next;
        }
        printf("\n");
    }
}


void move(CircBuff * cb) {
    
    Node * start3, * end3, * tmp, * last;
    int curr_data, i, dst, picked;
    int pick_up[3];

    printf("\n");
    print_cb(cb);
    
    start3 = cb->curr->next;
    end3 = start3;
    curr_data = cb->curr->data;

    printf("pick up: ");
    for(i=0; i<3; i++) {
        printf("%d ", end3->data);
        pick_up[i] = end3->data;
        end3 = end3->next;
    }
    printf("\n");
    cb->curr->next = end3;

    dst = 0;
    while (dst == 0) {   
    
        curr_data = (curr_data - 1) % (cb->max_data + 1);
        
        picked = 0;
        for(i=0; i<3; i++) {
            if (curr_data == pick_up[i]) {
                picked = 1;
                break;
            }
        
            if (picked == 0) {
                dst = curr_data;    
            }
        }
    }
    printf("destination: %d\n", dst);
    
    print_cb(cb);

    tmp = cb->curr;
    last = cb->curr;
    while(tmp->next != last) {
        if (tmp->data == dst) {
            break;
        }
        tmp = tmp->next;
    }
    
    Node * old = tmp->prev->next;
    tmp->prev->next = start3;
    start3->prev = tmp;
    end3->next = old;
    
    print_cb(cb);
}






int main(int argc, char * argv[]) {

    CircBuff cb;
    init_cb(&cb);

    int i;
    for (i=0; i<strlen(test); i++) {
        
        char * tmp;
        tmp = strndup(&test[i], 1);
        append_cb(&cb, atoi(tmp));
        free(tmp);
    }

    move(&cb);
    
}
