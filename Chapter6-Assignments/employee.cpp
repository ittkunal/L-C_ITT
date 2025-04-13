Class Employee
{

    string name;

    int age;

    float salary;

public:
    string getName();

    void setName(string name);

    int getAge();

    void setAge(int age);

    float getSalary();

    void setSalary(float salary);
};

Employee employee;


// The Employee class is basically more like a data structure that just contains data. 
// It doesn’t actually do anything with that data—it just lets other code get and set the values. 
// Even though it’s technically a class with private variables and all, it’s not really behaving like a proper object. 
// In good object-oriented design, you'd expect the class to have some logic or behavior built in, not just act like a bucket of variables.