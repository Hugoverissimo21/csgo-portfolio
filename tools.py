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

def qnt_de_(file): ##### por acabar
    csv_lines = csv.reader(open(file,"r"))
    item_list = []
    for line in csv_lines:
        item_list.append(line[2])
    item_list.remove(item_list[0])
    procura = input("Queres ver o quê? ")
    if procura in item_list:
        item_index = []
        item_index_id = 0
        for item in item_list:
            if item == procura:
                item_index.append(item_index_id)
            intem_index_id += 1
        return(item_index_id)
    else:
        return("Item não encontrado")

if __name__ == "__main__":
    print(total_invested("db.csv"),"from f(total_invested)")
    print(qnt_de_("db.csv"),"from f(qnt_de_)")
