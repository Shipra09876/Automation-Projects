from datetime import datetime,timedelta
import time
import pandas as pd
import os

def get_user_details(prompt):
    while True:
        try:
            return datetime.strptime(input(prompt), "%I:%M %p")
        except ValueError:
            print("Enter time in HH:MM AM/PM format ('9:00 AM')")

def get_task_details():
    task=[]

    while True:
        name=input("Enter your Task Name")
        duration=int(input("Enter duration time in (minutes)"))
        priority=input("Enter priority of the task ('high', 'medium', 'low')").capitalize()
        fixed_time=input("Fixed start time? (leave blank if flexible):")

        if fixed_time:
            try: 
                fixed_time=datetime.strptime(fixed_time.strip(), "%I:%M %p").time()
            except:
                print("Invalid time format skipping fixed_time")
                fixed_time=None
        
        else:
            fixed_time=None
        
        task.append({
            "Task Name":name,
            "Duration":duration,
            "Priority":priority,
            "fixed_time":fixed_time
        })

        cont=input("Any other task? (y/n)").lower()
        if cont!='y':
            break
    

    
    df=pd.DataFrame(task)
    df.to_csv('Daily planner/task.csv',index=False)
    print("\nTask is saved into csv files\n",df)

def schedule_task(start_time,end_time):
    # read data from CSV file 
    df=pd.read_csv("Daily planner/task.csv")
    print("csv data",df)

    df['fixed_time']=pd.to_datetime(df['fixed_time'],format='%I:%M %p',errors='coerce').dt.time

    df['Priority']=pd.Categorical(df['Priority'],categories=['High','Medium','Low'],ordered=True)

    df.sort_values(by=['fixed_time','Priority'],inplace=True)

    current_time=start_time
    schedule=[]

    for _ ,row in df[df["fixed_time"].notnull()].iterrows():
        task_time=datetime.combine(datetime.today(),row['fixed_time'])
        print(task_time)

        if task_time>current_time:
            # add break
            schedule.append((current_time.time(),task_time.time(),"Break"))
            current_time=task_time
        
        end_task_time=current_time+timedelta(minutes=row["Duration"])
        if end_task_time<=end_time:
            schedule.append((current_time.time(),end_task_time.time(),row["Task Name"]))
            current_time=end_task_time

            if current_time + timedelta(minutes=5) <= end_time:
                break_end = current_time + timedelta(minutes=5)
                schedule.append((current_time.time(), break_end.time(), "Short Break"))
                current_time = break_end
    
    for _, row in df[df['fixed_time'].isnull()].iterrows():
        if current_time + timedelta(minutes=row['Duration']) > end_time:
            break

        end_task_time = current_time + timedelta(minutes=row['Duration'])
        schedule.append((current_time.time(), end_task_time.time(), row['Task Name']))
        current_time = end_task_time

        # Add 5-minute break after each task
        if current_time + timedelta(minutes=5) <= end_time:
            break_end = current_time + timedelta(minutes=5)
            schedule.append((current_time.time(), break_end.time(), "Short Break"))
            current_time = break_end

    print(schedule)
    return schedule


def show_output(schedule):
    if os.path.exists('output.txt'): 
        print("yes exist")
        with open("Daily planner/output.txt","w") as f:
            for start,end,task in schedule:
                line = f"{start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}: {task}"
                f.write(line+"\n")

    
def main():
    username=input("Enter your name ")
    print(f"Welcome to daily planner {username}")

    start_time=get_user_details("Enter the starting time of work ('9:00 AM') ")
    end_time=get_user_details("Enter the ending time of work ('9:00 AM') ")
    
    get_task_details()

    schedule=schedule_task(start_time,end_time)

    for start,end,task in schedule:
        print(f"{start.strftime('%I:%M %p')} - {end.strftime('%I:%M %p')}: {task}")

    show_output(schedule)

if __name__=="__main__":
    main()