def to_do_list():
    tasks = []
    completed_tasks = []

    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Show Tasks")
        print("4. Exit")
        choose = int(input("Enter the tasks: "))
        if choose == 1:
            task = input("Enter task: ")
            tasks.append(task)
        elif choose == 2:
            if task in tasks:
                tasks.remove(task)
            else:
                print("no task found")
        elif choose == 3:
            for task in tasks:
                print(tasks)
        elif choose == 4:
            break
        else:
            print("no such a task")
        comp_task = input("Enter completed task: ")
        completed_tasks.append(comp_task)
        print(completed_tasks)
        
to_do_list()
            
