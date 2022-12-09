import sys
import pandas as pd


#testing locally
dependence_values = {}
df1 = pd.read_csv(r'C:\Users\trish\Desktop\CSstars\edgelist.csv')
df2 = pd.read_csv(r'C:\Users\trish\Desktop\CSstars\clusters.csv')

node_ids = df2['node_id']
clusters = df2['cluster_id']
cited = df1['citing']
citing = df1['cited']

"""
#testing in virtual environment
df1 = pd.read_csv(sys.argv[1], header = None) #edgelist
df2 = pd.read_csv(sys.argv[2], header = None) #clusters
node_ids = df2[0]
clusters = df2[1]
cited = df[0]
citing = df[1]
"""





def find_references(cited, citing, doi):
    ref_list = list()
    for index, value in enumerate(cited):
        if value == doi:
            ref_list.append(citing[index])
    return ref_list

def find_references_cluster(cited, citing, doi, cluster):
    ref_list = list()
    for index, i in enumerate(cited):
        if i == doi and i in cluster:
            ref_list.append(citing[index])
    return ref_list
            

"""
def calculate_dependence(ref1, ref2, node):
    dependence_values[node] = [len(set(ref1).intersection(set(ref2))), round(len(set(ref1).intersection(set(ref2)))/len(ref1), 3)]
    len(set(ref1).intersection(set(ref2)))
"""
    
def print_table(values):
    print("node\tlevel\tdep\trel_dep\tindep")
    for node in values:
        print(str(node) + "\t"+  str(values.get(node)[0]) + "\t" + str(values.get(node)[1]) + "\t" + str(values.get(node)[2]))# + "\t" + str(values.get(node)[3]))
        

def main():
    for cluster in set(clusters):
        nodes = find_references(clusters, node_ids, cluster)
        
        for node in nodes:
            dependence = 0
            independence = 0
            references = find_references_cluster(cited, citing, node, nodes)
            referring = find_references_cluster(citing, cited, node, nodes)
            for ref in referring:
                references2 = find_references_cluster(cited, citing, ref, nodes)
                if (len(set(references).intersection(set(references2))) > 0):
                    dependence += 1
                else:
                    independence += 1
            dependence_values[node] = [len(references), dependence, independence]
    print_table(dependence_values)
    
main()
        
    
