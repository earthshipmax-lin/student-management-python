import manager
import utils

def main():

    while True:

        data = manager.load_data()

        utils.menu()

        choice = input("选择功能: ")

        if choice == "1":
            manager.show_students(data)

        elif choice == "2":
            manager.add_student(data)

        elif choice == "3":
            manager.delete_student(data)

        elif choice == "4":
            manager.find_student(data)

        elif choice == "5":
            manager.score_statistics(data)

        elif choice == "6":
            manager.score_ranking(data)
        
        elif choice == "7":
            manager.score_chart(data)

        elif choice == "8":
            manager.generate_report(data)

        elif choice == "9":
            print("退出系统")
            break

        else:
            print("输入错误")

if __name__ == "__main__":
    main()