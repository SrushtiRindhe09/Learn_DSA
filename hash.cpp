#include <iostream>
#include <list>
using namespace std;

const int size = 10;
struct Employee
{
 int id;
 string name;
};

class linearhash
{
 private:
         Employee table[size];
         bool occupied[size] = {false};
         
 public:
         int hashFunc(int id)
         {
           return id % size;
         }        
         
         void insert(int id, string name)
         {
           int index = hashFunc(id);
           while (occupied[index])
           {
            index = (index+1) % size;
           }
           table[index] = {id, name};
           occupied[index] = true;
         }
   
   
         void display()
         {
           cout << "\nLinear Probing table:\n";
           for (int i = 0; i < size; i++)
           {
             if (occupied[i])
             {
               cout << i << "-> ID: " << table[i].id << ",Name: " << table[i].name << "\n";
             }
             else 
             {
               cout << i << "-> Empty\n";
             }
           }
         }
};

class Chainhash
{
  private:
         list<Employee> table[size];
         
  public:
         int hashFunc(int id)
         {
           return id % size;
         }       

         void insert( int id, string name)
         {
           int index = hashFunc(id);
           table[index].push_back({id, name});
         }

         void display()
         {
            cout << "\nChaining Table:\n";
            for (int i=0; i < size; i++)
             {
               cout << i << "->"; 
             }
            for (auto emp : table[i])
             {
               cout << "[ID: " << emp.id << "," << emp.name << "] -> ";
             }
            cout << "NULL\n";
         }

};

int main()
{
  linearhash linear;
  Chainhash chain;

  int n, id;
  strig name;
  cout << "\nEnter the Number of Employee\n";
  cin >> n;
  
  for (int i = o; i < n; i++)
  {
    cout << "\nEnter the Id and name of Employee\n";
    cin >> id >> name ;
    linear.insert(id, name);
    linear.insert(id, name);
  }
  
  linear.display();
  chain.display();
  return 0;

}
