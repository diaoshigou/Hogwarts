class Student:
    def __init__(self,id,s,n):
        self.id = id
        self.sex = s
        self.name = n
    pass


class StudentList:
    def __init__(self, student_list):
        self.s_list = student_list

    def get(self, student_id):

        print(student_id.id)
        print(student_id.sex)
        print(student_id.name)
        pass

    def delete(self, student_id):
        del student_id
        pass


if __name__ == '__main__':
    # 入参自己定义
    s1 = Student("10001","男","张三2")
    s2 = Student("10002","女","李四")
    s3 = Student("10003","男","王五")
    # 初始化一个成员名单
    s_list = StudentList([s1, s2, s3])
    # 实现get()方法
    s_list.get(s1)
    # 实现delete
    s_list.delete(s1)