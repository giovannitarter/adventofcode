#include <iostream>
#include <vector>

using namespace std;

int compute_fuel(int mass) {

    int res, fuel;

    res = 0;
    while(mass > 0) {
        
        fuel = (mass / 3) - 2;

        if (fuel < 0) {
            break;
        }

        res += fuel;
        mass = fuel;
    }

    return res;
}


int sol01(vector<int> * data) {

    int res = 0;

    for(auto i=data->begin(); i != data->end(); ++i) {
        int fuel =  (*i / 3) - 2;

        //printf("mass: %d, fuel: %d\n", *i, fuel);
        res += fuel;
    }

    return res;
}


int sol02(vector<int> * data) {

    int res = 0;

    for(auto i=data->begin(); i != data->end(); ++i) {
        
        int fuel = compute_fuel(*i);
        //printf("mass: %d, fuel: %d\n", *i, fuel);
        res += fuel;
    }

    return res;
}


vector<int> * parse_data(char * file) {
    
    FILE * fd;
    char * tmp;
    int read;
    size_t len;
    
    int mass;
    vector<int> * res;

    res = new vector<int>;

    fd = fopen(file, "r");
    tmp = NULL;
    while((read = getline(&tmp, &len, fd)) != -1) {
        sscanf(tmp, "%d", &mass);
        res->push_back(mass);
    }
    free(tmp);
    fclose(fd);

    return res;
}


int main(int argc, char * argv[]) {
    
    vector<int> * data;

    if (argc < 2) {
        printf("error!\n");
        exit(1);
    }
    
    data = parse_data(argv[1]);
    
    int s01 = sol01(data);
    printf("sol01: %d\n", s01);
    
    int s02 = sol02(data);
    printf("sol02: %d\n", s02);

    delete data;
}
