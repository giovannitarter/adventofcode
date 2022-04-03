#include <iostream>
#include <vector>


using namespace std;


class Range {

    public:
    int start;
    int end;

    Range(int pstart, int pend) {start=pstart; end=pend;};
};


Range parse_data(char * file) {

    FILE * fd;
    char * tmp;
    int read;
    size_t len;
    int s, e;

    Range res = Range(0, 0);    

    fd = fopen(file, "r");
    tmp = NULL;
    
    while((read = getline(&tmp, &len, fd)) != -1) {
        sscanf(tmp, "%d-%d", &s, &e);
        res.start = s;
        res.end = e;
    }
    
    free(tmp);
    fclose(fd);

    return res;

}

int check_pass(int nr) {
    
    int res;
    int dd;
    int curr, last;

    res = 1;
    dd = 0;
    
    last = nr % 10;
    nr = nr / 10;
    while(nr > 0) {

        curr = nr % 10;
        
        if (last < curr) {
            res = 0;
            break;
        }
        else if (last == curr) { 
            dd = 1;
        }

        last = curr;
        nr = nr / 10;
    }

    res = dd && res;
    return res;
}


int check_pass2(int nr) {
    
    int res;
    int curr, last;
    int state;

    res = 0;
    state = 0;
    
    last = nr % 10;
    nr = nr / 10;
    while(nr > 0) {

        curr = nr % 10;

        if (state == 0) {
            //start, last 2 digits were different

            if (curr == last) {
                state = 1;
            }
            else {
                state = 0;
            }
        }
        else if (state == 1) {
            //last 2 digits were equal
            if (curr == last) {
                state = 2;
            }
            else {
                res = 1;
                break;
            }
        }
        else if (state == 2) {
            //last 3 digits were equal
            
            if (curr == last) {
                state = 2;
            }
            else {
                state = 0;
            }
        
        }

        last = curr;
        nr = nr / 10;
    }
    
    //also ok if state is 1 but digits finished
    if (state == 1) {
        res = 1;
    }

    return res;
}


int main(int argc, char * argv[]) {
    
    int sol01, sol02;
    Range data = Range(0, 0);

    if (argc < 2) {
        printf("error!\n");
        exit(1);
    }
    
    data = parse_data(argv[1]);
    printf("data: %d, %d\n", data.start, data.end);

    sol01 = 0;
    sol02 = 0;
        
    for(int i=data.start; i<=data.end; i++) {

        if  (check_pass(i)) {
            sol01 += 1;   
        
            if (check_pass2(i)) {
                sol02 += 1;   
            }
        }

    }

    printf("sol01: %d\n", sol01);
    printf("sol02: %d\n", sol02);
}
