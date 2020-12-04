from itertools import combinations

'''This is the answer to day 1 of the Advent of code, the question can be found here: https://adventofcode.com/2020/day/1
 
 For Part 1, I attempted to do a Binary Search to try and have a fairly fast answer, 
 I implemented the Binary search from memory, hence the hacky handling of 1 and 2 size arrays. 
 I could go back and make a proper implementation, but wheres the fun in that? 
 
 For Part 2, I decided to do it via combinations, this was much easier than using my Binary Search again,
 It would have been easier for part 1 also, but I opted to do that manually to have something a bit more substantial.
 
 '''


data = """1732
1972
1822
1920
1847
1718
1827
1973
1936
1865
1817
1954
1939
1979
1846
1989
1818
398
1786
1900
1949
1161
609
1967
1845
1795
1874
1982
2010
1494
1752
1803
1908
1876
1977
1999
1858
1885
1975
1878
1784
1787
1765
1778
1893
1746
1807
1966
1991
1905
1970
1942
1792
1750
713
1871
1860
1931
1976
1771
128
390
2006
1801
1946
1914
1833
1515
1958
1737
1887
1962
1895
2004
1747
1841
1793
1948
1790
1808
1957
1770
1960
1952
1932
1782
1762
1898
1919
1909
1929
1964
1848
1959
1381
280
1899
1855
1849
1889
1772
1843
1767
1830
1838
1869
1926
1768
1789
1791
1888
1371
2001
1943
1741
1904
1468
1969
1910
649
1953
1916
1852
1996
1842
1950
1850
1998
1963
1780
1883
1955
443
1773
1896
1985
1809
2007
1819
1891
1853
1802
1861
1813
1831
1974
1915
1997
2000
1945
1832
1763
1981
1922
1862
1944
1925
1742
1744
1994
1961
1881
1937
1911
1788
1971
1890
1734
1781
1984
1912
1834
1766
1769
1797
195
1965
1934
1894
1928
1759
1812
1758
1988
1821
1776
2009
1749
1857
1785
1824
1796
1930
1777
1886
477
1761
1800
1745
1993"""

split_data = data.split("\n")
split_data = list(map(int, split_data))
sorted_data = sorted(split_data)


def bsearch (list, value):
    middle = (len(list) - 1)//2

    if list[middle] == value:
        print("Value found!")
        return True

    elif len(list) == 2:
        if list[0] == value or list[1] == value:
            return value
        else:
            return None

    elif len(list) == 1:
        if list[0] == value:
            return value
        else:
            return None

    elif value < list[middle]:
        return bsearch(list[:middle], value)
    else:
        return bsearch(list[middle:], value)



#2 numbers
for x in sorted_data:
    temp = sorted_data
    difference = 2020 - x
    if bsearch(sorted_data, difference):
        print("Value found!, your two numbers are " + str(x) + " and " + str(difference) + " Multiplied together they equal " + str(x * difference))
        break


#3 numbers

three_combination = list(combinations(sorted_data, 3))

for combo in three_combination:
    if sum(combo) == 2020:
        print("Wow, that was easy! here are the numbers: " + str(combo) + " here they are multiplied: " + str(combo[0] * combo[1] * combo[2] ))