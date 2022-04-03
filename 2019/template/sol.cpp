#include <iostream>
#include <vector>


using namespace std;



vector<int> * parse_data(char * file) {

    FILE * fd;
    char * tmp;
    int read;
    size_t len;
    
    vector<int> * res;
    res = new vector<int>;

    fd = fopen(file, "r");
    tmp = NULL;
    
    while((read = getline(&tmp, &len, fd)) != -1) {
        
        res->push_back();
    }
    
    free(tmp);
    fclose(fd);

    return res;

}


int main(int argc, char * argv[]) {
    
    int sol01, sol02;
    vector<int> * data;

    if (argc < 2) {
        printf("error!\n");
        exit(1);
    }
    
    data = parse_data(argv[1]);



}
