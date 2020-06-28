# Author 
# AL BIRR KARIM SUSANTO
# https://github.com/albirrkarim
# Berdasarkan contoh di -> Model-pert.pdf

# Struktur Encode

# data Node
# struktur
# [idxNode,ET,EL]

# data relation
# [idxOfThisNode,idxOfDestinationNode,a,m,b,t,v]

# Keterangan

# a = Waktu terpendek yang mungkin untuk menyelesaikan kegiatan i-j, atau disebut optimistic time.
# m = Waktu yang paling mungkin untuk menyelesaikan kegiatan i-j, atau disebut realistic time.
# b = Waktu terlama yang mungkin untuk menyelesaikan kegiatan i-j, atau disebut pessimistic time .
# t = time
# v = variansi

# Konfigurasi encode
idxOfThisNode   = 0
idxOfDestNode   = 1
idxOfTime       = 5
idxOfVarian     = 6



dataNode=[
    [1,0,0],
    [2,0,0],
    [3,0,0],
    [4,0,0],
    [5,0,0],
]

dataRelation=[
    [1,2,5,8,17,0,0],
    [1,3,7,10,13,0,0],
    [2,3,3,5,7,0,0],
    [2,4,1,3,5,0,0],
    [3,4,4,6,8,0,0],
    [3,5,3,3,3,0,0],
    [4,5,3,4,5,0,0],
]


# Hitung T dan v
def hitungT(a,m,b):
    return (a + (4*m) + b)/6

def hitungV(a,b):
    return pow((b-a)/6,2)


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


def hitungTandV(dataRelation):
    for row in dataRelation:
        a = row[2]
        m = row[3]
        b = row[4]

        row[5] = hitungT(a,m,b)
        row[6] = hitungV(a,b)

    return dataRelation
    

# Hitung T dan V
dataRelation = hitungTandV(dataRelation)
# print(dataRelation)



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
sumVariansi  = 0

for row in dataRelation:

    if(row[idxOfThisNode] == criticalPath[idx] and row[idxOfDestNode] == criticalPath[idx+1] ):
        idx+=1
        criticalTime += row[idxOfTime]
        sumVariansi  += row[idxOfVarian]

print("\n\nCritical Time")
print(criticalTime)


print("\n\nVariansi")
print(sumVariansi)