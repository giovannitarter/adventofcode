#include <iostream>
#include <vector>
#include <cstring>


using namespace std;


class CompInt {

    public:
        CompInt(vector<int> * inst);
        ~CompInt();
        int run();
        int get_mem(int idx) {return (*mem).at(idx);};
        void set_mem(int idx, int val) {(*mem)[idx] = val;};

    private:
        int curr_inst;
        vector<int> * mem;
};


CompInt::CompInt(vector<int> * inst) {

    mem = new vector<int>(inst->size());

    for(int i=0; i<inst->size(); i++) {
        (*mem)[i] = inst->at(i);
    }

    curr_inst = 0;
}


CompInt::~CompInt() {
    delete(mem);
}


int CompInt::run() {

    int res = 1;
    int opc, op1, op2, op3;

    while(mem->at(curr_inst) != 99) {

        opc = mem->at(curr_inst);
        op1 = mem->at(curr_inst + 1);
        op2 = mem->at(curr_inst + 2);
        op3 = mem->at(curr_inst + 3);

        switch(opc) {
        
            case 1:
                (*mem)[op3] = mem->at(op1) + mem->at(op2);
                break;
            
            case 2:
                (*mem)[op3] = mem->at(op1) * mem->at(op2);
                break;

            default:
                break;

        }

        curr_inst = curr_inst + 4;
    }

    return res;
}


vector<int> * parse_data(char * file) {

    FILE * fd;
    char * line;
    int read, inst;
    size_t len;

    char * field;
    
    vector<int> * res;
    res = new vector<int>;

    line = NULL;
    fd = fopen(file, "r");
    
    while((read = getline(&line, &len, fd)) != -1) {

        field = strtok(line, ",");
        while (field != NULL) {

            sscanf(field, "%d", &inst);
            res->push_back(inst);

            field = strtok(NULL, ",");
        }
    }
    
    free(line);
    fclose(fd);

    return res;

}


int test_pair(int p1, int p2, vector<int> * data) {
    
    int res;
    CompInt * ci;

    ci = new CompInt(data);
    ci->set_mem(1, p1);
    ci->set_mem(2, p2);
    ci->run();
    res = ci->get_mem(0);
    delete(ci);

    return res;
}


int main(int argc, char * argv[]) {
    
    vector<int> * data;
    CompInt * ci; 
    int sol01, sol02;

    if (argc < 2) {
        printf("error!\n");
        exit(1);
    }
    
    data = parse_data(argv[1]);

    sol01 = test_pair(12, 2, data);

    
    printf("sol01: %d\n", sol01);


    for(int i=0; i<100; i++) {
        for(int j=0; j<100; j++) {
            
            int val = test_pair(i, j, data);
            if (val == 19690720) {
                sol02 = 100 * i + j;
            }

        }
    }

    printf("sol02: %d\n", sol02);
}
