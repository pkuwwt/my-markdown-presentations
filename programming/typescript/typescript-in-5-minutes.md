
# TypeScript in 5 minutes

---

## Install TypeScript

  * Install by command line `npm`
```bash
npm install -g typescript
```

---

## Compile your first TypeScript file

  * For a script `hello.ts`:

```typescript
function greeter(person) {
    return "Hello, " + person;
}

let user = "Jane User";
console.log(greeter(user));
```

  * Compile syntax: `tsc hello.ts`
  * It will generate `hello.js`

```javascript
function greeter(person) {
    return "Hello, " + person;
}
var user = "Jane User";
console.log(greeter(user));
```

---

## Type Annotations

  * Type annotations is a lightweight way to enforce type checking
  * For example: `hello1.ts`

```typescript
function greeter(person: string) {
    return "Hello, " + person;
}

let user = [0, 1, 2];
console.log(greeter(user));
```
  * The compilation `tsc hello1.ts` will result in an error

```
error TS2345: Argument of type 'number[]' is not assignable to parameter of type 'string'.
```

  * Similarly, the call `greeter()` also leads to an error, because of wrong number of arguments.
  * Although there is error, the `.js` file is still generated. The errors are more like serious warnings.

---

## Interfaces

  * Interface is an abstract concept
  * There is no need to use `implements`, as the compatibility between two types are determined by their internal structures.
  * For example:

```typescript
interface Person {
    firstName: string;
    lastName: string;
}
function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}
let user = { firstName: "Jane", lastName: "User" };
console.log(greeter(user));
```

  * The `Person` interface and the `user` object are compatible, because they both have members `firstName` and `lastName`.

---

## Classes

  * Typescript supports object-oriented programming, just like Javascript.
  * The `class` and `interface` have different level of abstraction.
  * We can specify the `public` fields as the constructor parameters.

```typescript
class Student {
    fullName: string;
    constructor(public firstName: string, public middleInitial: string, public lastName: string) {
        this.fullName = firstName + " " + middleInitial + " " + lastName;
    }
}
interface Person {
    firstName: string;
    lastName: string;
}
function greeter(person: Person) {
    return "Hello, " + person.firstName + " " + person.lastName;
}
let user = new Student("Jane", "M.", "User");
console.log(greeter(user));
```

---

## References

  * [Typescript in 5 minutes](https://www.typescriptlang.org/docs/handbook/typescript-in-5-minutes.html)

