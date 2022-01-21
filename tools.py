import csv

def total_invested(file):
    csv_lines = csv.reader(open(file,"r"))
    spent_list =[]
    for line in csv_lines:
        spent_list.append(line[3])
    spent_list.remove(spent_list[0])
    total_spent = 0
    for value in spent_list:
        total_spent += float(value)
    return(total_spent)

def qnt_de_(file):
    csv_lines = csv.reader(open(file,"r"))
    csv_lines2 = csv.reader(open(file,"r"))
    item_list = []
    for [qty , name , type , spent, purchased , notes_info] in csv_lines:
        item_list.append(type)
    item_list.remove(item_list[0])
    procura = input("Queres ver o quê? ")
    if procura in item_list:
        item_index = []
        item_index_id = 0
        for item in item_list:
            if item == procura:
                item_index.append(item_index_id)
            item_index_id += 1
        line = int("-1")
        quantidades = 0
        for a in csv_lines2:
            line +=1
            if line in item_index:
                quantidades += int(a[0])
        return(str(quantidades) + " itens / " + str(item_index_id) + " tipos")
    else:
        return("Item não encontrado")




if __name__ == "__main__":
    print(total_invested("db.csv"),"from f(total_invested)")
    print(qnt_de_("db.csv"),"from f(qnt_de_)")
