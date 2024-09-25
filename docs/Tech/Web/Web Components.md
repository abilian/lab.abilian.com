Web Components is a suite of different technologies allowing you to create reusable custom elements — with their functionality encapsulated away from the rest of your code — and utilize them in your web apps. Developed by the World Wide Web Consortium (W3C), Web Components represent a set of web platform APIs that enable developers to build encapsulated and reusable custom elements. 

## Underlying technologies

The main technologies underpinning Web Components include:

1. **Custom Elements**: This API allows developers to define new HTML tags (custom elements) and specify their behavior. With custom elements, you can create new HTML tags, extend existing ones, and encapsulate styles and functionalities, making your code more modular and reusable.

2. **Shadow DOM**: This technology enables encapsulated styling and markup structure within web components. The Shadow DOM is a way of creating a DOM "subtree" inside your element, which is separate from the main document's DOM. It allows you to include styles and scripts that are scoped to the component, preventing clashes with styles and scripts in the main document.

3. **HTML Templates**: The `<template>` and `<slot>` elements enable developers to write markup templates that are not displayed in the rendered page. These templates can be reused and instantiated as part of web components. The `<slot>` element is a placeholder inside a web component that you can fill with your own markup, allowing for flexible content projection inside the component.

4. **ES Modules**: Although not exclusively part of Web Components, JavaScript modules are often used in conjunction with them. ES Modules allow for the importation and encapsulation of JavaScript functionality, which is crucial for complex components.

## Why Web Components?

The significance of Web Components lies in their ability to:

- **Encapsulate Functionality**: Prevents style and scripting conflicts between components.
- **Promote Reusability**: Encourages a modular approach to web development, where components can be reused across different projects.
- **Improve Maintainability**: By keeping the component's internal workings separate from the rest of your code, it becomes easier to maintain and update.

Web Components are supported in most modern browsers, providing a standardized way to develop and use custom elements in web applications. This standardization is particularly valuable in complex web applications, where maintaining code can become challenging without proper organization and encapsulation.

## References

- https://medium.com/@mariusbongarts/react-vs-web-components-80d754f74811

"While Web Components provide strong encapsulation for reusable components, React provides a declarative library that keeps the DOM in sync with your data."

- https://blog.logrocket.com/web-components-vs-react/

"For example, web components are faster and more memory-efficient than React (according to [this benchmark](https://krausest.github.io/js-framework-benchmark/)) because they are browser-native. But creating web components using the standard API is complex and not so developer-friendly compared to JSX-based React. However, the Lit-like libraries let you create web components in a React-like simple way."

- https://web-highlights.com/blog/will-web-components-replace-frontend-frameworks-they-are-built-to-solve-different-problems/

## Components libraries

- https://open-wc.org/guides/community/component-libraries/
- https://github.com/SAP/ui5-webcomponents
- https://shoelace.style/

## Frameworks

- Stenciljs
- Lit https://lit.dev/
- WYC

### Lit vs. Stencil

Lit (formerly LitElement and lit-html), developed by the Polymer team at Google, is known for its simplicity and small size. It uses JavaScript templates, which makes it feel like just using JavaScript. It's excellent for building light-weight web components quickly.

Stencil, developed by the Ionic team, is more feature-rich and includes a number of built-in tools like a JSX renderer, automatic generation of components for various frameworks (React, Vue, Angular), and automatic generation of Progressive Web Apps. It's often seen as a toolchain or a compiler rather than just a library. Stencil could be a good choice if you need to create components that are compatible with multiple frameworks, or if you're building a large-scale application.

---

## Examples

### Slim.js

```javascript
import { Slim } from 'slim-js';
import { tag, template } from 'slim-js/decorators';

@tag('my-awesome-element')
@template(`
    <button @click="this.inc()"> + </button>
    <span>{{this.count}}</span>
    <button @click="this.dec()"> - </button>
`)
class extends Slim {
  count = 0;
  inc() { this.count++ }
  dec() { this.count-- }
}
```

https://github.com/slimjs/slim.js

### Lit

```javascript
import {html, css, LitElement} from 'lit';
import {customElement, property} from 'lit/decorators.js';

@customElement('simple-greeting')
export class SimpleGreeting extends LitElement {
  static styles = css`p { color: blue }`;

  @property()
  name = 'Somebody';
  
  render() {
    return html`<p>Hello, ${this.name}!</p>`;
  }
}
```

https://github.com/lit/lit/


### Hybrids.js

```javascript
import { html, define } from "hybrids";
  
function increaseCount(host) {
  host.count += 1;
}

export default define({
  tag: "simple-counter",
  count: 0,
  render: ({ count }) => html`
    <button onclick="${increaseCount}">
      Count: ${count}
    </button>
  `,
});
```

## References

- https://begin.com/blog/posts/2023-12-13-web-component-therapy
- https://blog.carlana.net/post/2023/web-component-alternative-futures/
- https://github.com/matschik/component-party.dev
