
# Session 1: Galileo and multiplication of objects

## Introduction

  * Goal of this book: explore the consequences of a new and fundamental insight about the nature of mathematics which has led to better methods for understanding and using mathematical concepts.
  * **Category**: a mathematical universe, corresponding to a particular subject matter.
    * There are ways to pass from one category to another 
    * Ingredients: objects, maps, compositions of maps
  * This chapter provides an informal introduction with some examples
  * Origin: **A workings of mathematics and the relationships of its parts**, 1945, by Eilenberg and Mac Lane
    * The categories involved in mathematics and their relationships have been implicit for centuries until 1945
    * This paper gave explicit definitions of the basic notions of category


---

## Galileo and the flight of a bird

  * Galileo wished to understand the precise motion of a thrown object
  * Everyone has observed the graceful parabolic arcs
  * Beyond the moving track, the motion involves the changing position for each instant
    * motion: `map/function` from `time` to `space`

```
      flight of birds
TIME  --------------> SPACE
```

  * For the multiplication `SPACE = PLANE x LINE`, we have

```

                             TIME
                                \  flight of birds
                                _\|
SPACE  -------------> LINE        SPACE  -------------> LINE     
  |        level                    |        level
  | shadow                          | shadow
  |                                 |
 \|/                               \|/
 PLANE                             PLANE                   
```

  * So we get two maps: `TIME ---> LINE` and `TIME ---> PLANE`

---

## Example: Multiplication as independent choices

  * Meals in restaurants with two courses:

|meals|||||2nd courses|
|---|---|---|---|---|---|------|
||soup,steak|pasta,steak|||steak|
||soup,veal|||<span style='font-size:20px;'>&#8680;</span>|veal|
||soup,chicken||||chicken|
||soup,fish||||fish|
||||||||
|||<span style='font-size:20px;'>&#8681;</span>|||||
||||||||
|**1st courses**|soup|pasta|salad|||

  * So the diagram is

     MEALS  <span style='font-size:30px;'>&#8680;</span> 2nd COURCES
	 </br>
    <span style='font-size:30px;'>&#8681;</span></br>
  1st COURCES

---

## Example: Multiplication in geometry dimensions

  * `CYLINDER = DISK x LEVEL`
  * Each point in a cycliner corresponds to a level point and a disk point
  * The volume of a cylinder is also the area of the disk multiplies the length of the level

---

## Example: Multiplication in logic

  * There is a connection between **multiplication** and **and**

     John is sick **and** Mary is sick <span style='font-size:30px;'>&#8680;</span> John is sick
	 </br>
    <span style='font-size:30px;'>&#8681;</span></br>
	Mary is sick

