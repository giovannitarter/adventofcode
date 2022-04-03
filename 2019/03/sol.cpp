#include <iostream>
#include <vector>
#include <cstring>
#include <limits>

using namespace std;


class Point {
    
    public:
        int x, y;
        Point(int px, int py) {x=px; y=py;};
        Point() {x=0; y=0;};
};


class Segment {


    public:
    
    Point p0;
    Point p1;
    Point orig;
    
    int dist;

    Segment(Point pp0, Point pp1, int pdist);
};



Segment::Segment(Point pp0, Point pp1, int pdist) {


    p0 = pp0;
    orig = pp0;

    p1 = pp1;

    dist = pdist;

    int tmp;
    if (p0.x > p1.x) {
        tmp = p0.x;
        p0.x = p1.x;
        p1.x = tmp;
    }
    
    if (p0.y > p1.y) {
        tmp = p0.y;
        p0.y = p1.y;
        p1.y = tmp;
    }

}


vector<Segment *> parse_line(char * line) {
    
    vector<Segment *> res;
    
    char * dir;
    Segment * newseg;
    
    char d;
    int len;
    int clen;
    
    Point curr = Point(0, 0);
    Point last = Point(0, 0);

    clen = 0;
    dir = strtok(line, ",");
    while(dir != NULL) {
    
        sscanf(dir, "%c%d", &d, &len);

        switch(d) {

            case 'R':
                curr.x = curr.x + len;
                break;
            
            case 'L':
                curr.x = curr.x - len;
                break;
            
            case 'U':
                curr.y = curr.y + len;
                break;
            
            case 'D':
                curr.y = curr.y - len;
                break;
        }


        newseg = new Segment(last, curr, clen);
        res.push_back(newseg);

        clen += len;
        last = curr;
        dir = strtok(NULL, ",");
    }

    return res;
}


void parse_data(char * file, vector<Segment *> res[]) {

    FILE * fd;
    char * tmp;
    int read;
    size_t len;
    int i;
    
    fd = fopen(file, "r");
    tmp = NULL;

    read = getline(&tmp, &len, fd);
    res[0] = parse_line(tmp);
    
    read = getline(&tmp, &len, fd);
    res[1] = parse_line(tmp);
    
    free(tmp);
    fclose(fd);

}


Point * intersect(Segment * a, Segment * b) {


    Point * res;

    if (a->p0.x < b->p0.x && b->p0.x < a->p1.x && b->p0.y < a->p0.y && a->p0.y < b->p1.y) 
    {
        res = new Point(b->p0.x, a->p0.y);
    }
    else if (b->p0.x < a->p0.x && a->p0.x < b->p1.x && a->p0.y < b->p0.y && b->p0.y < a->p1.y) 
    {
        res = new Point(a->p0.x, b->p0.y);
    }
    else {
        res = NULL;
    }

    return res;
}


int manhattan_dist(Point p0, Point p1) {
    int res = abs(p1.x-p0.x) + abs(p1.y-p0.y);
    return res;
}


int main(int argc, char * argv[]) {
    
    int sol01, sol02;
    
    vector<Segment *> data[2];

    if (argc < 2) {
        printf("error!\n");
        exit(1);
    }
    
    parse_data(argv[1], data);

    int dist, dist02;
    
    sol01 = std::numeric_limits<int>::max();
    
    Segment *ci, *cj; 
    for (int i=0; i<data[0].size(); i++) {
            
        ci = data[0].at(i);
        for (int j=0; j<data[1].size(); j++) {

            cj = data[1].at(j);
            Point * p = intersect(ci, cj);
            if (p) {

                dist = manhattan_dist(*p, Point());
                if (dist < sol01) {
                    sol01 = dist;
                }

            }
       }
     }

    printf("sol01: %d\n", sol01);
    
    sol02 = std::numeric_limits<int>::max();
    for (int i=0; i<data[0].size(); i++) {
            
        ci = data[0].at(i);
        for (int j=0; j<data[1].size(); j++) {

            cj = data[1].at(j);
            Point * p = intersect(ci, cj);
            if (p) {

                //printf("\n");
                //printf("dist1: %d\n", ci->dist);
                //printf("orig1: x:%d y:%d\n", ci->orig.x, ci->orig.y);
                //printf("rem: %d\n", manhattan_dist(p->x, p->y, ci->orig.x, ci->orig.y));

                //printf("dist2: %d\n", cj->dist);
                //printf("orig2: x:%d y:%d\n", cj->orig.x, cj->orig.y);
                //printf("rem: %d\n", manhattan_dist(p->x, p->y, cj->orig.x, cj->orig.y));

                //printf("intersect: x:%d y:%d\n", p->x, p->y);
                dist = ci->dist + cj->dist 
                    + manhattan_dist(*p, ci->orig) 
                    + manhattan_dist(*p, cj->orig);

                //printf("dist: %d\n", dist);

                if (dist < sol02) {
                    sol02 = dist;
                }
            }
       }
    }
    printf("sol02: %d\n", sol02);
}
