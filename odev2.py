studentInfo = []

def addStudents():
    studentInfo.append(input(" Eklemek istediğiniz ismi giriniz: "))
    print("Ekleme başarılı!")
    print("**********************************************************************")
    print("\n")
    menu()

def delStudent():
    studentInfo.remove(input(" Silmek istediğiniz ismi giriniz: "))
    print("Silme başarılı!")
    print("**********************************************************************")
    print("\n")
    menu()

def multiAdd():
    studentInfo.extend([input(" Toplu eklenecek isimleri ekleyin: ")])
    print("Ekleme başarılı!")
    print("**********************************************************************")
    print("\n")
    menu()

def list():
    for i in studentInfo:
        print("**********************************************************************")
        print(i)
    print("Listeleme başarılı!")
    print("**********************************************************************")
    print("\n")
    menu()

def searchIndex():
    print(studentInfo.index(input("bul: ")))
    print("Bulundu!")
    print("**********************************************************************")
    print("\n")
    menu()

def multiRemove():
    register = 0
    number = int(input("Kaç tane öğrenci silmek istiyorsunuz?: "))
    while register < number:
        studentInfo.pop()
        register +=1
    print("Silme başarılı!")
    print("**********************************************************************")
    print("\n")
    menu()

def menu():
    choose = int(input("""Yapmak istediğiniz işlem numarasını giriniz: 
    1) Öğrenci Ekle
    2) Öğrenci Sil
    3) Toplu öğrenci ekleme
    4) Liste elemanlarını yazdır
    5) Öğrenci Numarası bulma
    6) Toplu kayıt silme
    >>>"""))

    if choose == 1:
        addStudents()
    elif choose == 2:
        delStudent()
    elif choose == 3:
        multiAdd()
    elif choose == 4:
        list()
    elif choose == 5:
        searchIndex()
    elif choose == 6:
        multiRemove()
    else:
        quit()


menu()
