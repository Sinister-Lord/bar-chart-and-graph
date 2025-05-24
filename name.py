import matplotlib.pyplot as plt 
students_names=["sanjay","Rahul","Karan","Wasim","Ramesh","Ajay","Sartaj","Priya"]
students_marks=[35,50,20,45,25,40,25,40]

def line_chart():
    plt.plot (students_names,students_marks,marker="^",ms=20,mec="r",linestyle="dotted")

    plt.xlabel ("student_names")

    plt.ylabel("student_marks")

    plt.title("student_marks_graph")
    plt.show()

line_chart()

def bar_graph():
    plt.bar (students_names,students_marks)

    plt.xlabel ("student_names")

    plt.ylabel("student_marks")

    plt.title("student_marks_graph")
    plt.show()

bar_graph()