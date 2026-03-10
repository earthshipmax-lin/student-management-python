import pandas as pd

#读取学生数据
def load_data():
    return pd.read_csv("../data/students.csv")

#显示所有学生
def show_students(data):
    print("\n学生列表:")
    print(data)

#添加学生
def add_students(data):
    new_id = int(input("输入学生ID:"))
    name = input("输入学生姓名")
    score = float(input("输入学生成绩"))

    new_student = pd.DataFrame({
        "id": [new_id],
        "name": [name],
        "score": [score]
    })

    data = pd.concat([data, new_student], ignore_index=True)
    data.to_csv("../data/students.csv", index=False)

    print("学生添加成功!")

#删除学生
def delete_students(data):
    studnet_id = int(input("输入要删除的学生ID: "))
    data = data[data["id"] != student_id]
    data.to_csv("../data/students.csv", index=False)

    print("学生删除成功!")

#查询学生
def find_students(data):
    student_id = int(input("输入要查询的学生ID "))
    student = data[data["id"] == student_id]

    if student.empty:
        print("没有找到该学生")
    else:
        print(student)

#主菜单
def menu():
    print("\n===== 学生管理系统 =====")
    print("1 查看所有学生")
    print("2 添加学生")
    print("3 删除学生")
    print("4 查询学生")
    print("5 退出")

#主程序
def main():

    while True:

        data = load_data()

        menu()
        choice = input("选择功能: ")

        if choice == "1":
            show_students(data)

        elif choice == "1":
            add_students(data)

        elif choice == "2":
            add_students(data)

        elif choice == "3":
            delete_students(data)

        elif choice == "4":
            find_students(data)

        elif choice == "5":
            print("退出程序")
            break

        else:
            print("输入错误")

if __name__ == "__main__":
    main()