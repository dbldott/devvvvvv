
#include <fstream>
#include <cstring>
#include <iostream>



int main(int argc, char** argv)
{
    if(argc != 3)
    {
        return 0;
    }
    
    std::ifstream file(argv[2]);
    if(!file.is_open())
    {
        return 0;
    }
    
    int N;
    file >> N;
    
    if(N <= 0)
    {
        file.close();
        return 0;
    }
    
    int *NOMINAL = new int[N];
    int *AMMOUNT = new int[N];
    
    for(int i = 0; i < N; ++i)
    {
        file >> NOMINAL[i];
    }
    for(int i = 0; i < N; ++i)
    {
        file >> AMMOUNT[i];
    }
    
    file.close();
    

    int value = atoi(argv[1]);
    
    if(value <= 0)
    {
        delete [] NOMINAL;
        delete [] AMMOUNT;
        return 0;
    }
    
    
    int* F = new int[value + 1];
    int** AMMOUNT_STEP = new int*[value + 1];
    for(int i = 0; i <= value; ++i)
    {
        AMMOUNT_STEP[i] = new int[N];
        for(int j = 0; j < N; ++j)
        {
            AMMOUNT_STEP[i][j] = AMMOUNT[j];
        }
    }
    const int INF = 1000000000;
    F[0] = 0;
    for(int i = 0; i < N; ++i)
    {
        if( value >= NOMINAL[i])
        {
            F[NOMINAL[i]] = 1;
            AMMOUNT_STEP[NOMINAL[i]][i]--;
        }
    }
    
    for(int m = 1; m <= value; ++m)
    {
        F[m] = INF;
        int index = -1;
        for(int i = 0; i < N; ++i)
        {
            if(m >= NOMINAL[i] && F[m - NOMINAL[i]] + 1 < F[m] && AMMOUNT_STEP[m - NOMINAL[i]][i] > 0)
            {
                F[m] = F[m - NOMINAL[i]] + 1;
                index = i;
            }
        }
        
        if(index != -1)
        {
            for(int i = 0; i < N; ++i)
            {
                AMMOUNT_STEP[m][i] = AMMOUNT_STEP[m - NOMINAL[index]][i];
            }
            --AMMOUNT_STEP[m][index];
        }
        
        
    }
    
    
    bool flag = (F[value] >= INF);
    
    if(flag)
    {
        std::ofstream file;
        file.open(argv[2], std::ios::app);
        file << "\nIMPOSSIBLE";
    }else{
        
        std::ofstream file;
        file.open(argv[2], std::ios::app);
        file.put('\n');
        for(int i = 0; i < N-1; ++i)
        {
            file << AMMOUNT[i] - AMMOUNT_STEP[value][i] << " ";
        }
        file << AMMOUNT[N-1] - AMMOUNT_STEP[value][N-1];
    }
    
    
    
    delete [] NOMINAL;
    delete [] AMMOUNT;
    delete [] F;
    
    for(int i = 0; i <= value; ++i)
    {
        delete [] AMMOUNT_STEP[i];
    }
    delete [] AMMOUNT_STEP;
}
