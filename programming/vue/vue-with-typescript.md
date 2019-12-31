
# Vue with TypeScript


---

## Why TypeScript?

  * TypeScript leads to faster coding, and helps to catch and rectify more problems in development time
  * TypeScript enables IDE to provide features like intellisense, auto-complete etc.
    * For example: figure out the return type of an async function

---

## Setup

  * Install `Vue Cli 3`
```bash
npm install -g @vue/cli
```
  * Create a project support TypeScript
```
# choose the "Manually select features"
vue create your-project
```
  * Choose an IDE
    * Prefer [Visual Studio Code](https://code.visualstudio.com/) with [Vetur extension](https://github.com/vuejs/vetur)
    * WebStorm also support Vue and TypeScript 

---

## Basic Usage

```vue
import Vue from 'vue'

const Component = Vue.extend({
  // type inference enabled
})

const Component = {
  // this will NOT have type inference,
  // because TypeScript can't tell this is options for a Vue component.
}
```

---

## Class-Style Vue Components

```vue
import Vue from 'vue'
import Component from 'vue-class-component'

// The @Component decorator indicates the class is a Vue component
@Component({
  // All component options are allowed in here
  template: '<button @click="onClick">Click!</button>'
})
export default class MyComponent extends Vue {
  // Initial data can be declared as instance properties
  message: string = 'Hello!'

  // Component methods can be declared as instance methods
  onClick (): void {
    window.alert(this.message)
  }
}
```

---

## Annotating Return Types

  * Because of the circular nature of Vue's declaration files, TypeScript may have difficulties inferring the types of certain methods
  * We may need to annotate the return type on methods like `render` and those in `computed`.

```vue
import Vue, { VNode } from 'vue'

const Component = Vue.extend({
  data () {
    return {
      msg: 'Hello'
    }
  },
  methods: {
    greet (): string {      // need annotation due to `this` in return type
      return this.msg + ' world'
    }
  },
  computed: {
    greeting(): string {    // need annotation
      return this.greet() + '!'
    }
  },
  // `createElement` is inferred, but `render` needs return type
  render (createElement): VNode { 
    return createElement('div', this.greeting)
  }
})
```

---

## `tsconfig.json`



---

## Mix JavaScript and TypeScript


---

## References

  * [Vue.js with TypeScript](https://johnpapa.net/vue-typescript/)
  * [TypeScript Vue Starter](https://github.com/microsoft/typescript-vue-starter)
  * [Official Support for TypeScript](https://vuejs.org/v2/guide/typescript.html)

