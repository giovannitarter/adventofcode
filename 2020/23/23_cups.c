#include "stdio.h"
#include "stdlib.h"
#include "string.h"


struct Node {
    
    struct Node * next;
    //struct Node * prev;
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


#define PART2_NODES_NR 1000000
Node * arr[PART2_NODES_NR];


void init_cb(CircBuff * cb) {
    cb->start = 0;
    cb->end = 0;
    cb->curr = 0;
    cb->max_data = 0;
}


Node * append_cb(CircBuff * cb, int data) {

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
        //tmp->prev = tmp;

        cb->curr = tmp;
        cb->end = tmp;
        cb->start = tmp;

    }
    else {
        
        tmp->next = cb->start;
        //tmp->prev = cb->end;

        cb->end->next = tmp;
        cb->end = tmp;
    }

    return tmp;
}


void print_cb(CircBuff * cb) {

    Node * curr, * last;
    last = cb->curr;
    curr = cb->curr;
    int i;

    //printf("max_data: %d\n", cb->max_data);

    i = 0;
    if (last != 0) {

        while(curr->next != last && i < 20) {

            printf("%d ", curr->data);
            curr = curr->next;
            i++;
        }
        printf("%d ", curr->data);
        printf("\n");
    }
}


int mod(int a, int b)
{
    int r = a % b;
    return r < 0 ? r + b : r;
}


void move(CircBuff * cb) {
    
    Node * start3, * end3, * tmp, * last;
    int curr_data, i, dst, picked;
    int pick_up[3];

    //printf("\n");
    
    curr_data = cb->curr->data;
    //printf("curr: %d\n", curr_data);
    //print_cb(cb);
    
    start3 = cb->curr->next;
    end3 = start3;

    //printf("pick up: ");
    for(i=0; i<3; i++) {
        //printf("%d ", end3->data);
        pick_up[i] = end3->data;
        last = end3;
        end3 = end3->next;
    }
    //printf("\n");
    cb->curr->next = end3;
    
    end3 = last;

    dst = 0;
    while (dst == 0) {   
    
        curr_data = mod((curr_data - 1), (cb->max_data + 1));
        //printf("curr_data: %d\n", curr_data);
        
        picked = 0;
        for(i=0; i<3; i++) {
            if (curr_data == pick_up[i]) {
                picked = 1;
                break;
            }
        }
        
        if (picked == 0) {
            dst = curr_data;    
        }
    }
    //printf("destination: %d\n", dst);
    
    //print_cb(cb);

    //tmp = cb->curr;
    //last = cb->curr;
    //while(tmp->next != last) {
    //    if (tmp->data == dst) {
    //        break;
    //    }
    //    tmp = tmp->next;
    //}
    tmp = arr[dst];
    
    end3->next = tmp->next;
    tmp->next = start3;


    //printf("curr: %d\n", cb->curr->data);
    cb->curr = cb->curr->next;
    //printf("curr: %d\n", cb->curr->data);

    //start3->prev = tmp;
    //end3->next = old;
    
    //print_cb(cb);
}


void print_final(CircBuff * cb) {

    Node * curr, * last;
    curr = cb->curr;
    last = cb->curr;

    while(curr->next != last) {
        if (curr->data == 1) {
            break;
        }
        curr = curr->next;
    }


    last = curr;
    curr = curr->next;

    while(curr->next != last) {
        printf("%d", curr->data);
        curr = curr->next;
    }
    printf("%d ", curr->data);
    printf("\n");
}


void print_final2(CircBuff * cb) {

    Node * curr, * last;
    curr = cb->curr;
    last = cb->curr;
    long a, b, res;

    //while(curr->next != last) {
    //    if (curr->data == 1) {
    //        break;
    //    }
    //    curr = curr->next;
    //}
    //
    curr = arr[1];

    curr = curr->next;
    printf("data1: %d\n", curr->data);
    a = curr->data;
    
    curr = curr->next;
    printf("data2: %d\n", curr->data);
    b = curr->data;

    res = a * b;

    printf("sol2: %lu\n", res);

}





int main(int argc, char * argv[]) {

    CircBuff cb, cb2;
    init_cb(&cb);

    char test[] = "389125467";
    char input[] = "942387615";

    char * arg;
    arg = input;
    //arg = test;

    int i;
    for (i=0; i<strlen(arg); i++) {
        
        char * tmp;
        int n;
        tmp = strndup(&arg[i], 1);
        n = atoi(tmp);
        arr[n] = append_cb(&cb, n);
        free(tmp);
    }

    for (i=1; i<=100; i++) {
        //printf("\n-- move %d --\n", i);
        move(&cb);
    }
    
    printf("\nfinal move:\n");
    print_final(&cb);

    init_cb(&cb2);
    char * tmp;
    int n; 
    for (i=0; i<strlen(arg); i++) {    
        tmp = strndup(&arg[i], 1);
        n = atoi(tmp);
        arr[n] = append_cb(&cb2, n);
        free(tmp);
    }
    
    for (i=cb2.max_data+1; i<=PART2_NODES_NR; i++) {
        arr[i] = append_cb(&cb2, i);
    }
    
    printf("start\n");
    for (i=1; i<=10000000; i++) {
        
        //printf("\n-- move %d --\n", i);
        //print_cb(&cb2);

        if (i % 10000 == 0) {
            printf("%d\n", i);
        }
                
        move(&cb2);
    }
    
    printf("\nfinal move:\n");
    print_final2(&cb);
    
}
