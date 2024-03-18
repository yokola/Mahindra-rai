import queue as q
patient_name=q.Queue()
dispaly=None
name=str()
i=1
while i>0:
          print("Enter the option\n1.Register new patient\n2.Remove Patient\n3.View Patient\n4.Exit")
          opt=int(input("Enter the Option: \n"))
          if opt ==1:
                    name=str(input("\nEnter Patient name : "))
                    patient_name.put(name)
                    print("Patient registered successfully\n")
          #            for names in name:
          #                     display=patient_name.get()
          #                    # print(display)
          elif opt ==2:
                    if not patient_name.empty():
                              patient_name.get()
                              print("Patient Remove successfully")
          elif opt==3:
                    print("..............Patient(s) registered.............")
                    for names in name:
                              display=patient_name.get()
                              print(display)
          elif opt ==4:
                    print(".............Thank You for the Services.............")
          else:
                    print("............[Invalid option]...............\n")

