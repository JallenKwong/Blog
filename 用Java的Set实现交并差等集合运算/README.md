# 用Java的Set实现交并差等集合运算 #

creation date:2020-03-08 02: 45: 03

tag:Java,Set,集合运算

## 放码过来 ##

```java
package com.lun.util;

import java.util.HashSet;
import java.util.Set;

public class SetUtils {

	public static <T> Set<T> union(Set<T> setA, Set<T> setB) {
		Set<T> tmp = new HashSet<T>(setA);
		tmp.addAll(setB);
		return tmp;
	}

	public static <T> Set<T> intersection(Set<T> setA, Set<T> setB) {
		Set<T> tmp = new HashSet<T>();
		for (T x : setA)
			if (setB.contains(x))
				tmp.add(x);
		return tmp;
	}

	public static <T> Set<T> difference(Set<T> setA, Set<T> setB) {
		Set<T> tmp = new HashSet<T>(setA);
		tmp.removeAll(setB);
		return tmp;
	}

	public static <T> Set<T> symDifference(Set<T> setA, Set<T> setB) {
		Set<T> tmpA;
		Set<T> tmpB;

		tmpA = union(setA, setB);
		tmpB = intersection(setA, setB);
		return difference(tmpA, tmpB);
	}

	public static <T> boolean isSubset(Set<T> setA, Set<T> setB) {
		return setB.containsAll(setA);
	}

	public static <T> boolean isSuperset(Set<T> setA, Set<T> setB) {
		return setA.containsAll(setB);
	}

	public static void main(String args[]) {
		HashSet<Character> set1 = new HashSet<Character>();
		HashSet<Character> set2 = new HashSet<Character>();

		set1.add('A');
		set1.add('B');
		set1.add('C');
		set1.add('D');

		set2.add('C');
		set2.add('D');
		set2.add('E');
		set2.add('F');

		System.out.println("set1: " + set1);
		System.out.println("set2: " + set2);

		System.out.println("Union: " + union(set1, set2));
		System.out.println("Intersection: " + intersection(set1, set2));
		System.out.println("Difference (set1 - set2): " + difference(set1, set2));
		System.out.println("Difference (set2 - set1): " + difference(set2, set1));
		System.out.println("Symmetric Difference: " + symDifference(set1, set2));

		HashSet<Character> set3 = new HashSet<Character>(set1);

		set3.remove('D');
		System.out.println("set3: " + set3);

		System.out.println("Is set1 a subset of set2? " + isSubset(set1, set3));
		System.out.println("Is set1 a superset of set2? " + isSuperset(set1, set3));
		System.out.println("Is set3 a subset of set1? " + isSubset(set3, set1));
		System.out.println("Is set3 a superset of set1? " + isSuperset(set3, set1));

	}

}

/* result:

set1: [A, B, C, D]
set2: [C, D, E, F]
Union: [A, B, C, D, E, F]
Intersection: [C, D]
Difference (set1 - set2): [A, B]
Difference (set2 - set1): [E, F]
Symmetric Difference: [A, B, E, F]
set3: [A, B, C]
Is set1 a subset of set2? false
Is set1 a superset of set2? true
Is set3 a subset of set1? true
Is set3 a superset of set1? false

*/


```


## 参考资料 ##

[Set operations: union, intersection, difference, symmetric difference, is subset, is superset : Set « Collections Data Structure « Java](http://www.java2s.com/Code/Java/Collections-Data-Structure/Setoperationsunionintersectiondifferencesymmetricdifferenceissubsetissuperset.htm)
