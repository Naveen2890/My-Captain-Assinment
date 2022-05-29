import csv
def write_into_csv(info_list):
     with open('student_info.csv','a', newline='')as csv_file :
          writer =csv.writer(csv_file)
          if csv_file.tell()==0:
               writer.writerow(["Name", "Age", "Phone no", "e_mail.id"])
          writer.writerow(info_list)
if __name__=='__main__':
     condition=True
     student_num=1
     
     while (condition):
         student_info=input("enter student information in the following format(name Age Phone_no email):")
         

         student_info_list=student_info.split(' ')
       
          

         print("Enterd information is -\nName: {}\nAge: {}\nphone no:{} \nemail:{}"
               .format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
         choice_check=input("The enterd info is correct?(yes/no):")
         if choice_check=="yes":
               write_into_csv(student_info_list)
               condition_check=input("enter YES/NO to if ou want enter info about another student:")
               if condition_check=="YES":
                    condition=True
               elif condition_check =="NO":
                    condition=False
         elif choice_check=="no":
               print("\n please renter the vlues!")