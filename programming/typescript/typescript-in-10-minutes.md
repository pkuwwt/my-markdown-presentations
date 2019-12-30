
# TypeScript in 10 minutes

  * TypeScript is object-oriented programming language developed by Microsoft
  * TypeScript is a superset of JavaScript
  * File extension of TypeScript file is `.ts`
  * TypeScript compiler `tsc` converts `.ts` file to `.js` file

---

## Why TypeScript?

  * Opensource
  * It simplifies the `JavaScript` code and speeds up the development and debugging
  * It provides all the benefits of `ES6`, plus more productivity
  * It helps to avoid common and painful bugs by type checking
  * It is the superset of ES3, ES5, ES6
  * Support object-oriented programming
  * It has features like: interface, generic, inheritance, method access modifiers
  * It needs compiling before release, which reduces syntax errors and type errors

---

## Installing TypeScript

  * Install Typescript by `npm`

```bash
npm install -g typescript
tsc --version
```

---

## Writing first TypeScript Program

  * A first script: `hello.ts`

```typescript
function helloUser(user: string){
  return `Hello ${user}`
}
let msg = helloUser('World');
console.log(msg);
```

  * Compile it with `tsc hello.ts`, and it will generate `hello.js`

```javascript
function helloUser(user) {
return "Hello " + user;
}
var msg = helloUser('World');
console.log(msg);
```

  * Then we execute it with `node hello.js`

  * A note about `let`

    * `let` is alternative to `var`
    * `let` is new in ES6, and supported by TypeScript
    * In ES6, `let` has block scope, while `var` has weird function scope.
    * We should use `let` whenever possible.

---

## Data Types in TypeScript (1)

  * `boolean`: `true` or `false`
```typescript
let isReady: boolean = false;
let isDone: boolean;
```
  * `number`: numeric values
```typescript
let decimal: number = 6;
let hex: number = 0xf00d;
let binary: number = 0b1010;
let octal: number = 0o744;
```
  * `string`: text data
```typescript
let title: string = 'Hello World';
let concat: string;
concat = `${title}!`
```
  * `Array`: arrays of values
    * Homogeneous elements of array: `let list: Array<number> = [1, 2, 3];`
	* Non-homogeneous elements of array: `let list: Array<any> = ['a', 1];`

---

## Data Types in TypeScript (2)

  * Tuple: a type with fixed number of elements
```typescript
let x: [string, number] = ['hello', 10];
x = [10, 10]; // error
```
  * `enum`: a friendly way to express numeric values with names
```typescript
enum Color {Red, Green, Blue} // Red = 0, Green = 1, Blue = 2 
let c: Color = Color.Green;
console.log(c); // 1
```
  * `any`: unknown type
```typescript
let noSure: any = 4;
noSure = 'hello';
```
  * `void`: like `any`, the absense of any type, only support `undefined` and `null`
```typescript
function warnUser(): void {
        console.log('This is a warning message');
}
```

---

## Data Types in TypeScript (3)

  * `never`: the type of values never occur
```typescript
function error(msg: string): never {
        throw new Error(msg);
}
function fail() {
        return error('failed');
}
```
  * `Object`: `Object` in JavaScript, non-primitive type
```typescript
let employee: Object = {name: 'John', age: 10};
```

---

## Using Classes (1)

  * Class allows using object-oriented programming concepts like inheritance, encapsulation, abstraction and polymorphism.
  * Keyword `extends` is used to implement inheritance

```typescript
class Person{
    firstName = "";
    lastName = "";
    constructor(firstName: string, lastName: string){
      this.firstName = firstName;
      this.lastName = lastName;
    }
    fullName(){
      return `${this.firstName} ${this.lastName}`
    }
}
let p = new Person("John", "Snow");
console.log("Name: ", p.fullName());
```

---

## Using Classes (2)

```typescript
class Animal {
    move(distanceInMeters: number = 0) {
        console.log(`Animal moved ${distanceInMeters}m.`);
    }
}

class Dog extends Animal {
    bark() {
        console.log('Woof! Woof!');
    }
}

class Human extends Animal {
    talk() {
        console.log('Hello World! I\'m Chitti!');
    }
}

const dog = new Dog();
dog.move(10);
dog.bark();

const human = new Human();
human.move(100)
human.talk()
```
---

## Using Interfaces

  * An `interface` is a specification that defines a set of methods and properties to be implemented by a class/function

```typescript
// class using an interface
interface ClockInterface {
  currentTime: Date;
  setTime(d: Date): void;
}
class Clock implements ClockInterface {
  currentTime: Date = new Date();
  setTime(d: Date) {
      this.currentTime = d;
  }
  constructor(h: number, m: number) { }
}
// function using an interface
interface LabeledValue {
  label: string;
}

function printLabel(labeledObj: LabeledValue) {
    console.log(labeledObj.label);
}

let myObj = {size: 10, label: "Size 10 Object"};
printLabel(myObj);
```

---

## Using Decorators

  * A decorator is a special kind of declaration that can be attached to a class declaration, method, accessor, property or parameter
  * A decorator may or may not receive arguments based on its declaration

```typescript
function course(target) {
  Object.defineProperty(target.prototype, 'course', {value: () => "Angular"})
}

@course
class Person {
    firstName;
    lastName;

    constructor(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
}
let asim = new Person("Alex", "W");
console.log(asim.course()); //output: Angular
```

  * The `course` decorator adds a property `course` to the decorated class `Person` when it is initialized

---

## Generics

  * Generics are templates that allow the same function to accept arguments of various different types
  * Creating reusable components using generics is better than `any` data type, as generics preserve the types of the variables.

```typescript
function genericFunc<T>(argument: T): T[] {
    var arrayOfT: T[] = [];    // Create empty array of type T.
    arrayOfT.push(argument);   // Push, now arrayOfT = [argument].
    return arrayOfT;
}

var arrayFromString = genericFunc<string>("beep");
console.log(arrayFromString[0]);         // "beep"
console.log(typeof arrayFromString[0])   // String

var arrayFromNumber = genericFunc(42);
console.log(arrayFromNumber[0]);         // 42
console.log(typeof arrayFromNumber[0])   // number
```

  * Other generics examples can be found [here](https://www.typescriptlang.org/docs/handbook/generics.html).

---

## Modules

  * Modularity is important for large applications.
  * Spliting code into small and reusable components makes the projects organized and understandable.
  * TypeScript has a syntax for importing and exporting modules, but cannot handle the actual wiring between files.
  * To enable external modules, we need 3rd-party libraries like [require.js](http://requirejs.org/) for browser and [CommonJS](https://en.wikipedia.org/wiki/CommonJS) for Node.js

  * Following are the two sample code files: `exporter.ts`, `importer.ts`

```typescript
// exporter.ts
var sayHi = function(): void {
    console.log("Hello!");
}
export = sayHi;

// importer.ts
import sayHi = require('./exporter');
sayHi();
```
  * For `require.js`, we should compile the modules by `tsc --module amd *.ts`
  * More information refer to [TypeScript modules](https://www.typescriptlang.org/docs/handbook/modules.html) and [require.js usage](http://requirejs.org/docs/start.html)

---


## References

  * [TypeScript in 10 minutes: A quick introduction to typescript and its usage](https://www.agiliq.com/blog/2019/07/typescript-in-10-minutes/)
  * [Learn TypeScript in 30 minutes](https://tutorialzine.com/2016/07/learn-typescript-in-30-minutes)
  * [TypeScript Documentation](https://www.typescriptlang.org/docs/home.html)

