# Author 
# AL BIRR KARIM SUSANTO
# https://github.com/albirrkarim
# Berdasarkan contoh di -> Model-CPM.pdf

# Struktur Encode

# struktur setiap node
# [idxNode,ET,LT]

dataNode = [
    [1,0,0],
    [2,0,0],
    [3,0,0],
    [4,0,0],
    [5,0,0],
    [6,0,0],
    [7,0,0],
    [8,0,0],
]

# Data relasi antar node
# [idxOfThisNode,idxOfDestinationNode,time]

dataRelation=[
    [1,2,12],
    [2,3,8],
    [2,4,4],
    [2,5,3],
    [3,6,12],
    [4,6,18],
    [4,5,5],
    [5,7,8],
    [6,7,4],
    [7,8,6],
]

# Konfigurasi encode
idxOfThisNode   = 0
idxOfDestNode   = 1
idxOfTime       = 2



def hitungET(dataNode,dataRelation,idxOfThisNode,idxOfDestNode,idxOfTime):
    # Menghitung ET
    # Forward iteration
    # Start to finish

    for i in range(0,len(dataRelation)):
        nodeDest    = dataRelation[i][idxOfDestNode]

        kandidat = []

        for j in range(0,len(dataRelation)):

            if(dataRelation[j][idxOfDestNode] == nodeDest):
                that    = dataRelation[j][idxOfThisNode]

                ETSebelum = dataNode[ that -1][1]
                time      = dataRelation[j][idxOfTime]

                kandidat.append( time + ETSebelum )


        # print(kandidat)
        # print(nodeDest)
        # print("\n\n")
        dataNode[nodeDest-1][1] =  max(kandidat)

    return dataNode

def hitungEL(dataNode,dataRelation,idxOfThisNode,idxOfDestNode,idxOfTime):

    # Menghitung EL
    # Backward
    # From finish to start

    for i in range(len(dataRelation)-1,-1,-1):

        node        = dataRelation[i][idxOfThisNode]

        kandidat = []
        for j in range(len(dataRelation)-1,-1,-1):

            if(dataRelation[j][idxOfThisNode] == node):
                
                that        = dataRelation[j][idxOfDestNode]
                ELSebelum   = dataNode[ that -1][2]

                time =  dataRelation[j][idxOfTime]

                kandidat.append( ELSebelum - time )

        # print(kandidat)
        # print(node)
        # print("\n\n")

        dataNode[node-1][2] =  min(kandidat)

    return dataNode

def makeCriticalPath(dataNode):
    criticalPath=[]
    for row in dataNode:
        # Jika ET sama dengan EL
        if(row[1] == row[2]):
            criticalPath.append(row[0])

    return criticalPath



# Menghitung ET 
dataNode = hitungET(dataNode,dataRelation,idxOfThisNode,idxOfDestNode,idxOfTime)
# print(dataNode)



# Mengisi EL dengan nilai ET pada node terakhir
# Node terakhir ET = EL 
dataNode[len(dataNode)-1][2]=dataNode[len(dataNode)-1][1] 
# print(dataNode)



# Menghitung EL
dataNode = hitungEL(dataNode,dataRelation,idxOfThisNode,idxOfDestNode,idxOfTime)
print("Data Node with ET and EL")
print(dataNode)



# Membuat critical path
criticalPath = makeCriticalPath(dataNode)
print("\n\nCritical Path")
print(criticalPath)



# Menghitung criticalTime dan sumVariansi
idx=0
criticalTime = 0
for row in dataRelation:

    if(row[idxOfThisNode] == criticalPath[idx] and row[idxOfDestNode] == criticalPath[idx+1] ):
        idx+=1
        criticalTime += row[idxOfTime]
     

print("\n\nCritical Time")
print(criticalTime)