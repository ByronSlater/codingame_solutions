#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

struct Point
{
    int x, y;
};

enum Direction
{
    UP, DOWN, LEFT, RIGHT
};

class Map
{
public:
    int width;
    int height;
    Point location;
    vector<string> grid;
    int length;
    Direction d;

    Map(vector<string> lines, int x, int y)
    {
        height = lines.size();
        width = lines[0].size();
        grid = lines;
        location = {x, y};
    }

    void run()
    {
        length = 0;
        bool finished = false;

        while(!finished)
        {
            length++;
            if(length == height * width + 1
               || location.x >= height || location.y >= width
               || location.x < 0 || location.y < 0) 

            {
                cerr << location.x << ", " << location.y << endl;
                cerr << "exiting here" << endl;
                length = height * width + 1;
                return;
            }

            char here = grid[location.x][location.y];
            cerr << "(" << location.x << ", " << location.y << ")" << endl;
            cerr << here << endl;
            switch(here)
            {
                case '^':
                    d = UP;
                    break;
                
                case '>':
                    d = RIGHT;
                    break;

                case '<':
                    d = LEFT;
                    break;

                case 'v':
                    d = DOWN;
                    break;

                case 'T':
                    finished = true;
                    break;

                case '#':
                    length = height * width + 1;
                    finished = true;
                    break;
                
                case '.':
                    break;

            }
            if(!finished)
            {
                switch(d)
                {
                    case UP:
                        location.x--;
                        break;
                    case DOWN:
                        location.x++;
                        break;
                    case LEFT:
                        location.y--;
                        break;
                    case RIGHT:
                        location.y++;
                        break;
                }
            }
        }

    }

    friend ostream& operator << (ostream& out, const Map& m)
    {
        for(auto l : m.grid)
        {
            out << l << endl;
        }

        return out;
    }
};

int main()
{
    int w, h, startRow, startCol, n, min, bestIndex{-1};
    cin >> w >> h; cin.ignore();
    cin >> startRow >> startCol; cin.ignore();
    cin >> n; cin.ignore();

    vector<Map> maps;

    min = w * h + 1;

    for (int i = 0; i < n; i++) 
    {
        vector<string> lines;
        for (int j = 0; j < h; j++)
        {
            string mapRow;
            getline(cin, mapRow);
            lines.push_back(mapRow);
        }
        Map m{lines, startRow, startCol};

        cerr << m << endl;
        m.run();
        cerr << "length was: " << m.length << endl;
        cerr << "min is: " << min << endl;
        if(m.length < min) 
        {
            cerr << "we in here" << endl;
            bestIndex = i;
            min = m.length;
        }

    }
    
    if(bestIndex == -1)
    {
        cout << "TRAP" << endl;
    }
    else
    {
        cout << bestIndex << endl;
    }
}