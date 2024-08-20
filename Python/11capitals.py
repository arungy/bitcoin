#!/usr/bin/python

import sys

def main():
    print('Inside main')
    Capitals = dict()

    # Fill it with some values
    Capitals['Russia'] = 'Moscow'
    Capitals['Ukraine'] = 'Kiev'
    Capitals['USA'] = 'Washington'

    Countries = ['Russia', 'France', 'USA', 'Russia']

    for country in Countries:
        if country in Capitals:
            print('The capital of %s is %s' % (country, Capitals[country]))
        else:
            print('The capital of %s is %s' % (country, "**Unknown**"))

    #section 2
    Capitals = {'Russia' : 'Moscow', 'Ukraine' : 'Kiev', 'USA' : 'Washington'}
    print(Capitals)
    
    Capitals = dict(RA = 'Moscow', Ukraine = 'Kiev', USA = 'Washington')
    print(Capitals)

    Capitals = dict([("Russia", "Moscow"), ("Ukraine", "Kiev"), ("USA", "Washington")])
    print(Capitals)

    Capitals = dict(zip(["Russia", "Ukraine", "USA"], ["Moscow", "Keiv", "Washington"]))
    print(Capitals)

    #section 4
    A = dict(zip('abcdef', list(range(6))))

    print("")
    for key in A:
        print(key, A[key])

    print()
    A = dict(zip('abcdef', list(range(6))))
    for key, val in A.items():
        print(key, val)

    
    #section 3
    A = {'ab' : 'ba', 'aa' : 'bb', 'bb' : 'bb', 'ba' : 'ab' }

    key = 'ac'
    if key in A:
        del A[key]

    try:
        del A[key]
    except KeyError:
        print('There is no element with key "' + key + '" in dict')
    print(A)

    #section 4



#main function
if __name__ == "__main__":
    main()
    sys.exit(0)

