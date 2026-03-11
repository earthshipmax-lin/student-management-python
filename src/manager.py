import pandas as pd
import matplotlib.pyplot as plt


# 读取数据
def load_data():
    return pd.read_csv("../data/students.csv")


# 显示学生
def show_students(data):
    print("\n学生列表:")
    print(data)


# 添加学生
def add_student(data):

    id = int(input("输入学生ID: "))
    name = input("输入学生姓名: ")
    score = int(input("输入学生成绩: "))

    new_student = pd.DataFrame({
        "id":[id],
        "name":[name],
        "score":[score]
    })

    data = pd.concat([data,new_student],ignore_index=True)

    data.to_csv("../data/students.csv",index=False)

    print("学生添加成功")


# 删除学生
def delete_student(data):

    id = int(input("输入要删除的学生ID: "))

    data = data[data["id"] != id]

    data.to_csv("../data/students.csv",index=False)

    print("删除成功")


# 查询学生
def find_student(data):

    name = input("输入学生姓名: ")

    result = data[data["name"] == name]

    print(result)


# 成绩统计
def score_statistics(data):

    print("\n成绩统计:")
    print("学生人数:", len(data))
    print("平均成绩:", data["score"].mean())
    print("最高成绩:", data["score"].max())
    print("最低成绩:", data["score"].min())


# 成绩排名
def score_ranking(data):

    sorted_data = data.sort_values(by="score", ascending=False)

    print("\n成绩排名:")
    print(sorted_data)

    sorted_data.to_csv("../score_rank.csv", index=False)

    print("排名已保存为 score_rank.csv")


# 成绩分布图
def score_chart(data):

    plt.hist(data["score"], bins=5)

    plt.title("Score Distribution")
    plt.xlabel("Score")
    plt.ylabel("Number of Students")

    plt.savefig("../score_distribution.png")

    print("成绩图已保存为 score_distribution.png")

# 生成成绩报告
def generate_report(data):

    total = len(data)
    avg = data["score"].mean()
    max_score = data["score"].max()
    min_score = data["score"].min()

    report = f"""
学生成绩报告

学生人数: {total}
平均成绩: {avg}
最高成绩: {max_score}
最低成绩: {min_score}
"""
    
    with open("../score_report.txt", "w") as f:
        f.write(report)

    print("成绩报告已生成: score_report.txt")