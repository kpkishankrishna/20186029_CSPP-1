'''
dict_face = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
def face_values(hand):
    face_values = []
    for i in hand:
        face_values.append(dict_face[i[0]])
    return face_values
 '''
print(len(set([1, 1, 1, 1, 2])) == 2)